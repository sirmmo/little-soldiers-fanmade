# Little Soldiers — Sheet Design Framework

A generalization of the *Little Soldiers* rules (IELLO, by Adrien Fenouillet & Florent
Baudry) into a reusable system for designing **new sheets** — Little Soldiers, Generals,
Threats, Tactics cards, and Objects — that stay mechanically consistent with the published
game.

This is the human-readable spec. Its companions:

- `schema/soldier-sheet.schema.json` — the same model as a machine-readable JSON Schema.
- `examples/` — every base unit re-expressed in the schema, plus new worked examples.
- `tools/validate.py` — validates example sheets against the schema.
- `templates/card-template.html` — a print-ready, fill-in-the-blanks card.

## Source provenance

All three rulebooks were read: **Book 1 — Bootcamp** (core rules, card anatomy, the 4 base
units), **Book 2 — Modules** (the 6 modules: Super Soldiers, Levels, Objects, Reinforcements,
2v2, Advanced Tactics), and **Book 3 — Missions** (co-op Threats + the token glossary).

> Book 2 first arrived mojibake-corrupted (every byte ≥ 0x80 collapsed to `�`) and was
> recovered only after being re-supplied as a clean copy. See `README.md` for the
> base64-transport note if it ever needs re-delivering.

Confidence tags: **[confirmed]** seen directly in a rulebook · **[inferred]** deduced from
cross-references · **[card-scan]** needs the physical punchboard card (not legible in the
books) · **[homebrew]** original to this framework.

---

## 1. The sheet taxonomy

Everything with stats-and-an-action, or a printed effect, is one of five sheet kinds. The
first three are the originals; **Tactics cards** and **Objects** come from the Modules book.

| Sheet | Role | Driven by | Distinctive parts |
|-------|------|-----------|-------------------|
| **Little Soldier** | A unit in your squad | A player | Defense, Toughness, 3 actions, two rank sides, a figurine |
| **General** | Your HQ / order engine | A player | "Giving an Order" + (with Advanced Tactics) 3 signature Tactics cards |
| **Threat** | Co-op boss/enemy | The game | Defense, Toughness, auto-Attack, Force Field, Target point, Super Special |
| **Tactics card** | A one-shot rule-breaker | A player | Order-token *condition*, a type (General/Soldier/Reaction), an effect |
| **Object** | An activatable scenery power | A player on contact | A name and an effect triggered at the end of a Move |

A sheet is **data + a tiny rules grammar**. Designing one = filling slots with values drawn
from a constrained vocabulary (Sections 5–6) so the result reads and balances like the
originals (Section 7).

---

## 2. Little Soldier — anatomy

A Little Soldier card is **double-sided**: the front is the **New Recruit** rank; the back is
the **Super Soldiers** rank (same unit, abilities unlocked). [confirmed, Book 1 p4 + Book 2 p3]

```
 ┌─────────────────────────────────────────┐
 │ [Def] [Tough]        (Rank ^)   (Type)   │   ← top band
 │  🛡2    ♥5                                 │
 │            ART / FIGURINE AREA            │
 │  ╔═══════════╗                            │
 │  ║   NAME    ║                            │   ← name banner
 │  ╚═══════════╝                            │
 │ [ATTACK] [MOVE] [ SPECIAL ACTION: NAME ] │   ← actions band
 └─────────────────────────────────────────┘
```

| Slot | Meaning |
|------|---------|
| **Name / Type / Rank** | Title; "Little Soldier" type icon; chevron `^` = New Recruit (front), `^^` = Super Soldiers (back) |
| **Defense** 🛡 | A wound lands only when `hits > Defense`. Each Shield/Scout token = −1, floor 0. |
| **Toughness** ♥ | Breaks when Hearts on the card ≥ Toughness. |
| **Figurine** | The plastic miniature; its physical footprint is the in-play token. |
| **Actions** | Attack, Move, and one named **Special Action**. |
| **Super Soldiers side** | Adds a per-⚡ **Special Ability** + a universal **Move heal** (Section 5.5). |
| **Figure candidates** *(optional)* | A list of physical minis from a collection (e.g. the Mage Knight database) that can stand in for this role — so players can field it from what they own. See Section 8. |

### Figure candidates — playing roles from a collection (schema v1.2)

Any Little Soldier (or General) sheet may carry an optional **`figureCandidates`** list: real
miniatures that suit the role, each with `name`, `faction`, `set`, optional `points` /
`collectorNumber` / `dbUrl`, a `roleFit` note, and a `verified` flag (true once confirmed
against the source database). This lets you map an abstract role onto concrete minis you own.
`tools/match-collection.py` takes a collection file and reports which roles you can field and
exactly which figures to use. The `sets/mageknight/` roster is populated with Mage Knight
figure candidates as the worked example.

