---
title: MDMP Trigger Specification
type: doctrine
status: CANONICAL
date: 2026-07-06
source_files: []
---

# MDMP Trigger Specification

MDMP (Military Decision-Making Process adapted for EDEN) is event-driven,
never scheduled, and never triggered by data queries. It fires when officers
disagree on a decision that crosses shop boundaries, or when a decision
requires multi-shop input that no single officer owns.

## Trigger conditions (any one is sufficient)

1. **Explicit disagreement:** Two or more officers issue handoffs with
   conflicting recommendations on the same topic.
2. **Cross-shop decision:** A Commander task requires input from ≥3 shops
   (e.g., "should we apply for this grant" touches S4/finance,
   S3/operations, S5/strategy).
3. **Officer escalation:** Any officer writes a handoff to EDEN with
   `priority: mdmp_call` requesting a council.
4. **Deadlock:** Two officers exchange ≥2 rounds of handoffs without
   resolving a question.

## What MDMP is NOT triggered by

- Data queries ("how many goats", "what's the weather") — these are
  single-shop lookups, not deliberation.
- Information requests ("what does the grant say") — S4 reads it, done.
- Status requests ("are the officers alive") — standup covers this.
- Single-shop decisions within the officer's own domain.

## MDMP convening sequence

### Phase 1 — Convene (EDEN)

1. EDEN detects a trigger condition (from standup, handoff trail, or
   Commander direction).
2. EDEN writes an `MDMP_CALL.md` to the handoffs root with:
   - The question to be decided
   - Which officers are convened (by shop)
   - Position papers due within 24 hours
   - The evidence standard required
3. EDEN ledgers the call: `--event mdmp_call --to <officers> --outcome ok`

### Phase 2 — Position papers (convened officers)

1. Each convened officer reads the MDMP_CALL from their inbox.
2. Within 24 hours, each writes a `POSITION_<shop>.md` to the MDMP
   working directory with:
   - Their recommendation (one clear sentence)
   - Reasoning (≤3 paragraphs)
   - Evidence (cited file paths, API responses, session IDs)
   - Risks and mitigations
   - Dissenting notes (if the officer has internal reservations)
3. Each officer ledgers their position: `--event handoff --to eden --outcome ok`
4. If an officer cannot form a position (missing data, blocked
   credentials), they write `POSITION_<shop>.md` stating what's
   needed and flag `UNRESOLVED — needs <x>`. This is valid input.

### Phase 3 — Synthesis (EDEN)

1. EDEN reads all position papers.
2. EDEN produces an `MDMP_DECISION.md` with:
   - The recommendation (one sentence)
   - How each position was weighed
   - Dissenting views and why they were overruled or accommodated
   - Unresolved items for Commander adjudication
3. If EDEN can decide within O-6 authority → decision is final,
   recorded in the ledger.
4. If the decision exceeds O-6 authority → packaged for Commander
   with all position papers attached.

### Phase 4 — Execute and close

1. Affected officers are notified via handoff.
2. The decision is recorded in the wiki under `wiki/syntheses/MDMP-<date>-<topic>.md`.
3. All MDMP artifacts are archived under `handoffs/_mdmp/<date>-<topic>/`.
4. Ledger: EDEN writes closing `mdmp_call` with outcome + decision path.

## MDMP cadence and deadlines

- MDMP is **rare by design.** Most decisions are single-shop. If MDMP
  fires more than once a week, the trigger conditions are too loose.
- Position papers due within **24 hours** of convening. Officers flag
  if they need more time and why.
- No decision sits in MDMP for more than **72 hours** without
  escalation to Commander as `MDMP STALLED`.

## Integration with standup

The 0800 standup includes an MDMP status line:
- `MDMP: none active` — normal state
- `MDMP: <topic> — N/N positions received, decision by <time>` — in progress
- `MDMP: <topic> STALLED — Commander escalation` — overdue

---
Changelog:
- 2026-07-06 — CANONICAL, MDMP trigger spec + four-phase convening sequence