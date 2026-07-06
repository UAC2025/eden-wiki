---
title: Officer Profile Update 2026-07-06
status: VERIFIED
version: 0.1
source_files:
  - /persist/eden/hermes/workspace/eden-wiki/wiki/operations/Doctrine/Officers/
source_note: "Profile update report from live Hermes profile checks and one-shot verification drills; no animal observational facts asserted."
---

# Officer Profile Update — 2026-07-06

## BLUF

All six standing S-shop officer profiles were refreshed from the vault-copy officer doctrine, their `SOUL.md` files were reinstalled, their profile memories were pointed at vault doctrine paths, and their model defaults were verified as `gpt-5.5` via `openai-codex`.

## Update actions

- Copied vault `SOUL.md` files from `wiki/operations/Doctrine/Officers/<Officer>/SOUL.md` into each matching profile under `/persist/eden/hermes/.hermes/profiles/<profile>/SOUL.md`.
- Rewrote each officer profile memory pointer to the vault `CHARTER.md` and `PLAYBOOK.md` paths.
- Verified each profile config retained:
  - `model.default: gpt-5.5`
  - `model.provider: openai-codex`
- Ran one-shot identity verification drills for all six profiles.

## Verification table

| Officer | Profile | SOUL sync | Drill session | Drill result |
|---|---|---:|---|---|
| S1_Personnel | `s1_personnel` | Match | `20260706_102925_24d6ec` | Identified S1, six-step loop, TaskAI/ProgramsAI/GovernanceAI/SecretarialAI, gates. |
| S2_Intel | `s2_intel` | Match | `20260706_102940_c1b2d1` | Identified S2, six-step loop, eight parents, no-actuation/no-fabrication limits. |
| S3_Operations | `s3_operations` | Match | `20260706_102956_f55a98` | Identified S3, six-step loop, seven parents, life/safety/action gates. |
| S4_Logistics | `s4_logistics` | Match | `20260706_103011_b434a2` | Identified S4, six-step loop, six parents, money/entity gates. |
| S5_Plans | `s5_plans` | Match | `20260706_103025_ce9e89` | Identified S5, six-step loop, PlansAI/DevelopmentAI/EngineeringAI PROPOSED, implementation gates. |
| S6_Comms | `s6_comms` | Match | `20260706_103100_df58f2` | Identified S6, six-step loop, UXAI, public dispatch/brand/metrics gates. |

## Standing posture

- Standing profiles: six officers only.
- Standing parents: none.
- Cron: unchanged; no unproven officer loop cron was added.
- Gateway restart: not performed.
- System/NixOS changes: none.

## Remaining adjudications

- Decide whether `EngineeringAI.PROPOSED.md` becomes canonical S5 parent doctrine.
- Decide which officer loop, if any, should be promoted from `STANDING-READY` to a proven cron/event loop.
