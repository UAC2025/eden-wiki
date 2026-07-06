#!/usr/bin/env python3
"""officer_lint.py — verify an EDEN officer's doctrine artifacts against the
stand-up directive spec (2026-07-06). Stdlib only; no LLM, no network.

Usage:
    python3 officer_lint.py <officer-dir> [--skills skill1,skill2,...]

<officer-dir> must contain CHARTER.md, PLAYBOOK.md, SOUL.md.
--skills: comma-separated list of skills actually installed on the gateway
          (e.g. from `hermes -p <profile> skills list`); any skill named in
          the artifacts but absent from this list is flagged as an unwired claim.

Exit code 0 = PASS, 1 = FAIL, 2 = usage/IO error.
"""
import re
import sys
from pathlib import Path

SOUL_MAX_CHARS = 4500  # spec says <= ~4k; small tolerance

SIX_STEPS = ["observe", "learn", "decide", "act", "adapt", "repeat"]

CHARTER_SECTIONS = {
    "mission":            r"\bmission\b",
    "in-scope":           r"\bin[- ]scope\b",
    "out-of-scope":       r"\bout[- ]of[- ]scope\b",
    "authority":          r"\bauthority\b",
    "c2 seat":            r"\b(c2|chain of command|reports to)\b",
    "parents-on-demand":  r"\bparents?[- ]on[- ]demand\b",
    "kpis":               r"\bkpis?\b",
    "escalation":         r"\bescalat",
    "failure modes":      r"\bfailure modes?\b",
    "data boundaries":    r"\b(data boundar|data access)",
    "anti-fabrication":   r"\b(anti[- ]fabrication|no fabrication|never fabricate)\b",
    "dependencies":       r"\bdependenc",
    "activation":         r"\bactivation\b",
}

PLAYBOOK_SECTIONS = {
    "trigger":            r"\btriggers?\b",
    "preconditions":      r"\bpre[- ]?conditions?\b",
    "in-loop verification": r"\bverif",
    "output artifacts":   r"\boutputs?\b",
    "telemetry":          r"\b(telemetry|logging)\b",
    "idempotency":        r"\bidempoten",
    "recovery":           r"\b(recovery|rollback)\b",
    "model policy":       r"\bmodel policy\b",
    "handoff":            r"\bhand[- ]?off\b",
    "exit criteria":      r"\bexit criteria\b",
    "worked example":     r"\bworked example\b",
}

SOUL_REQUIRED = {
    "inherits EDEN SOUL":  r"\b(inherit|eden soul|soul doctrine)\b",
    "six-step loop":       r"observe.{0,40}learn.{0,40}decide.{0,40}act.{0,40}adapt.{0,40}repeat",
    "parents":             r"\bparents?\b",
    "mission":             r"\bmission\b",
}

# Steps must be concrete: within each step's block we expect at least one
# fenced command, backticked invocation, skill/tool name, file path, or an
# honest BLOCKED tag.
CONCRETE = (r"(```|`[^`]+`|\bskill\b|\bBLOCKED\b|\bdelegate_task\b|\bhermes\b"
            r"|\bcurl\b|\bgit\b|\b[a-z0-9]+(?:-[a-z0-9]+){1,}\b"  # skill-like name
            r"|[\w.-]+/[\w.-]+\.(?:md|log|json|yaml|py|db))")      # file path

# Common prose hyphenations that are not skill names.
HYPHEN_STOPWORDS = {
    "mid-loop", "in-loop", "six-step", "on-demand", "one-shot", "end-to-end",
    "read-only", "standing-ready", "non-negotiable", "re-run", "real-time",
    "cross-shop", "self-check", "act-report", "token-lean", "parents-on-demand",
    "out-of-scope", "in-scope", "anti-fabrication",
}


class Report:
    def __init__(self):
        self.failures, self.warnings, self.passes = [], [], []

    def check(self, ok, label, warn_only=False):
        if ok:
            self.passes.append(label)
        elif warn_only:
            self.warnings.append(label)
        else:
            self.failures.append(label)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def find_sections(text: str, sections: dict, rep: Report, artifact: str):
    low = text.lower()
    for name, pat in sections.items():
        rep.check(re.search(pat, low) is not None, f"{artifact}: section '{name}'")


