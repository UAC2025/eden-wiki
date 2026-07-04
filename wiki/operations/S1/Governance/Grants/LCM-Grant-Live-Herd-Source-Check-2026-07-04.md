---
title: LCM Grant Live Herd Source Check 2026-07-04
type: grant-source-verification
created: 2026-07-04
status: resolved-repo-ground-truth-source-found
owner: GovernanceAI / LivestockAI
---

# LCM Grant Live Herd Source Check — 2026-07-04

## BLUF
Resolved after Commander correction: the repository does contain the animal counts needed for the LCM draft.

## Source accepted

| Source | Evidence |
|---|---|
| `/persist/eden/hermes/workspace/eden/_MANIFEST/GROUND_TRUTH.md` | Lines 14–18 and 93–97 |
| Git history | `d285c2ae`, committed `2026-06-02T23:59:57-04:00`, message `docs(ground-truth): refresh GROUND_TRUTH.md to current state (2026-06-02)` |

## Count inserted

As of the 2026-06-02 repository ground-truth update:

- **9 Arapawa goats**
- **1 buck**
- **8 does**
- Previous **13 Arapawa / 6 unregistered** language is explicitly marked stale.
- Farmbrite is explicitly marked **not authoritative** for herd records.

## Conflict handling

A later auto-synced legacy `eden-vault/Animals/Herd-Index.md` file says 13 Arapawa. That conflicts with the repo ground-truth file. The ground-truth file explicitly says the 13-head item is stale, so the LCM draft uses the 9-head operator-ground-truth count.

## Output

Inserted into:

- `LCM-Microgrant-Draft-v4-Live-Herd-Source-2026-07-04.md`

QC output:

- `LCM-Microgrant-Draft-v4-QC-Report-2026-07-04.md`

QC result: **0 issues**.

## Gate

Draft 4 is ready for Commander approval review. S-1 may not submit until explicit approval.
