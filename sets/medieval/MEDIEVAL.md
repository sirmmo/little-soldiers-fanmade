# Little Soldiers: **Realms at War** — a Medieval adaptation

A medieval reskin and content expansion of *Little Soldiers*, built on the Sheet Design
Framework (`../../FRAMEWORK.md`). Every sheet here validates against the same
`soldier-sheet.schema.json` — this set is proof that the generalization is reusable.

> **The conceit.** The plastic toys are now a tabletop of painted lead knights. Two great
> houses — **House Stag** (green) and **House Wolf** (yellow) — fight for the great hall.
> The rules are unchanged; only the *names* change, plus six new units, four objects, five
> Tactics cards, and a co-op boss. Houses, names, and art are yours to rename.

Confidence: everything here is **homebrew** (original content), stat-balanced against the base
game's curve (Defense 2–3, Toughness 3–6). Treat the spicier units (Knight, Cleric) as
playtest material.

---

## 1. Terminology reskin (rules are identical)

Pure renames — no rule changes. Read the Bootcamp rules with this glossary.

| Base game | Realms at War |
|-----------|---------------|
| Little Soldier | **Warrior** |
| General | **Lord / Lady** (the house's commander) |
| Play Zone / playroom | **The Field** |
| HQ | **Camp** |
| Order token | **Command token** |
| Heart ♥ (damage) | **Wound** |
| Toughness | **Vigour** |
| Defense 🛡 | **Armour** |
| Shield / Scout token (−defense) | **Exposed token** (chinks in the armour) |
| Flag counter / Battle Track | **Banner** on the **War Track** |
| Star token (first player) | **Crown token** |
| Level 1/2 (Levels module) | **The Keep** — Level 1 = rampart, Level 2 = tower |
| Grenade die | **Firepot die** |
| Mortar token / catapult spoon | **Boulder token / the Trebuchet** |
| Sniper die | **Longbow die** |
| Crate (Advanced Tactics) | **Supply Wagon** |
| Tactics card | **Stratagem** |

So "place an Exposed token to reduce Armour", "roll the Firepot die", and "the Banner reaches
your Victory zone" all map 1:1 onto the printed rules.

---

## 2. The roster (Warriors)

Six unit sheets in `soldiers/`. The first four are medieval counterparts of the base archetypes
(same chassis, reskinned); the last two are new builds that show off the framework's primitives.
Warriors are house-agnostic (both houses field them), so their `color` is `any`.

| Warrior | Armour | Vigour | Special Action | Super-rank Ability (per ⚡) | Maps to |
|---------|:------:|:------:|----------------|-----------------------------|---------|
| **Man-at-Arms** | 2 | 5 | **Scout the Field** — place up to 2 Exposed tokens on foes (no valid target) | Make 1 Move after the Attack | Infantry |
| **Longbowman** | 3 | 3 | **Longbow Volley** — Attack adding the Longbow die (⊕ adds hits; a snapped string Wounds you) | Place 1 Exposed token on the target | Sniper |
| **Bombard** | 2 | 6 | **Hurl Firepot** — flick the Firepot die; AoE in yellow range to all; a misthrow bursts on you (7) | Apply the Attack's hits to another valid target | Grenadier |
| **Siege Engineer** | 2 | 5 | **Trebuchet** — launch a Boulder with the Trebuchet; AoE to friend and foe | Move 1 Wound from one Warrior to any other (redirect the rubble) | Operator |
| **Knight** ⚔ *(new)* | 3 | 4 | **Lance Charge** — a straight-line Move, then one Attack with +1 reroll | Make 1 Move after the Attack (ride down) | — |
| **Cleric** ✚ *(new)* | 2 | 4 | **Lay On Hands** — remove up to 2 Wounds split between self and one ally in yellow range | Remove 1 extra Wound from an ally in range | — |

Design notes (per `FRAMEWORK.md` §6):

- **Knight** trades Vigour (4) for its strong combined charge — well-armoured but over-committed.
  Keep an eye on it in play; if the charge feels too strong, drop the +1 reroll.
- **Cleric** is fragile (2/4) and unarmed of offense — pure tempo recovery, which is powerful.
- All four reskins keep their originals' exact stats and ability shapes, so they're
  tournament-equivalent to the base box.

---

## 3. Objects (`objects/`)

Medieval Objects for the Objects module. Activate when **your** Warrior ends a Move in contact
and no enemy is also touching it.

| Object | Effect | Maps to |
|--------|--------|---------|
| **Secret Tunnel** | Travel to any other Secret Tunnel in play (ends the Move) | Teleporter |
| **Portcullis** | Two-sided. While **shut**, sightlines through the gate are blocked: every Attack has **−1 reroll** | Switch |
| **Watchtower** | Place up to 2 Exposed tokens on enemies anywhere on the Field | Radar |
| **Sorcerer's Circle** | Swap the positions of any two Warriors in play (with their tokens) | Transmogrifier |

---

## 4. Stratagems (`tactics/`)

Five Stratagem cards for the Advanced Tactics module (which requires the Super-rank module).
The number is the **Command condition** — Command tokens the Lord/Warrior must *have*, never
spent. Each house's Lord starts with three signature Stratagems.

| Stratagem | Type | Cond. | Effect | House |
|-----------|------|:----:|--------|-------|
| **Volley Fire** | Soldier | 2 | Make up to 3 Attacks on different targets | Stag |
| **Hold the Line** | General | 1 | Up to 3 allied Warriors each make 1 Move | Stag |
| **Feint** | Reaction | — | When a foe declares a valid target, they roll −1 die | Stag |
| **Forced March** | Soldier | 2 | The chosen Warrior makes 3 Moves | Wolf |
| **Rally to the Crown** | General | 2 | Gain Bonus Command tokens (cleared at end of Round) | Wolf |

(Build more from the primitive table in `FRAMEWORK.md` §5.4 — the base game ships 50 cards.)

---

## 5. Lords & Ladies (`generals/`)

| Commander | House | Colour | Signature Stratagems |
|-----------|-------|--------|----------------------|
| **King Aldric** | Stag | green | Volley Fire · Hold the Line · Feint |
| **Queen Mara** | Wolf | yellow | Forced March · Rally to the Crown · Ambush |

Both use the standard order action — *"Play 1 Command token on one of your Warriors in play."*
Their asymmetry is entirely in the three signature Stratagems (per `FRAMEWORK.md` §3).

### 5.1 Legendary Commanders (historical)

Two commanders reprising real figures of the Third Crusade — designed as rivals, contrasting
**aggression + discipline** against **mobility + attrition**. Each comes with three signature
Stratagems (also in `tactics/`).

| Commander | Reprises | Colour | Style | Signature Stratagems |
|-----------|----------|--------|-------|----------------------|
| **Richard the Lionheart** | Richard I of England | green | Hard-hitting warrior-king; hold the line, then charge | **Charge at Arsuf** (charge: straight Move → boosted Attack) · **Lionheart's Valour** (2 Attacks, shrug off a Wound) · **Hold the Line** |
| **Saladin** | Salah ad-Din (Ayyubid) | yellow | Maneuver, encircle, exhaust | **Feigned Retreat** (Reaction: dodge a declared Attack with a Move) · **Encirclement at Hattin** (Expose up to 3 foes) · **Desert Maneuver** (3 Moves) |

Each ability is grounded in the framework's primitives and balanced against the Stratagems in
§4 — Richard pays for his offense with high Command conditions; Saladin trades raw damage for
position and armour-shredding. Drop them onto either house's Camp in place of Aldric/Mara.

---

## 6. The boss (`threats/`)

**The Old Wyrm** — a co-op Threat for the Missions style of play. Armour 5 / Vigour 8, protected
by a Force Field that needs **two** levers thrown (Switches 1 **and** 2 — topple the two
gate-towers) before it can be wounded. On 3+ ⚡ in the collective attack it unleashes an
**Inferno** (Super Special). See `threats/old-wyrm.json`.

---

## 7. Optional themed module — **Morale** (homebrew)

A light flavour module, fully optional and clearly experimental. Uses only existing components.

> **Morale.** A house is *Broken* the moment it has **no Warriors left in the Field** on its
> turn (this already ends the round via Wipeout in the base rules). *Variant:* if, at the end
> of any round, a house has had **three or more** Warriors broken this game while its opponent
> has lost one or fewer, move the Banner **one extra space** toward the steadier house — fear
> spreads through the ranks. Remove this rule if it snowballs; it is not part of the base game.

Everything else is the published rule set, reskinned.

---

## 8. Use it

```bash
# from sheet-system/ — validate the whole medieval set against the schema
python3 tools/validate.py $(find sets/medieval -name '*.json')

# print cards: open ../../templates/card-template.html and transcribe these sheets,
# or just write Realms-at-War names onto the blank cards.
```
