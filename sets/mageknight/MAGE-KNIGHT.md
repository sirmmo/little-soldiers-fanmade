# Little Soldiers: **Magestone** — a Mage Knight adaptation

A fantasy-with-magic adaptation that brings the world of **Mage Knight** (WizKids) into the
Little Soldiers system, built on the Sheet Design Framework (`../../FRAMEWORK.md`) and validated
against the same `soldier-sheet.schema.json`.

> **On the source data.** This set is inspired by the Mage Knight universe — its factions,
> unit types, hero "Mage Knights", spells and mana. The dial-stats site
> (mageknight.net/dial-stats) loads its figures via JavaScript and exposes only the standard
> WordPress API, so its numbers could not be pulled in directly; and per the brief, the
> **combat dial is deliberately not modeled** — each figure becomes a normal single-profile
> Little Soldiers sheet. Stats here are scaled to the Little Soldiers curve (Armor 2–3, Life
> 3–6); paste exact figure numbers onto any sheet if you want them.

Everything is **homebrew**. The mechanical chassis is unchanged from the base game — only the
skin (magic, mana, spells, war machines) and the roster change.

---

## 1. Terminology reskin (rules are identical)

These map onto real Mage Knight vocabulary (Wounds, Armor, mana, spells):

| Base game | Magestone |
|-----------|-----------|
| Little Soldier | **Unit** |
| General | **Mage Knight** (a hero) |
| Play Zone | **the Battlefield** |
| HQ | **Camp** |
| Order token | **Command token** |
| Heart ♥ (damage) | **Wound** |
| Toughness | **Life** |
| Defense 🛡 | **Armor** |
| Shield / Scout token (−defense) | **Hex token** (a curse that weakens armor) |
| Flag / Battle Track | **Banner** on the **Conquest track** |
| Star token (first player) | **Initiative crystal** |
| Levels module | **High Ground** |
| Grenade die | **Fireball die** |
| Mortar token / catapult | **Siege engine / Boulder** |
| Sniper die | **Bolt die** (crossbow) |
| Crate (Advanced Tactics) | **Mana Crystal cache** |
| Tactics card | **Spell** (Spell / Tactic) |

---

## 2. The roster (Units) — `soldiers/`

The six map onto real Mage Knight unit types; the first four reuse the base archetypes'
mechanics, the last two are new builds. Units serve any Mage Knight, so `color` is `any`.

| Unit | Armor | Life | Special Action | Super-rank Ability (per ⚡) | Maps to |
|------|:-----:|:----:|----------------|-----------------------------|---------|
| **Scout** | 2 | 5 | **Reconnoiter** — Hex up to 2 foes (no valid target) | Make 1 Move after the Attack | Infantry |
| **Bowmen** | 3 | 3 | **Aimed Bolt** — Attack adding the Bolt die (recoil can Wound you) | Hex the target after the Attack | Sniper |
| **Battle Mage** | 2 | 6 | **Fireball** — flick the Fireball die; AoE; a backfire Wounds you | Apply the hits to another valid target | Grenadier |
| **Siege Ballista** | 2 | 5 | **Bombardment** — the siege engine; AoE to friend and foe | Move 1 Wound from one Unit to any other | Operator |
| **Heavy Cavalry** ⚔ *(new)* | 3 | 4 | **Cavalry Charge** — straight Move, then an Attack with +1 reroll | Make 1 Move after the Attack | — |
| **Herbalist** ✚ *(new)* | 2 | 4 | **Healing Herbs** — remove up to 2 Wounds split between self and an ally in yellow range | Remove 1 extra Wound from an ally | — |

### 2.1 Figure candidates — field roles from the Resurrection set

