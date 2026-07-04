---
title: LCM Grant Live Herd Source Check 2026-07-04
type: grant-source-verification
created: 2026-07-04
status: blocked-live-count-source
owner: GovernanceAI / LivestockAI
---

# LCM Grant Live Herd Source Check — 2026-07-04

## BLUF
EDEN attempted to pull live herd counts for the LCM grant using locally available live-record surfaces. **No usable live animal count source was available inside the current Hermes session.** Therefore no herd counts were inserted into the grant.

## Checked sources

| Source | Result |
|---|---|
| `s1_operational/data/farmbrite/eden_farmbrite_source.db` | `animals` table exists but contains `0` rows |
| `eden/eden_farm.db` | SQLite file exists but has no `animals` table |
| `/opt/eden-core/app/data/farmbrite/animals_snapshot.json` | missing or unreadable from Hermes |
| `/opt/eden-core/app/data/livestock/animals.json` | missing or unreadable from Hermes |

## Decision
No current herd count, Arapawa count, sex count, breeding-stock count, or pregnancy/breeding status was inserted.

## Required gate to continue
Provide or authorize a live source for animal records:

1. readable local livestock JSON/DB path, or
2. current-session authorization to use Farmbrite credentials/API for read-only animal pull, or
3. exported Farmbrite animal CSV/JSON.

Until then, the LCM grant remains QC-clean only with a live-count placeholder.
