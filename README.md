# Little Soldiers — Sheet System

A generalization of the *Little Soldiers* rules into a reusable system for designing new
**sheets**: Little Soldiers, Generals, Threats, Tactics cards, and Objects. Built from all
three rulebooks in the parent folder (Bootcamp + Modules + Missions).

```
sheet-system/
├─ FRAMEWORK.md                     ← the rules generalization (read this first)
├─ schema/
│   └─ soldier-sheet.schema.json    ← machine-readable model (JSON Schema 2020-12, v1.2)
├─ examples/                        ← 11 sheets across all five kinds
│   ├─ infantry · sniper · grenadier · operator           (Little Soldiers, both ranks)
│   ├─ general-brick · general-dinosaur                    (Generals; Dinosaur has signature Tactics)
│   ├─ threat-pinky                                        (co-op Threat)
│   ├─ tactic-trigger-happy · tactic-camouflage            (Tactics cards: Soldier + Reaction)
│   ├─ object-teleporter                                   (Object power)
│   └─ medic                                               (homebrew worked example)
├─ tools/
│   ├─ validate.py                  ← validates sheets against the schema (no deps required)
│   └─ match-collection.py          ← reports which roles you can field from figures you own
├─ templates/
│   └─ card-template.html           ← print-ready fill-in cards (all five sheet kinds)
└─ sets/
    └─ medieval/                    ← "Realms at War": a full medieval adaptation (see its MEDIEVAL.md)
        ├─ MEDIEVAL.md              ← themed ruleset + terminology reskin + roster
        ├─ soldiers/  generals/  objects/  tactics/  threats/   (19 schema-valid sheets)
```

## Sets

Themed adaptations live under `sets/`, each reusing this same schema and validator:

- **`sets/medieval/` — Realms at War.** A medieval reskin + expansion: 6 Warriors (Man-at-Arms,
  Longbowman, Bombard, Siege Engineer, Knight, Cleric), 4 Lords incl. historical commanders
  (Richard the Lionheart, Saladin) with signature Stratagems, 4 Objects, 11 Stratagems, and a
  co-op boss (The Old Wyrm). Read `sets/medieval/MEDIEVAL.md`.
- **`sets/modern/` — Combined Arms.** A modern & WW2 adaptation focused on commanders: 7
  generals reprising real figures — **WW2:** Rommel, Patton, Montgomery, Zhukov; **Modern:**
  Schwarzkopf, Petraeus, Giáp — each with three signature Doctrine cards, over a shared
  14-card Doctrine deck. Read `sets/modern/COMBINED-ARMS.md`.
- **`sets/western/` — High Noon.** A Wild West adaptation (the box already ships a sheriff's
  star!): 6 Hands (Cowpoke, Sharpshooter, Dynamiter, Cannoneer, Gunslinger, Sawbones), 4 Bosses
  reprising legends (Wyatt Earp, Bass Reeves, Jesse James, Billy the Kid), 4 Objects, 10
  Gambits, and a co-op boss (The Grizzly King). Read `sets/western/HIGH-NOON.md`.
- **`sets/mageknight/` — Magestone.** A Mage Knight homage (fantasy + magic, **no combat
  dial**): 6 Units (Scout, Bowmen, Battle Mage, Siege Ballista, Heavy Cavalry, Herbalist), the
  4 hero Mage Knights as generals (Tovak, Arythea, Goldyx, Norowas) with signature Spells, 4
  magical Objects, 9 Spells, and a co-op boss (Volkare). Units, heroes and the boss each list
  **`figureCandidates`** drawn from **Mage Knight: Resurrection** (the commonly available 31-figure
  set; collector numbers & rarities accurate) — so you can field roles from minis you own via
  `tools/match-collection.py`. Read `sets/mageknight/MAGE-KNIGHT.md`.

## Fielding roles from a collection (schema v1.2)

