---
title: Agent Population Manifest — verified inventory & migration readiness
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
source_files: []
system_sources:
  - /mnt/kb/_SAFE_BACKUP_20260626/home_urbanarkconsole/hermes-workspace/_MANIFEST/autonomy/{charters,playbooks,souls}/ (enumerated 2026-07-06)
  - same tree HIERARCHY.md (locked 2026-04-27, amended through 2026-05-05) — shop assignments
  - same tree THE_SPEC.md — locked parent count 30 = 4+7+7+6+2+1+5
  - live gateway skill manifest (dashboard API capture 2026-07-06) — migrated-as-skill mapping
  - staged working copy for EDEN: /persist/eden/hermes/workspace/legacy-doctrine/ (83 files)
---

# Agent Population Manifest (verified 2026-07-06)

Every legacy agent, its doctrine artifacts, and its runtime status on
AEGIS-ARK. **No agent below runs as a standing process on this box.** Legacy
capabilities live on only where absorbed into gateway skills (last column).
Shop assignments per HIERARCHY.md (locked); playbook status per file
enumeration; "skill absorption" per the live gateway skill manifest.

## S1_Personnel (4 parents)

| Agent | Charter | Playbook | Absorbed into live skill |
|---|---|---|---|
| GovernanceAI | ✅ | ✅ full | `s1-governance-ops` |
| SecretarialAI | ✅ | ✅ full | `s1-governance-ops` |
| TaskAI | ✅ | ✅ full | `s1-task-programs-ops` |
| ProgramsAI | ✅ | ✅ full | `s1-task-programs-ops` |

**Officer S1:** legacy officer charter exists (`charters/S1_Officer.md`);
legacy officer playbook `PLAYBOOK_PERSONNEL.md`. Shop soul card
`souls/S1_Personnel.soul.yaml`. **Readiness: HIGH** — all four parents have
full doctrine and two live skills already carry their capabilities.

## S2_Intel (7 parents)

| Agent | Charter | Playbook | Absorbed into live skill |
|---|---|---|---|
| VisionAI | ✅ | ✅ full | — |
| TelemetryAI | ✅ | ⚠ draft-skeleton | — |
| WeatherAI | ✅ | ✅ full | — |
| PredictiveAI | ✅ | ✅ full | — |
| MapAI | ✅ | ⚠ draft-skeleton | — |
| CodexAI | ✅ | ✅ full | — |
| ForgeAI | ✅ | ✅ full | — |

**Officer S2:** legacy officer charter `charters/S2_Intel.md`; playbook
`PLAYBOOK_INTEL.md`; soul card present. Protocol skills live on the gateway
(`s2-neural-drift`, `cognitive-override-ceiling`). **Readiness: MEDIUM** — no
sensor data sources wired on this box yet (no cameras, no telemetry ingest);
loop cannot close on a live surface until at least one source exists.

## S3_Operations (7 parents)

| Agent | Charter | Playbook | Absorbed into live skill |
|---|---|---|---|
| LivestockAI | ✅ | ✅ full | — |
| VetAI (covers Medical — Commander ruling 2026-07-06) | ✅ | ✅ full | — |
| GreenhouseAI | ✅ | ⚠ draft-skeleton | — |
| BotanyAI | ✅ | ✅ full | — |
| AquaponicsAI | ✅ | ⚠ draft-skeleton | — |
| RoboticsAI | ✅ | ⚠ draft-skeleton | — |
| SecurityAI | ✅ | ⚠ draft-skeleton | — |

**Officer S3:** no dedicated legacy officer charter; playbooks
`PLAYBOOK_OPS.md` + `PLAYBOOK_MEDICAL.md` (the latter now VetAI source
material); soul card present. **Readiness: LOW-MEDIUM** — herd/health loops
need Farmbrite (key missing on gateway, verified 2026-07-02 audit) or
farm.sqlite access.

## S4_Logistics (6 parents)

