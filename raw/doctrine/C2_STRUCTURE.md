---
title: C2 Structure — Officers Standing, Parents On Demand
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
source_files: []
system_sources:
  - Commander ruling 2026-07-06 (officer stand-up project, this session)
  - /persist/eden/hermes/workspace/eden/ai/roster.py (verified by EDEN, 2026-07-06)
  - live EDEN SOUL C2 chain (dashboard API capture 2026-07-06)
---

# C2 Structure

```
Commander / E-9 (Chad) ↔ EDEN (O-6, system-gateway main agent)
   → 6 Staff Officers (standing Hermes profiles)
      → parent agents (on demand via delegate_task — never standing)
```

## The six officers (Commander ruling 2026-07-06 — supersedes the SOUL's earlier "Medical" line)

S1_Personnel · S2_Intel · S3_Operations · S4_Logistics · S5_Plans · S6_Comms
(exact `roster.py` names). **There is no Medical shop** — medical is covered by
VetAI as an on-demand parent under S3_Operations.

## Tier semantics

| Tier | Runtime form | Identity artifacts | Token cost |
|---|---|---|---|
| EDEN (O-6) | system gateway main agent | live SOUL | always on — correct |
| Officer | Hermes profile (`~/.hermes/profiles/<shop>/`): own SOUL, skills, cron, memories | SOUL.md + CHARTER.md + PLAYBOOK.md in `workspace/doctrine/officers/<shop>/` | on its loop triggers only |
| Parent | `delegate_task` child spawned by its officer; may run a cheaper model | charter-derived prompt; playbook compiled into shop skill | only while working |

## Standing rules

1. Officers are stood up **one at a time**, gated on readiness: live data
   source + working headless tools + one loop provable end-to-end (THE RULE).
   Build order 2026-07-06: S6 → S1 → S2 → S3 → S4 → S5.
2. Officers whose loop is not yet proven carry `Activation: STANDING-READY`
   with explicit activation conditions — **no cron for unproven loops**.
3. Parents are never standing. Their identity is durable (charter on file);
   their execution is lazy (spawned per mission).
4. Deliberation flows in loops up the chain: parents → officer → EDEN →
   Commander. Each tier runs the six-step loop ([[SIX_STEP_LOOP]]).
5. The Commander's gates are unchanged: money out, signatures, live store
   charges, flashing drives.
