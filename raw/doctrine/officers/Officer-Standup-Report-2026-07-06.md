---
title: Officer Stand-up Report 2026-07-06
status: DRAFT
version: 0.1
source_files:
  - /persist/eden/hermes/workspace/eden/ai/roster.py
  - /persist/eden/hermes/workspace/doctrine/officers/
source_note: "Operational doctrine report compiled from live profile verification and Commander-authorized stand-up artifacts; no animal observational facts asserted."
---

# Officer Stand-up Report — 2026-07-06

## BLUF

All six `roster.py` S-shop officers were stood up as standing Hermes profiles under EDEN. Parent agents remain on-demand only via `delegate_task`; no standing parent profiles were created. No cron was registered for unproven loops.

## Verified profiles

| Officer | Profile | Model | Profile evidence |
|---|---|---|---|
| S6_Comms | `s6_comms` | `gpt-5.5` via `openai-codex` | `hermes profile show s6_comms` reported `SOUL.md: exists`. |
| S1_Personnel | `s1_personnel` | `gpt-5.5` via `openai-codex` | `hermes profile show s1_personnel` reported `SOUL.md: exists`. |
| S2_Intel | `s2_intel` | `gpt-5.5` via `openai-codex` | `hermes profile show s2_intel` reported `SOUL.md: exists`. |
| S3_Operations | `s3_operations` | `gpt-5.5` via `openai-codex` | `hermes profile show s3_operations` reported `SOUL.md: exists`. |
| S4_Logistics | `s4_logistics` | `gpt-5.5` via `openai-codex` | `hermes profile show s4_logistics` reported `SOUL.md: exists`. |
| S5_Plans | `s5_plans` | `gpt-5.5` via `openai-codex` | `hermes profile show s5_plans` reported `SOUL.md: exists`. |

## Doctrine artifact paths

Vault copy:

- `wiki/operations/Doctrine/Officers/S1_Personnel/`
- `wiki/operations/Doctrine/Officers/S2_Intel/`
- `wiki/operations/Doctrine/Officers/S3_Operations/`
- `wiki/operations/Doctrine/Officers/S4_Logistics/`
- `wiki/operations/Doctrine/Officers/S5_Plans/`
- `wiki/operations/Doctrine/Officers/S6_Comms/`

Workspace source copy:

- `/persist/eden/hermes/workspace/doctrine/officers/`

## Parent-agent posture

Parent agents are not standing identities. Officers may instantiate parents only via `delegate_task` with charter-derived prompts.

| Officer | Parents-on-demand |
|---|---|
| S1_Personnel | TaskAI, ProgramsAI, GovernanceAI, SecretarialAI |
| S2_Intel | VisionAI, TelemetryAI, WeatherAI, SecurityAI, PredictiveAI, CodexAI, MapAI, ForgeAI |
| S3_Operations | LivestockAI, VetAI, GreenhouseAI, BotanyAI, AquaponicsAI, RoboticsAI, SecurityAI |
| S4_Logistics | LogisticsAI, FinanceAI, GrantsAI, FundraisingAI, InfrastructureAI, MarketingAI |
| S5_Plans | PlansAI, DevelopmentAI, EngineeringAI |
| S6_Comms | UXAI |

## Special adjudication notes

- `Medical` is not a standing shop. Veterinary/medical animal analysis routes to VetAI under S3_Operations.
- `S3_Ops` was superseded by exact `roster.py` name `S3_Operations`.
- S5 had no legacy officer playbook staged; Commander ruled synthesis from soul + children was authorized.
- EngineeringAI legacy charter/playbook were not staged; Commander authorized EDEN to write a proposed parent doctrine. The result is `wiki/operations/Doctrine/Officers/S5_Plans/parents/EngineeringAI.PROPOSED.md` and requires Commander adjudication before canonical promotion.

## Gates and blockers remaining

- Decide whether `EngineeringAI.PROPOSED.md` becomes canonical S5 parent doctrine.
- Decide whether any officer moves from `STANDING-READY` to a proven cron/event loop. Default is no cron until one loop is proven end-to-end.
- If gateway/runtime profile defaults must persist through NixOS-managed config, propose `/etc/nixos` diff and wait for Commander approval.

## Learning captured

The `officer-standup` skill was updated with the completed six-officer procedure, `gpt-5.5/openai-codex` verification policy, profile skill visibility pitfall, and proposed-parent synthesis pattern.
