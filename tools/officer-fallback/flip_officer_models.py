#!/usr/bin/env python3
"""Flip the six officer profiles between openai-codex and the Nous Portal.

Usage (needs root or the hermes user — profile configs live under /persist):
    sudo python3 flip_officer_models.py to-nous              # dry-run (default)
    sudo python3 flip_officer_models.py to-nous --apply
    sudo python3 flip_officer_models.py to-nous --model hermes-4-405b --apply
    sudo python3 flip_officer_models.py to-codex --apply

Per PROVIDER_POLICY (2026-07-06): primary = gpt-5.5/openai-codex,
fallback = deepseek/deepseek-v4-pro/nous (Nous Portal; --model overrides if the portal
offers a newer frontier Hermes). Every applied flip appends an `event:flip`
line to the officer ledger if it exists.

The script edits `model.default` / `model.provider` in each profile's
config.yaml via line-level regex (no YAML lib dependency), writes a
timestamped .bak next to each file, and prints a before/after diff.
"""

import argparse
import datetime
import difflib
import json
import re
import shutil
import sys
from pathlib import Path

HERMES_HOME = Path("/persist/eden/hermes/.hermes")
PROFILES = ["s1_personnel", "s2_intel", "s3_operations",
            "s4_logistics", "s5_plans", "s6_comms"]
LEDGER = Path("/persist/eden/hermes/workspace/ledgers/officers.jsonl")

TARGETS = {
    "to-nous": {"default": "deepseek/deepseek-v4-pro", "provider": "nous"},
    "to-codex": {"default": "gpt-5.5", "provider": "openai-codex"},
}


def set_model_keys(text: str, default: str, provider: str) -> str:
    """Set default:/provider: inside the `model:` block; add block if absent."""
    lines = text.splitlines(keepends=True)
    out, in_model, model_indent = [], False, ""
    seen = {"default": False, "provider": False}
    model_block_found = False

    def key_line(key, val):
        return f"{model_indent}  {key}: {val}\n"

    for line in lines:
        stripped = line.rstrip("\n")
        m_top = re.match(r"^(\s*)model\s*:\s*$", stripped)
        if m_top:
            in_model, model_indent, model_block_found = True, m_top.group(1), True
            out.append(line)
            continue
        if in_model:
            # leaving the block: a non-blank line at <= model indent level
            if stripped.strip() and not re.match(rf"^{model_indent}\s+\S", stripped):
                for k, v in (("default", default), ("provider", provider)):
                    if not seen[k]:
                        out.append(key_line(k, v))
                        seen[k] = True
                in_model = False
                out.append(line)
                continue
            m_kv = re.match(r"^(\s+)(default|provider)\s*:\s*(.*)$", stripped)
            if m_kv and m_kv.group(2) in seen:
                k = m_kv.group(2)
                out.append(f"{m_kv.group(1)}{k}: {default if k == 'default' else provider}\n")
                seen[k] = True
                continue
        out.append(line)

    if in_model:  # model: was the last block in the file
        for k, v in (("default", default), ("provider", provider)):
            if not seen[k]:
                out.append(key_line(k, v))
    if not model_block_found:
        out.append(f"\nmodel:\n  default: {default}\n  provider: {provider}\n")
    return "".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("direction", choices=sorted(TARGETS))
    ap.add_argument("--apply", action="store_true",
                    help="write changes (default is dry-run)")
    ap.add_argument("--model", default=None,
                    help="override the target model id (provider unchanged)")
    args = ap.parse_args()
    target = dict(TARGETS[args.direction])
    if args.model:
        target["default"] = args.model
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    failures = 0

    for prof in PROFILES:
        cfg = HERMES_HOME / "profiles" / prof / "config.yaml"
        try:
            if not cfg.exists():
                print(f"[MISS] {cfg} not found — profile layout differs, skipping")
                failures += 1
                continue
            old = cfg.read_text()
        except PermissionError:
            print(f"[DENIED] cannot read {cfg} — run with sudo (profiles are hermes-owned)")
            failures += 1
            continue
        new = set_model_keys(old, target["default"], target["provider"])
        if old == new:
            print(f"[OK]   {prof}: already at {target['provider']}/{target['default']}")
            continue
        diff = "".join(difflib.unified_diff(
            old.splitlines(keepends=True), new.splitlines(keepends=True),
            fromfile=f"{prof}/config.yaml", tofile=f"{prof}/config.yaml (new)"))
        print(diff)
        if args.apply:
            shutil.copy2(cfg, cfg.with_suffix(f".yaml.bak-{stamp}"))
            cfg.write_text(new)
            print(f"[FLIP] {prof} -> {target['provider']}/{target['default']}")

    if args.apply and LEDGER.parent.exists():
        entry = {
            "ts": datetime.datetime.now(datetime.timezone.utc)
                  .strftime("%Y-%m-%dT%H:%M:%SZ"),
            "officer": "eden", "event": "flip", "loop": None, "step": None,
            "outcome": "ok" if failures == 0 else "fail",
            "detail": f"officer profiles flipped {args.direction} "
                      f"({target['provider']}/{target['default']})",
            "evidence": "eden-ops/officer-fallback/flip_officer_models.py",
            "to": None,
        }
        with LEDGER.open("a") as fh:
            fh.write(json.dumps(entry) + "\n")
        print(f"[LEDGER] flip logged to {LEDGER}")

    if not args.apply:
        print("\nDry-run only. Re-run with --apply to write. "
              "Restart is NOT required — profiles are read per-session.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
