---
title: Mycelium S-1 Gmail Adapter 2026-07-04
type: mycelium-adapter-proof
created: 2026-07-04
status: active-near-real-time
owner: EDEN / S-1 / Loop Integrity Inspector
cron_job_id: 7878633ca0cf
---

# Mycelium S-1 Gmail Adapter — 2026-07-04

## BLUF
The first Mycelium adapter is active: Gmail → Mycelium event core → S-1 routing → local S-1 ledger/task artifact → live audit event. It runs every 2 minutes as the near-real-time trigger. The older 30-minute S-1 Gmail loop remains reconciliation/shadow backup.

## Scope proven

| Layer | Status |
|---|---|
| Event normalization | Implemented in `s1_operational/mycelium_core.py` |
| Dedupe | Stable `event_id` from source/type/external ID; duplicates suppressed |
| Routing | Gmail email events route to S-1 handler using existing S-1 classifier |
| S-1 action | Local inbound ledger/task creation only |
| Safety | No send, delete, submit, mark-read, booking confirmation, or credential use |
| Audit | `s1_live_event_audit.py` event emitted for handled events |
| Trigger | Script-only cron `Mycelium-S1-Gmail-Watch` every 2 minutes |

## Test evidence

- `test_mycelium_core.py`: 3/3 pass
- Synthetic event: receipt-like Gmail event routed to S-1, task created, audit event emitted
- Duplicate synthetic event: suppressed, no second action
- Live Gmail smoke: Gmail query succeeded, 0 unread messages at test time
- Cron job manual run: `last_status=ok`

## Trigger posture

Current:

```text
Gmail polling every 2 minutes -> Mycelium event core -> S-1 handler
```

Target future hardening:

```text
Gmail Watch/PubSub or IMAP IDLE -> Mycelium event core -> S-1 handler
```

The current phase is not yet true Gmail push/webhook, but it moves S-1 from 30-minute cron shadow mode to near-real-time Mycelium-routed events with dedupe/audit.

## Alert posture

The script is silent when no gate/high-value events are found. It emits a Telegram alert only when Mycelium records a gate-worthy S-1 event or the script fails.

## Next adapter candidates

1. Wix bookings → ProgramsAI gate events
2. Farmbrite tasks/animals → S-1/S-3 routed events
3. ARCOS critical hardware alerts → EDEN critical injection only
