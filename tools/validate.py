#!/usr/bin/env python3
"""Validate Little Soldiers sheet JSON files against soldier-sheet.schema.json.

Uses the `jsonschema` package if it is installed; otherwise falls back to a small
self-contained validator that supports exactly the JSON-Schema features used by
our schema ($ref, allOf, if/then/else, properties, required, additionalProperties,
enum, const, type, items, minItems, minLength, minimum, boolean schemas).

Usage:
    python3 validate.py                 # validate every examples/*.json
    python3 validate.py path/to.json    # validate specific file(s)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCHEMA_PATH = os.path.join(ROOT, "schema", "soldier-sheet.schema.json")
EXAMPLES_DIR = os.path.join(ROOT, "examples")


# --------------------------------------------------------------------------- #
# Minimal JSON-Schema validator (used only when `jsonschema` is unavailable).  #
# --------------------------------------------------------------------------- #
def _resolve_ref(root, ref):
    if not ref.startswith("#/"):
        raise ValueError("only local refs supported: %s" % ref)
    node = root
    for part in ref[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        node = node[part]
    return node


def _type_ok(value, t):
    if t == "object":
        return isinstance(value, dict)
    if t == "array":
        return isinstance(value, list)
    if t == "string":
        return isinstance(value, str)
    if t == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if t == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if t == "boolean":
        return isinstance(value, bool)
    if t == "null":
        return value is None
    return True


def _validate(value, schema, root, path, errors):
    # boolean schemas
    if schema is True:
        return
    if schema is False:
        errors.append("%s: not allowed here" % (path or "<root>"))
        return

    if "$ref" in schema:
        _validate(value, _resolve_ref(root, schema["$ref"]), root, path, errors)
        # a $ref in our schema is the whole subschema; nothing else alongside it
        return

    if "const" in schema and value != schema["const"]:
        errors.append("%s: must equal %r (got %r)" % (path, schema["const"], value))
    if "enum" in schema and value not in schema["enum"]:
        errors.append("%s: %r not in %r" % (path, value, schema["enum"]))

    if "type" in schema:
        types = schema["type"]
        types = types if isinstance(types, list) else [types]
        if not any(_type_ok(value, t) for t in types):
            errors.append("%s: expected type %s (got %s)" % (path, types, type(value).__name__))

    if isinstance(value, str) and "minLength" in schema and len(value) < schema["minLength"]:
        errors.append("%s: shorter than minLength %d" % (path, schema["minLength"]))
    if isinstance(value, (int, float)) and not isinstance(value, bool) and "minimum" in schema:
        if value < schema["minimum"]:
            errors.append("%s: %r < minimum %r" % (path, value, schema["minimum"]))

    if isinstance(value, dict):
        for req in schema.get("required", []):
            if req not in value:
                errors.append("%s: missing required property '%s'" % (path or "<root>", req))
        props = schema.get("properties", {})
        for k, v in value.items():
            if k in props:
                _validate(v, props[k], root, "%s.%s" % (path, k), errors)
            else:
                ap = schema.get("additionalProperties", True)
                if ap is False:
                    errors.append("%s: unexpected property '%s'" % (path or "<root>", k))
                elif isinstance(ap, dict):
                    _validate(v, ap, root, "%s.%s" % (path, k), errors)

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append("%s: fewer than minItems %d" % (path, schema["minItems"]))
        items = schema.get("items")
        if isinstance(items, dict) or items is True or items is False:
            for i, item in enumerate(value):
                _validate(item, items, root, "%s[%d]" % (path, i), errors)

    for sub in schema.get("allOf", []):
        _validate(value, sub, root, path, errors)

    if "if" in schema:
        probe = []
        _validate(value, schema["if"], root, path, probe)
        branch = "then" if not probe else "else"
        if branch in schema:
            _validate(value, schema[branch], root, path, errors)


def _validate_builtin(instance, schema):
    errors = []
    _validate(instance, schema, schema, "", errors)
    return errors


# --------------------------------------------------------------------------- #
def validate_one(path, schema, use_lib):
    with open(path) as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            return ["JSON parse error: %s" % e]
    # Not a sheet (e.g. a collection file) — skip rather than fail.
    if isinstance(data, dict) and "kind" not in data and "schemaVersion" not in data:
        return None
    if use_lib:
        import jsonschema
        v = jsonschema.Draft202012Validator(schema)
        return ["%s: %s" % ("/".join(map(str, e.path)) or "<root>", e.message)
                for e in sorted(v.iter_errors(data), key=lambda e: list(e.path))]
    return _validate_builtin(data, schema)


def main(argv):
    with open(SCHEMA_PATH) as f:
        schema = json.load(f)

    try:
        import jsonschema  # noqa: F401
        use_lib = True
        engine = "jsonschema library"
    except ImportError:
        use_lib = False
        engine = "built-in fallback validator"

    targets = argv[1:]
    if not targets:
        targets = [os.path.join(EXAMPLES_DIR, f)
                   for f in sorted(os.listdir(EXAMPLES_DIR)) if f.endswith(".json")]

    print("Validating %d file(s) with the %s\n" % (len(targets), engine))
    failures = 0
    skipped = 0
    for path in targets:
        errors = validate_one(path, schema, use_lib)
        name = os.path.relpath(path, ROOT)
        if errors is None:
            skipped += 1
            print("SKIP  %s (not a sheet)" % name)
        elif errors:
            failures += 1
            print("FAIL  %s" % name)
            for e in errors:
                print("        - %s" % e)
        else:
            print("PASS  %s" % name)

    passed = len(targets) - failures - skipped
    tail = (", %d skipped" % skipped) if skipped else ""
    print("\n%d passed, %d failed%s" % (passed, failures, tail))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
