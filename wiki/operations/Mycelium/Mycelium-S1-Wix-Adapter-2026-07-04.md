---
title: Mycelium S-1 Wix Bookings Adapter 2026-07-04
type: mycelium-adapter-proof
created: 2026-07-04
status: active-near-real-time
owner: EDEN / S-1 / ProgramsAI
cron_job_id: d93643ad176f
---

# Mycelium S-1 Wix Bookings Adapter — 2026-07-04

## BLUF
Second Mycelium adapter: Wix Bookings → Mycelium event core → S-1 ProgramsAI routing → local S-1 task → audit event. Polling every 5 minutes. No Wix writes, confirms, or cancellations.

## Routing

| Wix status | Mycelium category | Priority |
|---|---|---|
| CONFIRMED | booking_confirmed | high |
| CANCELLED / CANCELED / DECLINED | booking_cancelled | high |
| CREATED / PENDING | booking_pending | medium |
| other | booking_unknown | medium |

All booking events route to `S1/ProgramsAI` and inject to EDEN.

## Safety

- No Wix write, confirm, cancel, or modify.
- Local S-1 task store upsert only.
- Wix token extracted transiently from email source; never persisted or printed by the adapter.
- PII-bearing contact fields are not stored by the Mycelium adapter.

## Test evidence

- `test_mycelium_wix.py`: 4/4 pass
- Synthetic Wix event: routing, task creation, audit emission verified
- Live Wix poll: 8 bookings processed, tasks created, 0 errors
- Cron: script-only `no_agent`, 5-minute interval

## Trigger posture

```text
Wix Bookings API polled every 5 minutes → Mycelium event core → S-1 ProgramsAI handler
```

Future: Wix webhook or real-time push would replace polling.

## Adapter inventory

| # | Adapter | Cron | Interval | Status |
|---|---:|---|---|---|
| 1 | Gmail → S-1 | `7878633ca0cf` | 2m | Active |
| 2 | Wix Bookings → S-1 ProgramsAI | `d93643ad176f` | 5m | Active |
