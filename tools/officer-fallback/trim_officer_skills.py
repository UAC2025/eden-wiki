#!/usr/bin/env python3
"""Trim officer profile skills to their domain keep-lists (quarantine, not delete).

Implements raw/doctrine/officers/Officer-Skill-Manifest-2026-07-06.md.

Usage (needs root or the hermes user):
    sudo python3 trim_officer_skills.py                 # dry-run, all officers
    sudo python3 trim_officer_skills.py --apply s6_comms
    sudo python3 trim_officer_skills.py --apply --strict  # also quarantine ADJUDICATE items

Skills not on KEEP (or ADJUDICATE, unless --strict) move to
profiles/<p>/skills-quarantine-2026-07-06/ — restore is a `mv` back.
Never deletes anything.
"""

import argparse
import shutil
import sys
from pathlib import Path

HERMES_HOME = Path("/persist/eden/hermes/.hermes")
QUARANTINE = "skills-quarantine-2026-07-06"

BASELINE = {"officer-standup", "eden-operations", "eden-wiki"}

KEEP = {
    "s1_personnel": {"s1-governance-ops", "s1-task-programs-ops",
                     "mdmp-council-protocol", "eden-verdict-protocol"},
    "s2_intel": {"s2-intel-ops", "s2-neural-drift", "forensic-mirror-analysis"},
    "s3_operations": set(),   # no S3 domain skill exists yet (capability gap)
    "s4_logistics": set(),    # same gap
    "s5_plans": {"claude-code", "codex", "opencode", "s5-blind-spot-scanner"},
    "s6_comms": {"s6-dispatch-ops", "inbound-comms-processor"},
}

# Loaded today but pending Commander adjudication (kept unless --strict).
ADJUDICATE = {
    "s1_personnel": {"s2-intel-ops", "s6-dispatch-ops", "inbound-comms-processor",
                     "forensic-mirror-analysis", "cognitive-override-ceiling",
                     "s5-blind-spot-scanner", "s2-neural-drift"},
    "s2_intel": set(),
    "s3_operations": set(),
    "s4_logistics": set(),
    "s5_plans": {"cognitive-override-ceiling"},
    "s6_comms": {"reach-engine", "uac-social-loop", "uac-content-system",
                 "meta-graph-api"},
}


def find_skills_dir(profile_dir: Path) -> Path | None:
    for cand in (profile_dir / "skills",):
        if cand.is_dir():
            return cand
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("profiles", nargs="*", default=[],
                    help="officer profiles to trim (default: all six)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="also quarantine ADJUDICATE items")
    args = ap.parse_args()
    profiles = args.profiles or sorted(KEEP)
    rc = 0

    for prof in profiles:
        if prof not in KEEP:
            print(f"[ERR]  unknown profile {prof}")
            rc = 1
            continue
        pdir = HERMES_HOME / "profiles" / prof
        sdir = find_skills_dir(pdir)
        if sdir is None:
            print(f"[MISS] {pdir}/skills not found — layout differs, skipping")
            rc = 1
            continue
        keep = BASELINE | KEEP[prof] | (set() if args.strict else ADJUDICATE[prof])
        entries = sorted(p for p in sdir.iterdir() if not p.name.startswith("."))
        to_move = [p for p in entries if p.name not in keep]
        kept = [p for p in entries if p.name in keep]
        print(f"\n== {prof}: {len(entries)} skills, keeping {len(kept)}, "
              f"quarantining {len(to_move)}")
        for p in to_move:
            print(f"   -> quarantine {p.name}")
        if args.apply and to_move:
            qdir = pdir / QUARANTINE
            qdir.mkdir(exist_ok=True)
            for p in to_move:
                shutil.move(str(p), str(qdir / p.name))
            print(f"[DONE] {prof}: moved {len(to_move)} to {qdir}")

    if not args.apply:
        print("\nDry-run only. Re-run with --apply to move.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
