---
title: Mycelium → Officer Event Routing Table
type: doctrine
status: CANONICAL
date: 2026-07-06
source_files: []
---

# Mycelium → Officer Event Routing

The Mycelium adapters (Gmail, Wix, Calendar, Farmbrite, Weather) already
emit events. This table says who owns each event type, what tier of
response is expected, and whether it auto-routes or waits for standup.

## Tier definitions

| Tier | Name | Action |
|---|---|---|
| 0 | Log-only | Append to ledger; no officer action |
| 1 | Officer review | Route to owning officer's inbox for next-session review |
| 2 | Standup flag | Surface in 0800 standup as `info` line |
| 3 | Blocker | Surface in standup as `blocker`; requires same-day acknowledgment |
| 4 | Emergency | Commander alert (not yet wired — placeholder) |

## Routing Table

### From: Mycelium-S1-Gmail (every 2m)

| Trigger | Officer | Tier | Notes |
|---|---|---|---|
| Grant-related email from known funder domain | S4_Logistics | 2 | Create handoff `gmail-grant-<id>.md` in S4 inbox |
| Donation receipt (PayPal, Stripe, etc.) | S4_Logistics | 1 | Log and route; S4 files for tax prep |
| Registration/volunteer inquiry | S1_Personnel | 1 | Route to S1 for ProgramsAI handling |
| Compliance/legal/IRS communication | S1_Personnel | 3 | Blocker — same-day acknowledgment |
| Vendor invoice or bill | S4_Logistics | 2 | Route with priority; payment = Commander gate |
| General inquiry (unclassified) | S1_Personnel | 1 | Default routing |

### From: Mycelium-S1-Wix (every 5m)

| Trigger | Officer | Tier | Notes |
|---|---|---|---|
| New store order | S4_Logistics | 2 | Fulfillment reminder; money = Commander gate |
| Booking/event registration | S1_Personnel | 1 | Route to ProgramsAI |
| Contact form submission | S1_Personnel | 1 | Standard routing |
| Donation via Wix | S4_Logistics | 2 | Receipt and log |

### From: Mycelium-S1-Calendar (daily 0900)

| Trigger | Officer | Tier | Notes |
|---|---|---|---|
| Upcoming grant deadline (7 days) | S4_Logistics | 3 | Blocker — draft must be ready |
| Scheduled farm event this week | S3_Operations | 1 | Operational awareness |
| Board meeting approaching | S1_Personnel | 2 | Governance packet prep needed |
| Compliance filing due (14 days) | S1_Personnel | 2 | Prep window warning |

### From: Mycelium-S1-Farmbrite (every 30m)

| Trigger | Officer | Tier | Notes |
|---|---|---|---|
| Task drift > 10 records | S3_Operations | 2 | Indicates sync gap |
| New task added by external user | S3_Operations | 1 | Awareness only |
| Task overdue > 30 days | S1_Personnel | 2 | Escalation candidate |

### From: S2-Weather-Fusion / S2-Weather-Threshold (every 15m)

| Trigger | Officer | Tier | Notes |
|---|---|---|---|
| Frost warning | S3_Operations | 3 | Livestock shelter + greenhouse prep |
| Heat stress alert (>85°F) | S3_Operations | 3 | Pig wallows, cattle shade |
| Heavy rain/flood watch | S3_Operations | 2 | Pasture rotation, drainage |
| Severe storm warning | S3_Operations | 3 | All-hands prep; Commander alert |
| Wind advisory >30mph | S3_Operations | 1 | Structural awareness |

### From: S2-Alive-Loop (hourly)

| Trigger | Officer | Tier | Notes |
|---|---|---|---|
| Source degradation (weather APIs down) | S2_Intel | 1 | Self-monitoring |
| S1 task gates active | S1_Personnel | 2 | Escalation from S2 deliberation |
| No alerts — all clear | — | 0 | Log only |

## Routing mechanics

1. The Mycelium adapter writes its output as usual.
2. At standup (0800) or on manual EDEN invocation, an officer reads
   the routing table and checks: did any of my triggers fire?
3. If yes: the officer retrieves the adapter output, drafts a handoff
   response, and ledgers the action.
4. Tier 3+ events are surfaced in the standup BLUF immediately.

## Future: auto-route via inbox write

Currently, routing is manual (standup reads the table). The next
iteration — after the handoffs mechanism is proven — writes adapter
outputs directly to officer inboxes as `.md` handoff files, making
the routing automatic. This is the "Mycelium nervous system" the
Commander has described. This table is the schema for that future.

---
Changelog:
- 2026-07-06 — CANONICAL, routing table for all 12 Mycelium + weather adapters
