---
title: Officer Ledger — shared inter-officer event ledger
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
source_files: []
system_sources:
  - TELEMETRY_POLICY.md (CANONICAL, Commander ruling 2026-07-06)
  - EDEN officer roll-call audit 2026-07-06 (finding: "Inter-officer: none — no bus, no shared memory")
---

# Officer Ledger (PROPOSED 2026-07-06)

EDEN's roll-call audit found the six officer profiles are isolated: no bus,
no shared memory, no MDMP trigger. This doctrine wires the minimum viable
inter-officer channel — a shared, cron-synchronized, append-only ledger —
without building a message bus we haven't proven we need.

Per TELEMETRY_POLICY: the ledger is a heartbeat/handoff monitor, never
committed to the wiki; the wiki receives synthesis only.

## Location

`/persist/eden/hermes/workspace/ledgers/officers.jsonl`

- Gateway workspace, so EDEN and all six officer profiles can read/write it.
- Append-only. One JSON object per line. Never edited, never truncated;
  rotate by year (`officers-2026.jsonl`) if it grows past ~10 MB.

## Schema (one line per event)

```json
{"ts":"2026-07-06T18:40:00Z","officer":"s6_comms","event":"loop_tick","loop":"s6-dispatch","step":"act","outcome":"ok","detail":"one-line human note","evidence":"workspace/path/or/session-id","to":null}
```

| Field | Required | Values |
|---|---|---|
| `ts` | yes | UTC ISO-8601 |
| `officer` | yes | `s1_personnel` … `s6_comms`, or `eden` |
| `event` | yes | `loop_tick` \| `handoff` \| `blocker` \| `flip` \| `standup` \| `mdmp_call` |
| `loop` | for loop_tick | loop name from the officer's PLAYBOOK |
| `step` | for loop_tick | `observe|learn|decide|act|adapt` (six-step loop) |
| `outcome` | yes | `ok` \| `fail` \| `blocked` \| `noop` |
| `detail` | yes | one line a human can read |
| `evidence` | yes | artifact path or session id — DATA RULE applies; no claim without it |
| `to` | for handoff/mdmp_call | receiving officer |

## Rules

1. **Every officer loop tick appends one line** (usually at `adapt`).
   Cron does not run the work; cron triggers a loop — the tick line proves
   the loop actually turned.
2. **Handoffs are two lines**: sender writes `event:handoff, to:<officer>`;
   receiver acknowledges with its own `loop_tick` citing the sender's line.
3. **Model flips** (openai-codex ↔ anthropic, per PROVIDER_POLICY) are
   logged as `event:flip` by whoever performs the flip.
4. **`mdmp_call`** is the MDMP trigger EDEN's audit found missing: any
   officer may write one naming the convener; S1 watches for it at standup.
5. **Daily standup synthesis**: the `officer-standup` cron reads the last
   24 h of ledger lines and writes ONE synthesis page per day to
   `wiki/operations/Officer-Standups/` citing the ledger — narrative, not
   log (THE_SPEC Property 7). No per-tick packets in the vault.
6. Reading the ledger is always allowed; officers consult it at `observe`.

## Non-goals (deliberately)

- No message bus, no sockets, no queues — unproven need.
- No wiki commits of raw ticks (TELEMETRY_POLICY).
- No standing parent agents woken by ledger lines.

## Activation

Gated on the S6 proof loop (GO/NO-GO board): the ledger is created and S6
writes to it during the proof run; the other five officers adopt it only
after the proof loop passes.
