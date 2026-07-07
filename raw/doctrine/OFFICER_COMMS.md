---
title: Officer Comms Doctrine — file-based handoffs + ledger trails
type: doctrine
status: CANONICAL
date: 2026-07-06
source_files: []
---

# Officer Comms Doctrine

EDEN officers do not share a message bus. They run as isolated Hermes profiles,
each in its own session. This doctrine defines the mechanism by which they
communicate — file-based handoffs with ledger trails — and the rules that
govern cross-shop deliberation.

## The model

Each officer has an **inbox** and a **sent** directory under the handoffs tree:

```
/persist/eden/hermes/workspace/handoffs/
├── S1_Personnel/inbox/
├── S1_Personnel/sent/
├── S2_Intel/inbox/
├── S2_Intel/sent/
├── S3_Operations/inbox/
├── S3_Operations/sent/
├── S4_Logistics/inbox/
├── S4_Logistics/sent/
├── S5_Plans/inbox/
├── S5_Plans/sent/
├── S6_Comms/inbox/
└── S6_Comms/sent/
```

## Send a handoff (writing officer)

1. **Write** a handoff file to `<recipient>/inbox/<timestamp>-<topic>.md`.
   Format: YAML frontmatter with `from`, `to`, `priority`, `topic`, then
   markdown body describing the request, context, and any deadlines.
2. **Ledger** the handoff via `ledger_append.py`:
   `--event handoff --to <officer> --outcome ok --evidence <handoff-file-path>`
3. **Block** on gates: if the handoff requires Commander adjudication, write
   it as `PROPOSED` and append `outcome blocked` to the ledger.

## Receive handoffs (reading officer)

At session start (or standup tick), the officer:
1. **Lists** its `inbox/` directory.
2. **Reads** the oldest unread handoff first (by filename timestamp).
3. **Acts** on it per the six-step loop.
4. **Moves** handled handoffs to `archive/` under the recipient's directory.
5. **Ledgers** receipt: `--event loop_tick --step observe --outcome ok`
   noting the handoff that was processed.

Timed out handoffs (7+ days unhandled) are surfaced in the officer standup
as `blocker` lines.

## Directives

- **Never delete.** Archive moved handoffs; never remove them.
- **One handoff, one action.** Don't bundle requests. If two officers
  need the same data, write separate handoffs.
- **Receipts rule applies.** Every handoff claims an evidence path. A
  handoff reading "please check X" without a source cite is returned
  with `outcome fail` to the sender.
- **Commander gate.** Handoffs that direct another officer to publish,
  spend, sign, send externally, or reconfigure are automatically `blocked`
  — they become Commander approval requests instead.

## Cross-shop deliberation (MDMP light)

When two officers disagree or a decision spans shops:
1. The initiating officer writes a `DELIBERATION_REQUEST` handoff to the
   other officer(s), stating its position and citing evidence.
2. Each recipient writes a `POSITION` handoff back within 24 hours (or
   flags `blocked — needs more data`).
3. The initiating officer synthesizes and escalates to EDEN with all
   positions attached.
4. EDEN either rules (if the decision is within O-6 authority) or
   packages it for Commander adjudication.

This is not a real-time council — it's asynchronous, file-trailed, and
survives model/provider changes. Every step writes a ledger line.

## Standup integration

The 0800 standup cron now includes an inbox check:
- Each officer reports `inbox: N unread` in its status line.
- Unread handoffs older than 48 hours are flagged as blockers.
- The standup report includes an `open handoffs` section.

---
Changelog:
- 2026-07-06 — CANONICAL, established file-based officer comms pattern
