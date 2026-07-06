---
name: s3-farmbrite-ops
description: |
  S3_Operations' first domain skill: working the Farmbrite farm-management
  API — task audits (proven 2026-07-06), drift detection against the local
  ledger, and the GATED animal-records workflow. DATA RULE applies to every
  record. Never write to Farmbrite without a Commander-approved list.
---

# S3 Farmbrite Ops

Farmbrite is the farm's operational system of record. You read it freely;
you write to it ONLY through the gated workflow below.

## Connection (verified 2026-07-06)

- API key: `FARMBRITE_*` env var from the gateway environment; decrypted
  fallback at `/run/agenix/farmbrite`; last-resort `.env` fallback per the
  gen-26 rebuild notes. Never print the key; cite it as "key present
  (68-char)" the way the roll-call did.
- `GET /v1/tasks` — proven live: HTTP 200, ~11,747 records.
- `GET /v1/animals` — proven live but EMPTY (0 records) until the herd
  import lands. Report the zero honestly; never infer herd facts from
  other modules.

## Proven loop 1 — task audit (run freely, read-only)

1. Observe: pull live tasks; read the local task ledger.
2. Learn: diff — tasks in one and not the other, status mismatches, stale
   due-dates.
3. Decide: classify drift (data-entry lag vs real missed work).
4. Act: write a discrepancy brief to
   `workspace/doctrine/officers/S3_Operations/run/` citing task ids.
5. Adapt: `ledger_append.py --officer s3_operations --event loop_tick
   --loop farmbrite-task-audit --step adapt ...` citing the brief.

## Gated loop 2 — herd import (Commander approval REQUIRED mid-loop)

1. Observe: read vault animal sources — `raw/animals/`,
   `entities/` animal pages. These are the ONLY admissible sources.
2. Learn: draft ONE proposed Farmbrite record per animal: name, breed,
   sex, DOB if known — each field citing its raw/ source per the DATA
   RULE. No source → field stays blank, never guessed.
3. Decide: assemble the full proposed list into a review file under
   `run/`, flag conflicts (two sources disagree → both shown,
   confidence: low).
4. **GATE — STOP.** Deliver the list to the Commander. No API write of
   any kind before explicit approval of the list. If approval is partial,
   only approved rows proceed.
5. Act: import approved records via the API; capture each API response.
6. Adapt: one ledger line per import batch, evidence = API responses
   file. Then propose (do not run) the recurring herd-drift audit.

## After the herd lands (future loops, each needs its own proof drill)

Health-check reminders, FAMACHA logging support, breeding windows,
weight tracking — every new loop is proposed to the Commander, proven
once end-to-end via proof-drill, then earns its cron. One at a time.

## Hard rules

- Livestock health/breeding/death claims follow the vault's CARDINAL
  RULE: no observational claim without a raw/ citation, ever.
- You never DELETE Farmbrite records. Corrections are proposed, gated.
- Money, purchases, vet appointments with cost: report and escalate to
  the Commander — S3 does not spend.
