# Little Soldiers: **High Noon** — a Wild West adaptation

A frontier / Old-West reskin and expansion, built on the Sheet Design Framework
(`../../FRAMEWORK.md`) and validated against the same `soldier-sheet.schema.json`.

> **The conceit.** Two outfits face off for control of a dusty frontier town — the **Lawmen**
> (green) and the **Outlaws** (yellow). The base game already hands first player a **sheriff's
> star**, so the West was hiding in the box all along. This set ships a full posse roster, four
> **Bosses** reprising legendary Old-West figures, four Objects, ten Gambits, and a co-op boss.

Everything is **homebrew**, stat-balanced against the base curve (Cover 2–3, Sand 3–6). The
spicier picks (Gunslinger, Sawbones) are playtest material.

---

## 1. Terminology reskin (rules are identical)

| Base game | High Noon |
|-----------|-----------|
| Little Soldier | **Hand** (a gun-hand in your outfit) |
| General | **Boss** |
| Play Zone | **the Territory** |
| HQ | **Hideout** |
| Order token | **Grit token** (the Boss's say-so) |
| Heart ♥ (damage) | **Lead** ("full of lead") |
| Toughness | **Sand** (frontier slang for guts) |
| Defense 🛡 | **Cover** (barrels, batwing doors) |
| Shield / Scout token (−defense) | **Drop token** ("got the drop on 'em") |
| Flag / Battle Track | **Town marker** on **Main Street** |
| Star token (first player) | **Fastest Gun token** |
| Levels module | **High Ground** (rooftops, the bell tower) |
| Grenade die | **Dynamite die** |
| Mortar token / catapult | **Blast token / the old Army Cannon** |
| Sniper die | **Rifle die** (a Sharps buffalo rifle) |
| Crate (Advanced Tactics) | **Strongbox** |
| Tactics card | **Gambit** (a card up your sleeve) |

---

## 2. The roster (Hands) — `soldiers/`

The first four reskin the base archetypes (identical stats/abilities); the last two are new.
Hands serve either outfit, so `color` is `any`.

| Hand | Cover | Sand | Special Action | Super-rank Ability (per ⚡) | Maps to |
|------|:-----:|:----:|----------------|-----------------------------|---------|
| **Cowpoke** | 2 | 5 | **Get the Drop** — Drop up to 2 foes (no valid target) | Make 1 Move after the Attack | Infantry |
| **Sharpshooter** | 3 | 3 | **Buffalo Rifle** — Attack adding the Rifle die (a kick can Lead you) | Drop the target after the Attack | Sniper |
| **Dynamiter** | 2 | 6 | **Light the Fuse** — flick the Dynamite die; AoE; a dud blows up on you | Apply the hits to another valid target | Grenadier |
| **Cannoneer** | 2 | 5 | **Roll Out the Cannon** — the old Army Cannon; AoE to friend and foe | Move 1 Lead from one Hand to any other | Operator |
| **Gunslinger** ⚔ *(new)* | 3 | 4 | **Quickdraw** — Drop a valid target, then Attack it with +1 reroll | Make 1 Move after the Attack | — |
| **Sawbones** ✚ *(new)* | 2 | 4 | **Patch 'Em Up** — remove up to 2 Lead split between self and an ally in yellow range | Remove 1 extra Lead from an ally | — |

---

## 3. Objects — `objects/`

| Object | Effect | Maps to |
|--------|--------|---------|
| **Mineshaft** | Travel to any other Mineshaft in play (ends the Move) | Teleporter |
| **Saloon Doors** | Two-sided. While shut, sightlines are blocked: every Attack has −1 reroll | Switch |
| **Lookout Tower** | Drop up to 2 enemies anywhere on the Territory | Radar |
| **Runaway Wagon** | Swap the positions of any two Hands in play | Transmogrifier |

---

## 4. Bosses (legendary figures) — `generals/`

Four Bosses reprising real Old-West figures, split **Lawmen vs Outlaws**, each with three
signature Gambits. (`color` shown is a suggestion; swap freely.)

| Boss | Reprises | Side | Style | Signature Gambits |
|------|----------|------|-------|-------------------|
| **Wyatt Earp** | Tombstone lawman, the O.K. Corral | Lawmen (green) | Cold, disciplined walk-down | **The Walk-Down** · Dead Eye · Rally the Posse |
| **Bass Reeves** | legendary US Deputy Marshal | Lawmen (green) | Relentless manhunter | **Always Get Your Man** · Fan the Hammer · Ride Hard |
| **Jesse James** | outlaw gang leader, train robber | Outlaws (yellow) | Raids and quick getaways | **Train Robbery** · Ride Hard · Ace in the Hole |
| **Billy the Kid** | young outlaw gunfighter | Outlaws (yellow) | Lightning-fast aggression | **Lightning Hands** · Quickdraw Duel · Fan the Hammer |

## 5. The Gambit deck — `tactics/`

Shared Gambits the Bosses draw on, plus each Boss's unique signature card:

| Gambit | Type | Cond. | Effect |
|--------|------|:----:|--------|
| **Fan the Hammer** | Soldier | 2 | Make up to 3 Attacks on different targets |
| **Dead Eye** | Reaction | — | Before resolving your Attack, gain +1 reroll |
| **Ride Hard** | Soldier | 2 | The chosen Hand makes 3 Moves |
| **Rally the Posse** | General | 1 | Up to 3 allied Hands each make 1 Move |
| **Ace in the Hole** | General | 2 | Gain Bonus Grit tokens (cleared at end of Round) |
| **The Walk-Down** | Soldier | 2 | Straight Move, then an Attack with +1 reroll *(Earp)* |
| **Always Get Your Man** | Soldier | 3 | 2 Attacks, then a Move *(Reeves)* |
| **Train Robbery** | General | 1 | Draw 2 Gambits from the deck *(James)* |
| **Lightning Hands** | Soldier | 2 | Make 2 Attacks *(Billy)* |
| **Quickdraw Duel** | Reaction | — | When targeted, draw first: make 1 Attack immediately *(Billy)* |

---

## 6. The co-op boss — `threats/`

**The Grizzly King** — a frontier menace for the Missions style of play (Cover 5 / Sand 8).
Its hide is too thick to wound until both bait-traps are sprung (Switches 1 **and** 2); on 3+ ⚡
in the collective attack it goes on a **Maul** rampage. See `threats/grizzly-king.json`.

---

## 7. Use it

```bash
# from sheet-system/ — validate the whole western set
python3 tools/validate.py $(find sets/western -name '*.json')
```

Suggested showdown: Wyatt Earp's Lawmen vs Billy the Kid's Outlaws on a town with Saloon Doors
and a Lookout Tower — winner takes Main Street.
