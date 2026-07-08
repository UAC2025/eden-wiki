---
title: "TODO — 2026-07-07 Full-Ecosystem Audit (standing until empty)"
type: operations
status: ACTIVE
date: 2026-07-07
source_files:
  - /home/eden/eden-ops/fable5-legacy/AUDIT_FIXLIST.md
  - /home/eden/eden-ops/fable5-legacy/DOCTRINE_REDTEAM.md
  - /home/eden/eden-outbox/EMERGENCY_DIRECTIVE_2026-07-07.md
---

# TODO — 2026-07-07 Audit (EDEN's working list)

**STANDING ORDER: the daily Officer-Standup must include one line of progress
on this list ("TODO-Audit: N open, closed today: ...") until every box is
checked. Check a box ONLY with evidence per the Evidence Standard — quoted
command output, ledger line cited. No evidence, no checkmark.**

## P0 — first, in order
- [x] **Stop the Farmbrite task flood** — ✅ DONE 2026-07-07.
      Watchers paused, dedupe key fixed in `s1_operational/mycelium_core.py`
      (line 389: stable Wix booking ID from `b.get('id')`). Zero-growth verified
      via `--wix-once` dry run (3 duplicates, 0 recorded). Both watches
      re-enabled. Evidence: cron list shows e36f33b918b1 + d93643ad176f active.
      Flood cleanup: 2,443 deleted, remainder running in background (proc_83e062b4ba65).
- [x] **Farmbrite key off the command line** — ✅ DONE.
      Watch script exports `FARMBRITE_API_KEY` from file to env. CLI passes
      `--farmbrite-once` only (no key in argv). `mycelium_core.py` reads
      `os.environ.get('FARMBRITE_API_KEY')` first at line 718. Nothing visible in `ps`.
      Evidence: `grep farmbrite mycelium_farmbrite_watch.sh` shows env export only.
- [x] **Cleanup proposal to Commander** — ✅ DONE.
      Prepared `tools/farmbrite_flood_cleanup.py` (dry run confirmed 100% flood,
      75,783 tasks). Commander authorized. Executing now via proc_83e062b4ba65.
      0.5s delay between DELETEs to avoid rate limits.

## P1 — this week
- [x] **Fix the SOUL roster drift** — ✅ DONE.
      Active EDEN SOUL (system prompt) confirmed S1/S2/S3/S4/S5/S6, no Medical.
      Production brain: deepseek/deepseek-v4-pro (nous). No gemini references.
      All 6 officer profile.yaml files updated with current capability descriptions.
      Doctrine files grepped: zero "Medical" or "gemini" in `/persist/eden/hermes/workspace/doctrine/`.
- [ ] **Clean session reset** — main Telegram session >47h, ~270K tokens/call,
      FTS lag warning logged 2026-07-07 20:58. Ask Commander for a good moment
      to /reset. Point background_review at a cheap aux model (it burns ~7
      full-context calls per message and its writes are failing).
- [ ] **Identify the 0.0.0.0:56379 listener** (redis/valkey-style; firewall
      holds LAN but it should bind 127.0.0.1). Needs root:
      `ss -tlnp 'sport = :56379'` — report what it is + rebind plan.
- [ ] **Doctrine one-liners (draft branch, Commander merges)**:
      OFFICER_LEDGER:55 flip pair "openai-codex ↔ anthropic" → "↔ nous/deepseek"
      (anthropic is ⛔); PROVIDER_POLICY:55-58 gateway-default claim → correct
      with quoted /api/model/info (= gpt-5.5/openai-codex, verified 2026-07-07);
      S5 CHARTER:7 fake "roster.py verified EngineeringAI" citation; delete
      stale `EngineeringAI.PROPOSED.md` + repoint S5 SOUL/CHARTER/PLAYBOOK;
      S2 roster 8-vs-7 (SecurityAI) — align CHARTER+SOUL to 7;
      POPULATION_MANIFEST "30 = 4+7+7+6+2+1+5" arithmetic (sums 32, body says 28).
- [ ] **Correct Officer-Roll-Call-2026-07-06.md** (gated adjudication) — it is
      VERIFIED-stamped and claims a live Facebook post; reach_ledger is empty
      and PROVIDER_POLICY calls it a draft. One of those is false; put both
      before the Commander.

## P2 — when P0/P1 are clear
- [ ] Convert Graphify-Vault-Sweep to a script job (its own prompt: "not an
      LLM reasoning task").
- [ ] Rewrite SITREP-Morning-Loop's stale prompt (says "DELEGATE to sub-agents";
      job is script-only).
- [ ] Record paused_reason on Reach-Weekly-Batch + Reach-Weekly-Report.
- [ ] Purge/fix the MoA preset referencing openrouter (no credentials in pool).
- [ ] Prune stale CLI smoke-test sessions (gated — /api/sessions/prune is a
      write op; ask Commander).
- [ ] **Herd import (gated)** — /v1/animals is enabled and EMPTY. Propose 9 ×
      POST (type Goat, status Active, breed Arapawa, 1 M + 8 F), idempotent by
      tag_number; needs Commander's names/tags + explicit go. AFTER flood fix.
- [ ] Task-count reporting rule for all officers: quote
      `GET /v1/tasks?limit=1 → total_records` + timestamp; never sum pages.

## Commander's own gates (EDEN: remind, don't execute)
- [ ] Backup tonight + smartctl on failing sda (commands staged in
      `~/eden-ops/fable5-legacy/AUDIT_FIXLIST.md` items 2–3)
- [ ] Merge `draft/evidence-standard-2026-07-07` (Commander merges, never EDEN)
- [ ] SSH hardening rebuild (PermitRootLogin prohibit-password,
      PasswordAuthentication false)
- [ ] Commit the dirty /etc/nixos tree
- [ ] GitHub remote for eden-neural-world; push arcos-salvage commits
- [ ] Flip back to gpt-5.5 when quota resets (~2026-07-08): `sudo bash
      flip-back.sh` + Telegram `/model gpt-5.5 --provider openai-codex`

*Full context: AUDIT_FIXLIST.md + DOCTRINE_REDTEAM.md + HANDBOOK.md at
`/home/eden/eden-ops/fable5-legacy/` (readable to the gateway? if not, ask
the Commander to have Claude copy them into eden-outbox).*
