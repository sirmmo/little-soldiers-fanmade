# Little Soldiers: **Combined Arms** — a Modern & WW2 adaptation

A 20th–21st-century warfare adaptation, built on the Sheet Design Framework
(`../../FRAMEWORK.md`) and validated against the same `soldier-sheet.schema.json`.

> **The conceit.** *Little Soldiers* is already a game of plastic army men — grenades,
> mortars and snipers ship in the box — so the modern skin is the most natural of all. This
> set focuses on **commanders**: seven generals reprising real figures of **World War II** and
> **modern conflicts**, each with three signature Doctrine cards capturing their real-world
> style. Add the roster/objects from §2 to taste.

Everything here is **homebrew**, stat-balanced against the base curve. The famous matchups
(Rommel vs Montgomery at El Alamein, etc.) are flavour — generals use `color: any`, so you
assign squad colours at setup.

---

## 1. Terminology reskin (rules are identical)

| Base game | Combined Arms |
|-----------|---------------|
| Little Soldier | **Unit / Trooper** |
| General | **Commander** |
| Play Zone | **Theatre / AO** (area of operations) |
| HQ | **Staging Area** |
| Order token | **Command token** |
| Heart ♥ (damage) | **Casualty** |
| Toughness | **Endurance** |
| Defense 🛡 | **Cover** |
| Shield / Scout token (−defense) | **Suppression token** (pinned → easier to hit) |
| Flag / Battle Track | **Objective marker** on the **Front Line** |
| Star token | **Initiative token** |
| Levels module | **Elevation** (rooftops, ridgelines) |
| Grenade die · Mortar · Sniper die | unchanged — already modern |
| Crate (Advanced Tactics) | **Supply Cache** |
| Tactics card | **Doctrine card** |

## 2. Roster (maps straight onto the base archetypes)

The base units are already modern; just rename:

| Unit | = base | Cover/End. | Special Action |
|------|--------|:----------:|----------------|
| **Rifleman** | Infantry | 2 / 5 | **Recon** — Suppress up to 2 enemies (Scout) |
| **Marksman** | Sniper | 3 / 3 | **Overwatch Shot** — Risky Shot with the Sniper die |
| **Grenadier** | Grenadier | ? / 6 | **Frag Out** — Throw a Grenade |
| **Mortar Team** | Operator | ? / 5 | **Fire Mission** — Mortar Shot |

(Reuse the base `examples/` JSON as-is, or copy them here renamed. Generals below are the focus
of this expansion.)

---

## 3. WW2 Commanders (`generals/`)

| Commander | Reprises | Doctrine | Signature Doctrine cards |
|-----------|----------|----------|--------------------------|
| **Erwin Rommel** | "The Desert Fox" | Bold armoured maneuver, deep thrusts | **Dash to the Wire** · Rapid Redeployment · Air Strike |
| **George S. Patton** | US Third Army | Relentless offensive speed | **Audacity** · Overwhelming Force · Rapid Redeployment |
| **Bernard Montgomery** | El Alamein | Methodical set-piece + massed firepower | **El Alamein Set-Piece** · Air Strike · Forward Observers |
| **Georgy Zhukov** | Stalingrad / Berlin | Deep operations, overwhelming mass | **Deep Operation** · Overwhelming Force · Combined Arms |

## 4. Modern Commanders (`generals/`)

| Commander | Reprises | Doctrine | Signature Doctrine cards |
|-----------|----------|----------|--------------------------|
| **Norman Schwarzkopf** | Gulf War | Combined-arms "left hook"; overwhelming force | **The Left Hook** · Air Strike · Overwhelming Force |
| **David Petraeus** | COIN / the Surge | Clear-hold-build, sustain the force | **Clear and Hold** · CASEVAC · Combined Arms |
| **Võ Nguyên Giáp** | Asymmetric / People's War | Harass, attrit, endure | **People's War** · Suppressing Fire · Rapid Redeployment |

## 5. The shared Doctrine deck (`tactics/`)

Cards several commanders draw on (the common modern playbook):

| Card | Type | Cond. | Effect |
|------|------|:----:|--------|
| **Overwhelming Force** | Soldier | 2 | Make up to 3 Attacks on different targets |
| **Air Strike** | General | 3 | 1 Attack on any enemy, ignoring line of sight, +1 reroll |
| **Suppressing Fire** | Reaction | — | A foe declaring a target rolls −1 die |
| **Rapid Redeployment** | Soldier | 2 | The chosen unit makes 3 Moves |
| **Combined Arms** | General | 1 | Up to 3 allied units each make 1 Move |
| **Forward Observers** | General | 2 | Suppress (Expose) up to 3 enemies anywhere |
| **CASEVAC** | General | 1 | Remove up to 2 Casualties from an allied unit in range |

Plus the seven unique signature cards named in §3–4. All are grounded in the primitives of
`FRAMEWORK.md` §5.4 and gated by Command conditions per §6.

---

## 6. Use it

```bash
# from sheet-system/ — validate the whole modern set
python3 tools/validate.py $(find sets/modern -name '*.json')
```

Drop any commander into either side's Staging Area in place of a base General. Suggested
historical matchups: Rommel ↔ Montgomery, Patton ↔ Rommel, Zhukov ↔ (any Axis),
Schwarzkopf ↔ a conventional foe, Petraeus ↔ Giáp (conventional vs asymmetric).