### The four base units [confirmed]

| Unit | Def | Tough | Special Action | Super Soldiers — Special Ability (per ⚡) |
|------|-----|-------|----------------|-------------------------------------------|
| **Infantry** | 2 | 5 | **Scout** — place up to 2 Scout tokens on opponents (−def), no valid target | **Make 1 Move after this Attack** |
<!-- Infantry row also verified against physical-card photos of the Italian edition (FANTERIA), both rank sides, in `originals/`. -->
| **Sniper** | 3 | 3 | **Risky Shot** — Attack adding the Sniper die (⊕ adds hits; Boom adds ♥ to self) | **Place 1 Shield on the target after this Attack** (lowers its defense) |
| **Grenadier** | *[card-scan]* | 6 | **Throw a Grenade** — flick the Grenade die; AoE in yellow range to all; Boom = 7 to self | **Apply this Attack's hits to another valid target** (multi-target) |
| **Operator** | *[card-scan]* | 5 | **Mortar Shot** — catapult; AoE to allies + enemies; ♥ = mortar token face | **Transfer 1 ♥ from one Little Soldier to any other in play** (incl. opponents) |

Plus the universal Super Soldiers **Move heal**: *for each Move a Little Soldier makes, you may
remove 1 ♥ from its card.* Grenadier/Operator Defense aren't legible in the books (the cards
appear only as thumbnails) — read them off the physical punchboard.

---

## 3. General — anatomy

The General is your order engine, not a fighter: **no figurine, no Defense/Toughness, cannot
be attacked.** [confirmed]

| Slot | Meaning |
|------|---------|
| **Name / Color** | Flavor identity (Brick, Sun, Apple, Dinosaur…) + squad color (Green/Yellow) |
| **Order action** | Base game — *"Play 1 Order token on one of your Little Soldiers currently in play."* |
| **Signature Tactics** | With the *Advanced Tactics* module, each General owns **3 signature Tactics cards** printed on its back, marked with the General's icon | [confirmed]

> **Asymmetry lives in the Tactics deck, not the order text.** Base-game Generals are
> mechanically identical; the *Advanced Tactics* module differentiates them purely through
> their 3 starting cards (e.g. Dinosaur starts with Trigger Happy, Strategic Retreat,
> Camouflage). To design an asymmetric General, pick its 3 signature cards (Section 4.1).

---

## 4. Threat — anatomy

Co-op enemies (Book 3). A Threat has no player; it acts on rails during the **Threats' turn**.