Little Soldier and General sheets may carry an optional **`figureCandidates`** list — physical
minis (e.g. from the Mage Knight database) that can play the role, each with faction/set/points/
`roleFit`/`verified`. List the figures you own in a collection file (see
`sets/mageknight/collection.example.json`) and run:

```bash
python3 tools/match-collection.py sets/mageknight/collection.example.json
```

It reports, per role, whether it is fieldable and exactly which of your figures to use.

## Quick start

```bash
# validate every example
python3 tools/validate.py

# validate your own sheet
python3 tools/validate.py path/to/my-soldier.json

# design a card: open templates/card-template.html in a browser, type into it, Ctrl/Cmd-P
```

To invent a new sheet, follow **FRAMEWORK.md §7**. Copy the closest example as a starting
point (`medic.json` for a unit, `tactic-trigger-happy.json` for a card, etc.).

## Status: complete

All three rulebooks were read, including the **Modules book (Book 2)** and its six modules —
Super Soldiers, Levels, Objects, Reinforcements, 2 vs 2, and Advanced Tactics. The framework,
schema, examples, and template all reflect confirmed rules.

A couple of values genuinely live only on the **physical components** (not in any rulebook)
and are flagged `card-scan` / "verify from the box":

- **Grenadier** and **Operator** Defense — the rulebooks only show those two cards as
  thumbnails; their Defense badge isn't legible. (Infantry 2 and Sniper 3 are confirmed.)
- **Threat** Super Special Ability text and exact Def/Tough — printed on the box sides.

### One thing worth remembering about Book 2

The Modules PDF first arrived **mojibake-corrupted** — decoded as UTF-8 with
`errors='replace'`, which permanently collapses every byte ≥ 0x80 (≈ half of a binary PDF)
into the `�` replacement character. Such a file is unrecoverable (≈45–54% `�`, zero JPEG/zlib
markers, renders blank everywhere). If it ever needs re-supplying through a binary-mangling
transfer path, send it as **base64** (pure ASCII, survives intact):

```bash
base64 Little-Soldiers_Book-2-Modules_EN_Light.pdf > book2.b64
```

A healthy copy is ~14–17 MB, full of JPEG `ff d8` and zlib `78 9c` markers, with essentially
no `�`. (In the end a clean PDF was supplied directly and integrated.)

## Confidence tags

`FRAMEWORK.md` and each example carry one: **confirmed** (seen in a rulebook), **inferred**
(deduced from cross-references), **card-scan** (needs a physical component), **homebrew**
(original to this system).

## Copyright & attribution

**Little Soldiers** is a game published by **IELLO** and is © IELLO — *Little Soldiers*, its
rules, artwork, component names and all related trademarks are the property of IELLO
(9, avenue des Érables, lot 341, 54180 Heillecourt, France — iellogames.com). Game designed by
Adrien Fenouillet and Florent Baudry, from an original idea by Cédric Barbé.

This `sheet-system/` is an **unofficial, fan-made toolkit**. It is **not** produced, endorsed,
licensed, or affiliated by/with IELLO. It reproduces no rulebook text, artwork, or components;
it only describes game mechanics for interoperability and personal, non-commercial use. Please
support the official game — buy *Little Soldiers* from IELLO. If you are a rights holder and
have any concern about this material, it will be amended or removed on request.

The themed sets under `sets/` are original homebrew adaptations. Names they reference for
flavour or figure-matching are the property of their respective owners and are used only for
identification and compatibility:

- **Mage Knight** and the figure names in `sets/mageknight/` (including the *Resurrection* set)
  are trademarks/property of **WizKids / NECA**. Figure data is referenced from the community
  database [minisgallery.com](https://www.minisgallery.com/index.php?id=mage-knight-resurrection)
  for the sole purpose of helping owners identify which of their own minis can stand in for a
  role. This project is not affiliated with or endorsed by WizKids.
- Historical figures named in `sets/medieval/`, `sets/modern/` and `sets/western/` are used for
  inspiration/flavour only.

No copyright is claimed over any third party's marks. The original framework code, schema,
tooling and homebrew content in this directory are provided as-is for personal use.
