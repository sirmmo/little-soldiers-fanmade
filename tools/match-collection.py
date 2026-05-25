#!/usr/bin/env python3
"""Match a figure collection against role sheets' figureCandidates.

Given a collection of figures you own and a set of sheets that list
`figureCandidates` (e.g. the Mage Knight 'Magestone' set), report which roles you
can field from what you own — and which candidate minis to use for each.

Collection file format (JSON):
    {
      "name": "My Mage Knight collection",
      "figures": [
        { "name": "Utem Crossbowman" },
        { "name": "Amotep Incinerator", "faction": "Atlantis Guild" },
        ...
      ]
    }
Matching is by figure name, case-insensitive and whitespace-trimmed.

Usage:
    python3 tools/match-collection.py <collection.json> [sheet-or-dir ...]
    # defaults to sets/mageknight/soldiers if no sheets are given
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_TARGETS = [os.path.join(ROOT, "sets", "mageknight", "soldiers")]


def norm(s):
    return " ".join(str(s).split()).lower()


def gather_sheets(targets):
    out = []
    for t in targets:
        if os.path.isdir(t):
            for dirpath, _, files in os.walk(t):
                for fn in sorted(files):
                    if fn.endswith(".json"):
                        out.append(os.path.join(dirpath, fn))
        elif t.endswith(".json"):
            out.append(t)
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    with open(argv[1]) as f:
        collection = json.load(f)
    owned = {norm(fig["name"]): fig for fig in collection.get("figures", [])}
    owned_names = {fig.get("name", k) for k, fig in owned.items()}

    targets = argv[2:] or DEFAULT_TARGETS
    sheets = gather_sheets(targets)

    print("Collection: %s  (%d figures)" % (collection.get("name", "(unnamed)"), len(owned)))
    print("Matching against %d sheet(s)\n" % len(sheets))

    fieldable = 0
    roles = 0
    used = set()
    for path in sheets:
        sheet = json.load(open(path))
        cands = sheet.get("figureCandidates")
        if not cands:
            continue
        roles += 1
        have = []
        for c in cands:
            if norm(c["name"]) in owned:
                have.append(c)
                used.add(norm(c["name"]))
        status = "FIELDABLE" if have else "no figure owned"
        if have:
            fieldable += 1
        print("%-16s [%s]" % (sheet.get("name", os.path.basename(path)), status))
        for c in cands:
            mark = "x" if norm(c["name"]) in owned else " "
            fac = (" — %s" % c["faction"]) if c.get("faction") else ""
            print("    [%s] %s%s" % (mark, c["name"], fac))
        print()

    print("%d of %d roles fieldable from this collection." % (fieldable, roles))

    leftover = sorted(n for n in owned if n not in used)
    if leftover:
        print("\nOwned figures not matched to any role candidate:")
        for n in leftover:
            print("  - %s" % owned[n].get("name", n))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
