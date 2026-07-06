---
title: Hermes Loop Audit — Interim Findings & Fix Plan
type: qa
date: 2026-07-02
confidence: medium
status: audit-incomplete-blocked-on-sudo
source_files: []
system_sources:
  - journalctl -u hermes-agent.service (2026-06-25..2026-07-02)
  - /etc/nixos/hermes.nix
  - /etc/nixos/eden-ops.nix
  - systemctl cat/show hermes-agent.service
  - stat /run/agenix/{meta,telegram,google-api-key}
---

# Hermes Loop Audit — Interim Findings & Fix Plan (2026-07-02)

Audit of EDEN's 4 claimed scheduled loops. Phases 1/3/4 blocked on sudo access to
/persist/eden/hermes/.hermes (job store, mode 700). Findings below are journal- and
config-verified only. EDEN self-reports remain UNTRUSTED.

## Verified findings

1. **Job 1 (Morning SITREP, cron 0 6 * * *)** — DID fire 06:00:42 EDT 2026-07-02
   (local-time cron confirmed; TZ America/New_York). "Successful" is an overclaim:
   - wttr.in weather fetch returned no content; web_search dead
     ("Feature 'search.firecrawl' unavailable: pip install failed")
   - fallback `curl wttr.in` stuck in pending_approval — no user present in cron
   - Farmbrite health check: "No FARMBRITE_API_KEY configured" — all checks ✗
   - execute_code BLOCKED in cron context; sqlite3 not on service PATH
   - ~30× "Session DB append_message failed: 'NoneType' object has no attribute 'execute'"
   → SITREP produced with ZERO working data sources. Any weather/Farmbrite content
   in the delivered report violates the DATA RULE.
2. **Job 2 (social, 10:00)** — no journal entry 09:58–10:08 (WARNING+ only logged,
   so inconclusive). 10:19: EDEN attempted `cat /run/agenix/meta | head -c 100`.
3. **Job 3 (Sunday 03:00 graphify)** — no journal activity in window; consistent
   with "never run". claude = /run/current-system/sw/bin/claude v2.1.187; hermes-user
   auth state unverified.
4. **Job 4 (one-shot 20:30 today)** — pending; existence unverified.
5. **Secrets wiring broken**: hermes.nix declares environmentFiles=[google-api-key,
   telegram, meta] but running unit has NO EnvironmentFile= directives
   (systemctl show -p EnvironmentFiles empty; unit restarted 00:23 after rebuild).
   Telegram works anyway → token sourced elsewhere (likely .hermes/.env).
   /run/agenix/meta is hermes:hermes 400; telegram + google-api-key are root:root 400.
6. Job IDs 45628740efd5 / aa64e1ca6056 / 5f18eeeb1693 / af6bbec4b8e8 appear NOWHERE
   in 7 days of journal.
7. **Meta token access timeline (journal)** — past FB posting did NOT use the declared
   env wiring: Jun 29 21:58 read of /run/secrets/meta_page_access_token → no such file;
   Jun 29 21:59 `cat /run/agenix/meta` → Permission denied (pre-owner-fix);
   Jul 1 17:44 rebuild makes meta hermes-readable; Jul 2 10:19 retry had malformed
   tool args (sanitized to empty). Proven post therefore predates the wiring or ran
   interactively with operator approval. Works-interactively ≠ works-headless: cron
   terminal commands hit pending_approval (proven 06:01 Jul 2). Journal is WARNING+
   only — successful posts leave no trace; run-history store needed for full picture.
   Step-2 note: if meta.age is a bare token (EDEN cats it), it must be converted to
   KEY=value format before use as systemd EnvironmentFile (check via
   `sudo grep -cE '^[A-Z_]+=' /run/agenix/meta`, never print the value).

## Ground-truth map (from world-readable Hermes 0.17.0 source in /nix/store)

All under /persist/eden/hermes/.hermes/ (sudo required):
- `cron/jobs.json` — job defs: id, name, schedule, enabled/state, deliver targets,
  skills, script, workdir, PLUS last_run_at / last_status / last_error /
  last_delivery_error (cron/jobs.py:66,1001-1002,1243-1244)
- `cron/output/{job_id}/{timestamp}.md` — full text of every run's output
  (cron/jobs.py:5,87) — the actual delivered SITREP lives here
- `cron/ticker_heartbeat`, `cron/ticker_last_success` — scheduler heartbeat files
- `logs/agent.log` (INFO+, catch-all), `logs/gateway.log` (INFO+) — rotating,
  redacting (hermes_logging.py:5-22); journal only gets WARNING+
- CLI: `hermes cron list` prints schedule/state/last-run/delivery-error per job

Scheduler facts (source-verified): gateway ticks every 60s; file lock
cron/.tick.lock prevents overlapping ticks; env-mutating jobs run on a
1-worker sequential pool (scheduler.py:8,321-331). FAILED jobs DO deliver
"⚠️ Cron '<name>' failed: ..." to chat (scheduler.py:49-101) — but tool
failures inside an agent run that still returns text count as SUCCESS, so
degraded/fabricated output delivers silently. Assembled prompts pass an
injection scanner before execution.

## Fix plan (ordered, one change at a time)

0. Audit access: operator runs sudo reads via `!`, or add
   `security.sudo.extraConfig = "Defaults timestamp_type=global";` to eden-ops.nix.
1. FINISH AUDIT before any fix — job definitions never yet seen verbatim.
2. Secrets root cause: add explicit
   `systemd.services.hermes-agent.serviceConfig.EnvironmentFile = [ ...agenix paths ]`
   to hermes.nix; rebuild; verify show -p EnvironmentFiles non-empty; dedupe
   .hermes/.env token.
3. SITREP data: (a) new agenix secret farmbrite.age (FARMBRITE_API_KEY), wire into
   EnvironmentFile list; (b) weather — allowlist exact wttr.in curl in Hermes
   approval config (runtime pip is permanently broken on immutable Nix env).
4. DATA RULE into job-1 prompt: source fails → "SOURCE UNAVAILABLE" + operator
   failure notice; never substitute. Add pkgs.sqlite to hermes-agent service path.
5. THE RULE: pause jobs 2+3 until job 1 proves N consecutive clean SITREPs.
   Decide job 4 before 20:30 today — Meta token not in gateway env yet.
6. Diagnose session-DB append failures (.hermes) — run history is being lost,
   making all EDEN self-reports structurally unverifiable.