| Agent | Charter | Playbook | Absorbed into live skill |
|---|---|---|---|
| LogisticsAI | ✅ | ✅ full | — |
| FinanceAI | ✅ | ✅ full | — |
| GrantsAI | ✅ | ✅ full | — |
| MarketingAI | ✅ | ✅ full | `s6-dispatch-ops` (dispatch function) |
| FundraisingAI | ✅ | ✅ full | `s6-dispatch-ops` (dispatch function) |
| InfrastructureAI | ✅ | ✅ full | — |

**Officer S4:** no dedicated legacy officer charter; playbook
`PLAYBOOK_LOGISTICS.md`; soul card present. **Readiness: MEDIUM** — strongest
legacy doctrine set (all six full), but finance/grants loops need live data
feeds (books, grant pipeline) not yet wired.

## S5_Plans (3 parents — EngineeringAI adopted by Commander ruling 2026-07-06)

| Agent | Charter | Playbook | Absorbed into live skill |
|---|---|---|---|
| PlansAI | ✅ | ✅ full | — |
| DevelopmentAI | ✅ | ⚠ draft-skeleton | — |
| EngineeringAI (new, non-legacy) | ✅ adopted 2026-07-06 | card only | — |

**Officer S5:** no legacy officer playbook exists (legacy set was
Personnel/Intel/Ops/Medical/Logistics/Comms). Officer artifacts must be
synthesized from soul card + children charters and marked PROPOSED
(Commander ruling 2026-07-06). Protocol skill `s5-blind-spot-scanner` lives on
the gateway. **Readiness: LOW** — synthesis-heavy shop; sensible last in build
order.

## S6_Comms (1 parent)

| Agent | Charter | Playbook | Absorbed into live skill |
|---|---|---|---|
| UXAI | ✅ | ⚠ draft-skeleton | — |

**Officer S6:** playbook `PLAYBOOK_COMMS.md`; soul card present. Live skills:
`s6-dispatch-ops`, `uac-social-loop`, `reach-engine`, `uac-content-system`,
`meta-graph-api`, `inbound-comms-processor`. **Readiness: PROVEN** — first
officer stood up and verified 2026-07-06 (profile `s6_comms`, drill passed on
gpt-5.5). Note: S6 was intentionally thin in legacy (CommsAI promoted to
EDEN-tier 2026-04-28); the new S6 officer inherits the dispatch/channel
function.

## EDEN-tier (5)

| Agent | Charter | Playbook | Status on this box |
|---|---|---|---|
| EDEN | ✅ | ✅ full | LIVE — system gateway main agent |
| CommsAI | ✅ | ✅ full | absorbed into `s6-dispatch-ops` + S6 officer |
| NexusAI | ✅ | ✅ full | not migrated |
| DESKAI | ✅ | ✅ full | not migrated |
| EDEN_Synthesizer | ❌ MISSING | ❌ MISSING | not migrated; no legacy charter/playbook found |

## Totals

- 33 charter files (31 parents + 2 officer charters) + 1 template; 30 parents
  per THE_SPEC's locked count, EDEN_Synthesizer's charter missing.
- Playbooks: 23 full · 8 draft-skeleton (Telemetry, Map, Greenhouse,
  Aquaponics, Robotics, Security, Development, UX) · draft-skeletons are
  legacy DRIFT (scope reduction) — do not port as-is.
- Souls: 7 shop soul cards (S0_EDEN + S1–S6).
- Migrated to this box: EDEN (live agent) + capabilities of 7 parents absorbed
  into 3 shop skills + S6 officer profile (2026-07-06).

## Migration-readiness gate (per officer / parent)

An officer activates (STANDING-READY → ACTIVE) when: (1) a live data source
for its loop exists on this box, (2) its tools verify headless (no
pending_approval, no missing keys), (3) one loop closes end-to-end on a real
surface, lint PASS ([[SIX_STEP_LOOP]], `tools/officer_lint.py`). A parent
migrates when its officer is ACTIVE and a real mission needs it — never
before (THE RULE).
