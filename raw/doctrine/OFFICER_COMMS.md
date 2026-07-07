---
title: Officer Comms — file-based handoffs between officers
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
source_files: []
system_sources:
  - OFFICER_LEDGER.md (PROPOSED 2026-07-06) — handoff event type and `to` field already in schema
  - EDEN officer roll-call audit 2026-07-06 (finding: "Inter-officer: none — no bus, no shared memory")
  - PARENT_INVOCATION.md — mission block format reused here
  - TELEMETRY_POLICY.md (CANONICAL) — ledger never committed to wiki; wiki receives synthesis only
---

# Officer Comms (PROPOSED 2026-07-06)

Today every "deliberation" is EDEN fanning out `delegate_task` calls and
synthesizing — EDEN-as-switchboard. This doctrine gives officers a lateral
channel that needs **zero new infrastructure**: a handoff is one file plus
one ledger line, and delivery is guaranteed by sessions the officers already
run. The [[OFFICER_LEDGER]] schema has had `event:handoff` and a `to` field
since day one; this is the mechanism that consumes them.

**A handoff moves work sideways. It never moves authority.** The receiver
decides inside its own charter; anything gate-shaped still goes up the chain
(officer → EDEN → Commander), never sideways.

## The channel

```
/persist/eden/hermes/workspace/handoffs/<shop>/inbox/   ← others write here
/persist/eden/hermes/workspace/handoffs/<shop>/done/    ← receiver archives here
```

Shops: `s1_personnel s2_intel s3_operations s4_logistics s5_plans s6_comms`
plus `eden` (EDEN has an inbox too — escalations are handoffs up).

Gateway workspace, same rationale as the officer ledger: every profile can
read and write it. No bus, no sockets, no queues — unproven need
([[OFFICER_LEDGER]] non-goals hold here too).

## Sending — two writes, always both

1. **The payload file** at `handoffs/<receiver>/inbox/<UTC-ts>_<sender>_<slug>.md`
   (example: `2026-07-06T2140Z_s2_frost-warning.md`):

```markdown
---
from: s2_intel
to: s3_operations
ts: 2026-07-06T21:40:00Z
re: frost warning for kidding pens
tier: ACTION            # FYI | ACTION | DECISION
expires: 2026-07-08T00:00:00Z
---
MISSION: <one sentence — the outcome the receiver owes, not the activity>
CONTEXT: <verified inputs only — paths, data, constraints; DATA RULE applies:
  every factual claim carries its evidence path or is marked UNKNOWN>
DEADLINE/BUDGET: <when this stops mattering>
RETURN: <what the sender needs back, or "none — FYI">
```

2. **The ledger line** (per [[OFFICER_LEDGER]] schema), `evidence` pointing at
   the payload file:

```json
{"ts":"2026-07-06T21:40:00Z","officer":"s2_intel","event":"handoff","outcome":"ok","detail":"frost warning → S3 kidding pens","evidence":"workspace/handoffs/s3_operations/inbox/2026-07-06T2140Z_s2_frost-warning.md","to":"s3_operations"}
```

File without ledger line = invisible (nothing announces it). Ledger line
without file = fabrication (claim with no artifact). **Both, always.**

## Tiers

| Tier | Receiver owes | Example |
|---|---|---|
| `FYI` | Read it. No reply. | S2 weather note with no action needed |
| `ACTION` | An artifact + ack tick, inside the receiver's charter | S4 strategy → S6 drafts dispatch copy |
| `DECISION` | Escalation — receiver packages it for EDEN/Commander; a handoff can *request* a decision, never *make* one | anything touching money, publish, signature, living-being gates |

## Receiving — inbox first, always

At **Observe** (step 1 of the six-step loop), before any new work:

```bash
ls /persist/eden/hermes/workspace/handoffs/<my_shop>/inbox/ 2>/dev/null
# CHECK: empty → proceed. Non-empty → process every file below before new tasking.
```

Per file, oldest first:

