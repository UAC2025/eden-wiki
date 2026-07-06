#!/usr/bin/env python3
"""ledger_append — the ONLY approved way to write the officer ledger.

Enforces the OFFICER_LEDGER doctrine schema so malformed entries are
impossible (S6's first hand-written tick had invented field names and a
wrong year — this tool exists so that can't happen again).

Usage (officers call this via the terminal tool):
    python3 tools/ledger_append.py \
        --officer s6_comms --event loop_tick --loop social-dispatch \
        --step adapt --outcome ok \
        --detail "one-line human note" \
        --evidence workspace/path/or/session-id [--to eden]

The timestamp is stamped by the tool (UTC, now) — officers never supply it.
Exit code 0 = appended; non-zero = rejected with a reason (fix and retry;
do NOT hand-write the ledger as a workaround).
"""

import argparse
import datetime
import json
import os
import sys
from pathlib import Path

DEFAULT_LEDGER = Path("/persist/eden/hermes/workspace/ledgers/officers.jsonl")

OFFICERS = {"s1_personnel", "s2_intel", "s3_operations",
            "s4_logistics", "s5_plans", "s6_comms", "eden"}
EVENTS = {"loop_tick", "handoff", "blocker", "flip", "standup", "mdmp_call"}
OUTCOMES = {"ok", "fail", "blocked", "noop", "partial"}
STEPS = {"observe", "learn", "decide", "act", "adapt"}


def fail(msg: str) -> None:
    print(f"LEDGER REJECTED: {msg}", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--officer", required=True)
    ap.add_argument("--event", required=True)
    ap.add_argument("--loop", default=None)
    ap.add_argument("--step", default=None)
    ap.add_argument("--outcome", required=True)
    ap.add_argument("--detail", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--to", dest="to", default=None)
    ap.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    a = ap.parse_args()

    if a.officer not in OFFICERS:
        fail(f"unknown officer {a.officer!r} — one of {sorted(OFFICERS)}")
    if a.event not in EVENTS:
        fail(f"unknown event {a.event!r} — one of {sorted(EVENTS)}")
    if a.outcome not in OUTCOMES:
        fail(f"unknown outcome {a.outcome!r} — one of {sorted(OUTCOMES)}")
    if a.event == "loop_tick":
        if not a.loop:
            fail("loop_tick requires --loop (loop name from the PLAYBOOK)")
        if a.step not in STEPS:
            fail(f"loop_tick requires --step, one of {sorted(STEPS)}")
    if a.event in {"handoff", "mdmp_call"}:
        if a.to not in OFFICERS:
            fail(f"{a.event} requires --to <officer>")
    if not a.detail.strip():
        fail("--detail must be a non-empty human-readable line")
    if not a.evidence.strip():
        fail("--evidence must cite a real path or session id — "
             "if there is genuinely nothing to cite, write 'none: <why>'")
    if len(a.detail) > 500:
        fail("--detail over 500 chars — the ledger is a heartbeat, "
             "not a report; put the narrative in the wiki")

    entry = {
        "ts": datetime.datetime.now(datetime.timezone.utc)
              .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "officer": a.officer,
        "event": a.event,
        "loop": a.loop,
        "step": a.step,
        "outcome": a.outcome,
        "detail": a.detail.strip(),
        "evidence": a.evidence.strip(),
        "to": a.to,
    }

    a.ledger.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry) + "\n"
    # O_APPEND single write: atomic enough for line-oriented JSONL
    fd = os.open(a.ledger, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        os.write(fd, line.encode())
    finally:
        os.close(fd)
    print(f"LEDGER OK: {entry['ts']} {a.officer} {a.event} {a.outcome}")


if __name__ == "__main__":
    main()