| Slot | Meaning |
|------|---------|
| **Name / Def / Tough** | As a Little Soldier |
| **Target ⊙** | The single point on the art used for line-of-sight *and* range to the Threat |
| **Attack** | Auto-run every Threats' turn: a *"place X on valid targets / Y on all Little Soldiers"* template; **+1 ♥ to each valid target per ⚡ rolled** |
| **Super Special Ability** | Fires when the collective Threat attack rolls **3+ ⚡** (the only place a 3+⚡ tier exists — Little Soldiers don't have one) |
| **Force Field #n** | Damage immunity until the matching numbered Switch is flipped off; multi-part Threats can need several switches (Octocutie's head = both tentacle switches) |

### 4.1 Tactics card — anatomy [confirmed, Book 2 p12–15]

A one-shot effect from the *Advanced Tactics* module (must be combined with *Super Soldiers*).

| Slot | Meaning |
|------|---------|
| **Name** | e.g. Trigger Happy, Camouflage |
| **Type** | **General** card · **Soldier** card · **Reaction** (played on an opponent's turn at the moment its text names) |
| **Order condition** | A number in the top-left = how many Order tokens the General/Soldier must *have* to play it. **Not a cost — not spent**; just a gate. (Some cards, e.g. Fighting Fit, have none.) |
| **Owner icon** | Bottom-right icon tying a signature card to its General |
| **Effect** | Read aloud; **the card overrides the normal rules**. |

Card-play rules to respect when designing: up to **3 cards per turn**; at most **3 played
cards** kept face-up in HQ; played cards are discarded at end of your turn; Reactions count
toward the limit and linger until the end of your *next* turn. Confirmed cards:
*Fighting Fit* (1 Move, no condition), *Marathon Man* (3 Moves, ≥2), *Trigger Happy* (up to 3
Attacks on different targets, ≥2), *Warmonger* (2 Attacks, ≥3), *Strategic Retreat* (up to 3
allies make 1 Move), *Camouflage* (Reaction: attacker rolls −1 die), *Laser Targeting*
(Reaction: +1 reroll), *Chewed by the Dog* (Reaction: cancel 1 Move), *Unexpected Ally*
(place 1 token on every Little Soldier in play), *General's Orders* (grants Bonus Order
tokens — like Order tokens but cleared at end of Round).

### 4.2 Object — anatomy [confirmed, Book 2 p8–10]

A power attached to scenery (*Objects* module). Activated when **your** Little Soldier ends a
Move in contact with it and **no opponent** is also touching it.

| Object | Effect |
|--------|--------|
| **Teleporter** | Place your figurine in contact with any other Teleporter in play (ends the Move). A Grenade/Mortar touching a Teleporter can be teleported before exploding. |
| **Transmogrifier** | Swap the positions of any 2 Little Soldiers in play (with their tokens), any owner. |
| **Radar** | Place up to 2 Scout tokens on opponents anywhere (like Infantry's Scout). |
| **Marshmallow** | Make a straight-line Move as far as the fully-stretched cord allows, over objects/scenery; may end on a higher Level. |
| **Switch** | Flip its token. *"Who turned out the light?"* — for each Switch showing its dark side, **all players have 1 fewer reroll when Attacking**. |

---

## 5. The shared vocabulary (the "grammar")

### 5.1 Stats

| Stat | Range | Rule |
|------|-------|------|
| **Defense** | 2–3 (units), up to ~5 (Threats) | Wound only when `hits > Defense`; −1 per Shield/Scout token, floor 0 |
| **Toughness** | 3–6 (units) | Breaks when Hearts ≥ Toughness |

### 5.2 Range & measurement (cords)

No grid — distance is physical. **Green** (shortest, = 1 Move token; deployment & chains),
**Yellow** (medium; standard Move, grenade AoE), **Red** (long; grants the extra attack
reroll). Standard Attack has **no max range** — only **line of sight** (target's whole head
visible). Range checks ignore scenery ("as the crow flies").

### 5.3 The action grammar

An Order buys exactly **one** action on one Little Soldier:

1. **Attack** — ① declare a valid target → ② roll 5 Attack dice, reroll once; **+1 reroll in
   red range**; **+1 reroll attacking from a higher Level** (Levels module) → ③
   `wounds = max(0, hits − Defense)`, place that many Hearts. With *Super Soldiers*, each **⚡**
   also fires the unit's Special Ability once.
2. **Move** — lay the yellow cord, bend freely, place anywhere along it. With *Super
   Soldiers*, each Move may also remove 1 ♥ from the moving unit.
3. **Special Action** — the unit's named signature (the New-Recruit design surface).

### 5.4 Effect primitives

Compose Special Actions, Abilities, Tactics cards, and Object powers from these
(`effect.kind` in the schema). Confirmed across all three books:

| Primitive | What it does | Seen on |
|-----------|--------------|---------|
| `place_tokens` | Put N tokens on chosen figurines | Infantry Scout, Sniper SS, Radar, Unexpected Ally |
| `transfer_token` | Move a token from one card to another | Operator SS |
| `augment_attack` | Make an Attack with an extra die added | Sniper Risky Shot |
| `dice_launch` / `catapult_launch` | Physically flick a die / catapult; AoE by landing | Grenadier, Operator |
| `area_effect` | Affect *all* figurines in range, no valid target | Grenadier, Operator, Mortar |
| `multi_target` | Apply an Attack's results to additional valid target(s) | Grenadier SS, Trigger Happy |
| `extra_attacks` | Make N Attacks this action | Warmonger, Trigger Happy |
| `extra_move` | Chain Move(s) onto another action | Infantry SS, Marathon Man, Strategic Retreat, Fighting Fit |
| `straight_line_move` | Forced full-length straight Move | Marshmallow |
| `swap_positions` | Swap two figurines' positions | Transmogrifier |
| `teleport` | Relocate to another like Object | Teleporter |
| `self_heal` | Remove ♥ from a unit | Super Soldiers Move heal, Operator SS |
| `self_risk` | A die face that damages the actor (Boom!) | Sniper, Grenadier |
| `ignore_los` | Skip the valid-target requirement | Grenadier, Operator |
| `modify_rerolls` | Grant/remove rerolls or attack dice | Levels height (+1), Switch (−1), Laser Targeting (+1), Camouflage (−1 die) |
| `cancel_action` | Cancel an opponent's Move/action | Chewed by the Dog |
| `draw_cards` | Draw Tactics cards | Crate activation |
| `grant_order` | Add Order / Bonus Order tokens | General's Orders, Reinforcements setup |
| `custom` | Anything else (requires `text`) | — |

Parameters: **count**, **token/die type**, **range**, **targets** (enemies/allies/all/self),
**needsValidTarget**, and **trigger** (for Reactions/Abilities).

### 5.5 Ranks & abilities — the Super Soldiers side [confirmed, Book 2 p3]

Flip every Little Soldier card to its **Super Soldiers** side (the *Super Soldiers* module, or
in *Battle Royale* on reaching Supplies). Then:

- **⚡ Lightning is unlocked** during *Resolve the Attack*.
- **Special Ability** = the unit's per-⚡ ATTACK ability, activated **once per ⚡ rolled**
  (linear — 3 ⚡ = 3 activations; too few for one = nothing). This is the per-unit row in the
  Section 2 table.
- **Move heal** (universal) = each Move a Super Soldier makes may remove 1 ♥ from its card.

> Correction vs. an earlier guess: Little Soldiers have **no separate "3+⚡ Super Special."**
> That tier exists **only on Threats** (Section 4). A Little Soldier's power simply scales
> linearly with ⚡.

### 5.6 Token & symbol vocabulary [confirmed, Book 3 p16]

- **Combat/state:** Heart ♥, Shield (−def), Hit, Lightning ⚡, Boom!, Ouch, Target ⊙.
- **Economy/flow:** Order, Bonus Order, Star (first player), Flag counter, Numbered Block,
  Deployment, Move token.
- **Dice:** Attack ×5, Grenade, Sniper; Mortar token.
- **Module:** Level 1/2, Candy, Crate, Supplies, Switch; Object tokens — Teleporter, Radar,
  Transmogrifier, Marshmallow; Tactics card; Reaction.

### 5.7 Dice faces (design budget)

- **Attack die:** Hit · ⚡ Lightning (ability trigger) · blank. 5 dice, one guaranteed reroll.
- **Sniper die:** ⊕ faces add hits; Boom faces add **+2 / +1 ♥ to the sniper**; never modified.
- **Grenade die:** **3 / 5 / 7**, plus **Boom!** (7 to the thrower).
- **Mortar token:** two faces of differing ♥ to everything in range.

---

## 6. Balance heuristics

1. **Defense + Toughness is a budget.** Cannon (Sniper 3/3) vs tank (Grenadier ?/6); stay on
   that curve — never pair top Defense *and* top Toughness without a weak action.
2. **No-LoS power costs self-risk.** Anything that ignores valid target also hits your own
   side and/or carries a Boom! face.
3. **Rerolls are the damage dial.** Base 2 → red range 3 → higher Level +1. Effects that grant
   rerolls (Laser Targeting) or strip them (Switch, Camouflage) are strong — meter them.
4. **Super Soldier abilities scale with ⚡.** Per-⚡ linear, so an ability's *per-activation*
   value must be small (one Move, one Shield, one ♥) — the ceiling is the dice, not the text.
5. **Free value wants a string.** Scout is free but does no damage; the universal Move heal is
   free but costs your Move. Price new "free" effects in tempo.
6. **Tactics cards override rules — gate them.** Use the Order-token *condition* (not a cost)
   to gate strong cards behind a loaded General/Soldier; respect the 3-per-turn / 3-in-play
   limits; Reactions are premium (they act on the enemy's turn).
7. **Threats scale by breadth.** More targets per attack, more Force Fields/switches, or
   multi-part bodies before inflating Def/Tough; reserve the 3+⚡ Super Special for the spike.

---

## 7. How to design a new sheet (step by step)

**A Little Soldier:** ① pick one verb the unit is *for* → ② place it on the stat curve
(strong action ⇒ fragile body) → ③ write the **Special Action** from primitives (5.4) → ④
**pay for power** (friendly fire / Boom / lower stats) → ⑤ give the **Super Soldiers** side a
small **per-⚡ Special Ability** (the Move heal is automatic) → ⑥ encode as JSON and run
`tools/validate.py` → ⑦ lay out with `templates/card-template.html`.

**A Tactics card:** name it, pick **type** (General/Soldier/Reaction), set the **Order
condition** to gate its strength, write an effect from primitives, and decide if it's a
General's signature card.

**A General:** standard order text + choose its **3 signature Tactics cards** for the
asymmetry.

### Worked example — "MEDIC" (Def 2 / Tough 4)

- **Special Action — Field Dressing:** *Remove up to 2 ♥ split between this unit and one ally
  within yellow range. No valid target.* (`self_heal` + `place_tokens(heal, allies)`.)
- **Stat logic:** low Def/Tough — pure recovery, which is strong (heuristic 5).
- **Super Soldiers — Special Ability (per ⚡):** remove 1 extra ♥ from an ally in range.
  (Plus the universal Move heal.) — now grounded in the real per-⚡ model, *not* a 3+⚡ tier.

See `examples/medic.json`, `examples/tactic-trigger-happy.json`, and
`examples/object-teleporter.json` for encoded sheets across the new types.