1. Read it. Expired (`expires` in the past) → move to `done/`, append a
   `loop_tick` with `outcome:noop, detail:"expired unread: <file>"`. Done.
2. Live → act by tier within your charter. ACTION produces an artifact in
   your own `run/`; DECISION produces an escalation packet to EDEN.
3. Move the file `inbox/` → `done/` (move IS the ack-of-receipt; a file
   still in inbox/ is by definition unprocessed — this is what makes
   re-runs idempotent).
4. Append your own ledger `loop_tick` citing the sender's handoff line in
   `detail` and your artifact in `evidence` ([[OFFICER_LEDGER]] rule 2).

## Delivery ticks — when handoffs actually move

No daemon watches these directories. Delivery rides sessions that already
happen:

- **Any officer session start**: inbox check is step 1 of Observe (now in
  every PLAYBOOK).
- **Daily standup cron** is the guaranteed tick: it reads the last 24 h of
  ledger `handoff` lines, checks each named receiver's `inbox/`, and lists
  every unprocessed handoff in the standup synthesis. **A handoff older
  than 24 h still sitting in inbox/ is flagged STALE** — EDEN decides
  whether to wake the receiver or escalate.

Worst-case latency is therefore one standup cycle (~24 h). If a signal
can't wait that long it is not a handoff, it is an escalation: send it up
to EDEN, who can wake the receiving officer directly.

## Rules

1. Officers hand off to officers (and to EDEN). Parents never send or
   receive handoffs — a parent that finds cross-shop work returns it to its
   officer as part of its return contract ([[PARENT_INVOCATION]]).
2. A handoff never crosses a Commander gate and never orders the receiver
   outside its charter. Receiver disagrees → it writes back a `DECISION`
   handoff or escalates; disagreement between shops that survives one
   round-trip is an `mdmp_call` ([[OFFICER_LEDGER]] rule 4).
3. DATA RULE applies inside payloads: no observational claim without an
   evidence path. A handoff built on fabricated data poisons a second shop
   — worse than fabricating locally.
4. `handoffs/` is telemetry, like the ledger: never committed to the wiki.
   The standup synthesis is what the vault receives (TELEMETRY_POLICY).
5. Sweep discipline: receiver keeps the newest ~50 files in `done/`, deletes
   older ones at standup; the ledger remains the permanent record.

## Worked examples (the two the audit found missing)

**S2 weather alert → S3 livestock.** S2's forecast source shows a hard
frost. S2 writes `handoffs/s3_operations/inbox/<ts>_s2_frost-warning.md`
(tier ACTION, CONTEXT cites the forecast artifact in S2's run/) + ledger
line. S3's next session — or the standup tick — finds it: S3 produces a
pen-protection checklist in its own run/, moves the file to done/, appends
its loop_tick citing S2's line. No EDEN turn was spent switchboarding.

**S4 strategy → S6 dispatch.** S4's MarketingAI (spawned per
[[PARENT_INVOCATION]]) returns a campaign strategy. S4 verifies it, then
hands off tier ACTION to S6: MISSION "draft dispatch copy for X", CONTEXT
citing the strategy artifact. S6 drafts copy in its run/ — and stops:
**publishing is a Commander gate**, so S6's return is a draft plus an
escalation, never a live post. The doctrine-without-mechanism gap
(S4→S6 exists on paper) is now a file path.

## Activation & proof drill

Gated like the ledger (GO/NO-GO board): activates alongside
[[OFFICER_LEDGER]]. Acceptance = one proven round-trip, run as a drill:

1. S2 sends a test ACTION handoff to S3 (payload marked `DRILL`).
2. S3's next session processes it: artifact + move to done/ + ack tick.
3. Standup synthesis shows the pair (handoff line + ack tick) with zero
   STALE entries.

Both ledger lines + both artifacts = PASS. Any missing leg = FAIL, fix the
playbook hook, re-run. Officers adopt shop-by-shop after the drill passes,
same as ledger adoption.