def check_six_steps(playbook: str, rep: Report):
    low = playbook.lower()
    # Locate each step as a heading or numbered/bold list item, in order.
    positions = []
    for step in SIX_STEPS:
        m = re.search(rf"^\s{{0,6}}(#{{1,6}}|\d+[\.\)]|[-*]|\*\*)\s*.{{0,24}}\b{step}\b",
                      low, re.MULTILINE)
        rep.check(m is not None, f"PLAYBOOK: six-step '{step}' present as a step")
        positions.append(m.start() if m else None)
    known = [p for p in positions if p is not None]
    rep.check(known == sorted(known), "PLAYBOOK: six steps appear in canonical order")
    # Concreteness: text between consecutive step positions must contain a
    # command/tool/BLOCKED marker — a described step is not an executable step.
    for i, step in enumerate(SIX_STEPS[:-1]):  # 'repeat' may be a bare loop arrow
        if positions[i] is None:
            continue
        end = next((p for p in positions[i + 1:] if p is not None), len(playbook))
        block = playbook[positions[i]:end]
        rep.check(re.search(CONCRETE, block, re.IGNORECASE) is not None,
                  f"PLAYBOOK: step '{step}' is concrete (command/skill/BLOCKED), not prose")


def check_unwired_claims(text: str, installed: set, rep: Report, artifact: str):
    if not installed:
        return
    named = set(re.findall(r"\b([a-z0-9]+(?:-[a-z0-9]+)+)\b", text))
    named -= HYPHEN_STOPWORDS
    plausible = {s for s in named if any(
        k in s for k in ("ops", "engine", "api", "processor",
                          "protocol", "dispatch", "content", "social"))}
    for s in sorted(plausible - installed):
        rep.check(False, f"{artifact}: names skill-like '{s}' not in installed list", warn_only=True)


def coherence(charter: str, soul: str, rep: Report):
    def parents(text):
        m = re.search(r"parents?[- ]on[- ]demand.*?(?=\n#|\Z)", text, re.IGNORECASE | re.DOTALL)
        scope = m.group(0) if m else text
        return set(re.findall(r"\b([A-Z][A-Za-z]+AI)\b", scope))
    cp, sp = parents(charter), parents(soul)
    if cp and sp:
        missing = cp - sp
        rep.check(not missing,
                  f"COHERENCE: charter parents missing from soul: {sorted(missing)}",
                  warn_only=True)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    officer_dir = Path(args[0])
    installed = set()
    if "--skills" in args:
        installed = {s.strip() for s in args[args.index("--skills") + 1].split(",") if s.strip()}

    rep = Report()
    files = {}
    for name in ("CHARTER.md", "PLAYBOOK.md", "SOUL.md"):
        p = officer_dir / name
        if not p.is_file():
            rep.check(False, f"{name} exists")
            continue
        rep.check(True, f"{name} exists")
        files[name] = read(p)

    if "SOUL.md" in files:
        soul = files["SOUL.md"]
        rep.check(len(soul) <= SOUL_MAX_CHARS,
                  f"SOUL: token-lean ({len(soul)} chars <= {SOUL_MAX_CHARS})")
        find_sections(soul, SOUL_REQUIRED, rep, "SOUL")
    if "CHARTER.md" in files:
        find_sections(files["CHARTER.md"], CHARTER_SECTIONS, rep, "CHARTER")
        check_unwired_claims(files["CHARTER.md"], installed, rep, "CHARTER")
    if "PLAYBOOK.md" in files:
        find_sections(files["PLAYBOOK.md"], PLAYBOOK_SECTIONS, rep, "PLAYBOOK")
        check_six_steps(files["PLAYBOOK.md"], rep)
        check_unwired_claims(files["PLAYBOOK.md"], installed, rep, "PLAYBOOK")
    if "CHARTER.md" in files and "SOUL.md" in files:
        coherence(files["CHARTER.md"], files["SOUL.md"], rep)

    print(f"== officer_lint: {officer_dir} ==")
    for f in rep.failures:
        print(f"FAIL  {f}")
    for w in rep.warnings:
        print(f"WARN  {w}")
    print(f"-- {len(rep.passes)} passed, {len(rep.warnings)} warnings, "
          f"{len(rep.failures)} failures --")
    print("VERDICT:", "PASS" if not rep.failures else "FAIL")
    return 0 if not rep.failures else 1


if __name__ == "__main__":
    sys.exit(main())