Each sheet carries a **`figureCandidates`** list (schema v1.2) pointing at figures from
**Mage Knight: Resurrection** — the commonly available 31-figure relaunch
([minisgallery.com](https://www.minisgallery.com/index.php?id=mage-knight-resurrection)).
Collector numbers and rarities are accurate (`verified: true`); **role assignment is editorial**
(the set lists figures by rarity, not battlefield role, so roles are inferred from names).

| Role | Resurrection figures (collector # · rarity) |
|------|----------------------------------------------|
| **Scout** | Attem Sentinel (5·C) · Skeleton Skullwalker (3·C) · Zombie Shambler (7·C) · Goblin Pillager (6·C) · Gassalite Swordbrother (8·C) |
| **Bowmen** | Xandressan Windsman (4·C) · Skyguard Captain (16·U) · Technoshocker (18·U) |
| **Battle Mage** | Bonebreaker Shaman (11·C) · Solonavi Domineer (19·U) · Technoshocker (18·U) · Exarch Balion (23·R) |
| **Siege Ballista** | Technoshocker (18·U) · Skyguard Captain (16·U) — *no war-machine sculpt in the set; proxy or use a heavy ranged figure* |
| **Heavy Cavalry** | Moonborn Dunewolf (1·C) · Wolfkin Raider (9·C) · Dwarven Axeshield (2·C) · Orc Harrower (17·U) · Cavalier Freeblade (102·Uq) · Growlfang (103·Uq) · Harrowblade (105·Uq) |
| **Herbalist** | Bonebreaker Shaman (11·C) · Solonavi Domineer (19·U) — *prefer a figure with the Healer ability* |
| **Heroes (generals)** | Tovak (15·U) · Arythea (13·U) · Goldyx (14·U) · Norowas (12·U) · Wolfhawk (20·R) |
| **Boss (Volkare)** | General Volkare (21·R) · Za'Rax'As (101·Uq) · General Marz (104·Uq) |

**Pick from what you own:** list your shelf in a collection file (see
`collection.example.json`) and run the matcher:

```bash
python3 tools/match-collection.py sets/mageknight/collection.example.json \
    sets/mageknight/soldiers sets/mageknight/generals sets/mageknight/threats
```

It prints, per role, whether it is **fieldable** and exactly which of your figures to use.

---

## 3. Objects (magical sites) — `objects/`

| Object | Effect | Maps to |
|--------|--------|---------|
| **Magic Portal** | Travel to any other Magic Portal in play (ends the Move) | Teleporter |
| **Mage Tower** | Two-sided. While its ward is raised, a magical haze fouls every Attack: −1 reroll | Switch |
| **Scrying Pool** | Hex up to 2 enemies anywhere on the Battlefield | Radar |
| **Magical Glade** | Remove up to 2 Wounds from the Unit that reaches it | (Object → self-heal) |

---

## 4. The heroes (Mage Knights) — `generals/`

Four heroes reprising the iconic Mage Knights, each tied to a mana colour and a play style,
with three signature Spells.

| Mage Knight | Mana | Style | Signature Spells |
|-------------|------|-------|------------------|
| **Tovak** | Blue (ice) | Cold, calculating, precise | **Ice Bolt** · Concentration · Mana Surge |
| **Arythea** | Red (fire) | Aggressive blood-and-fire fury | **Blood Rage** · Fireball · Swiftness |
| **Goldyx** | Green (nature) | Versatile, resourceful, restorative | **Crystal Mastery** · Swiftness · Battle Cry |
| **Norowas** | White (light) | Inspiring leader of allies | **Bonds of Loyalty** · Battle Cry · Concentration |

## 5. The Spell & Tactic deck — `tactics/`

Shared Spells plus each hero's signature:

| Spell | Type | Cond. | Effect |
|-------|------|:----:|--------|
| **Fireball** | General | 3 | 1 Attack on any enemy, ignoring line of sight, +1 reroll |
| **Mana Surge** | General | 2 | Gain Bonus Command tokens (cleared at end of Round) |
| **Swiftness** | Soldier | 2 | The chosen Unit makes 3 Moves |
| **Battle Cry** | General | 1 | Up to 3 allied Units each make 1 Move |
| **Concentration** | Reaction | — | Before resolving your Attack, gain +1 reroll |
| **Ice Bolt** | Soldier | 2 | Hex a valid target, then Attack it with +1 reroll *(Tovak)* |
| **Blood Rage** | Soldier | 3 | Make 2 Attacks, then take 1 Wound *(Arythea)* |
| **Crystal Mastery** | General | 1 | Draw 2 Spells from the deck *(Goldyx)* |
| **Bonds of Loyalty** | General | 3 | Up to 3 different allied Units each make 1 Attack *(Norowas)* |

---

## 6. The co-op boss — `threats/`

**Volkare** — the great warlord, the iconic Mage Knight antagonist (Armor 5 / Life 8). His army
shields him until both flanking banners fall (Switches 1 **and** 2); on 3+ ⚡ in the collective
attack he calls a **Volley from the Host**. See `threats/volkare.json`.

---

## 7. Use it

```bash
# from sheet-system/ — validate the whole Mage Knight set
python3 tools/validate.py $(find sets/mageknight -name '*.json')
```
