# Officer Fallback Runbook — Nous Portal (deepseek/deepseek-v4-pro)

Implements EDEN's roll-call recommendations + Commander directive 2026-07-06
(Nous Portal subscription as the officer fallback; Anthropic route declined).
Doctrine: `eden-wiki/raw/doctrine/PROVIDER_POLICY.md`
(branch `draft/anthropic-fallback-2026-07-06`).

Everything under `/persist/eden/hermes/` is owned by the `hermes` user and
needs sudo (interactive password). Run phases in order. Each phase is
independently verifiable and reversible.

---

## Phase 0 — Connect the Nous Portal login + fix gateway default

**0.1 — Device-code OAuth login with the Commander's portal subscription**
(interactive: it prints a URL + code; log in with the portal account):

```sh
sudo -u hermes env HERMES_HOME=/persist/eden/hermes/.hermes \
  /run/current-system/sw/bin/hermes auth add nous
```

Verify: `sudo -u hermes env HERMES_HOME=/persist/eden/hermes/.hermes \
  /run/current-system/sw/bin/hermes auth list nous`

(Non-interactive alternative: the provider also reads `NOUS_API_KEY` from the
gateway environment — only if the portal issues one; the OAuth login is the
primary path.)

**0.2 — Check what the portal actually serves** and note the frontier Hermes
model. `deepseek/deepseek-v4-pro` is the portal-verified frontier (2026-07-06,
via /v1/models — 267 models served); if a newer frontier Hermes appears, use
the flip script's `--model` flag and update PROVIDER_POLICY ruling #2 in the
same pass:

```sh
sudo -u hermes env HERMES_HOME=/persist/eden/hermes/.hermes \
  /run/current-system/sw/bin/hermes model
```

**0.3 — Fix the depleted gateway default model** (PROVIDER_POLICY known risk
#1 — crons that don't override the model are born on dead Gemini):

```sh
sudo -u hermes env HERMES_HOME=/persist/eden/hermes/.hermes \
  /run/current-system/sw/bin/hermes config set model.default gpt-5.5
sudo -u hermes env HERMES_HOME=/persist/eden/hermes/.hermes \
  /run/current-system/sw/bin/hermes config set model.provider openai-codex
```

**0.4 — Restart the gateway** (drain-safe; check `gateway_busy:false` on
`curl -s http://127.0.0.1:9118/api/status` first):

```sh
sudo systemctl restart hermes-agent.service
```

**0.5 — Smoke-test the nous provider** (one-shot, no officer involved):

```sh
sudo -u hermes env --chdir=/persist/eden/hermes/workspace HOME=/persist/eden/hermes \
  HERMES_HOME=/persist/eden/hermes/.hermes \
  /run/current-system/sw/bin/hermes chat -m deepseek/deepseek-v4-pro --provider nous \
  -q "Reply with the single word: alive"
```

---

## Phase 1 — Officer fallback flip (when openai-codex is down/rate-limited)

Dry-run first, then apply:

```sh
sudo python3 /home/eden/eden-ops/officer-fallback/flip_officer_models.py to-nous
sudo python3 /home/eden/eden-ops/officer-fallback/flip_officer_models.py to-nous --apply
# newer frontier Hermes on the portal? add: --model <model-id>
```

Flip back when the OpenAI quota resets:

```sh
sudo python3 /home/eden/eden-ops/officer-fallback/flip_officer_models.py to-codex --apply
```

- Timestamped `.bak` written next to each config; ledger `flip` event logged.
- Hermes 0.18.0 has no cross-provider auto-fallback — this flip IS the
  fallback mechanism. NOTE: the nous plugin's built-in degradation chain
  still names stale hermes-3 IDs that 404 on the portal — do NOT rely on
  automatic within-provider fallback until hermes-agent updates it.
- Candidate automation (later, after proof): the loop watchdog
  (`/home/eden/eden-ops/loop_watchdog.py`) detects zero-tool-work runs;
  wiring it to suggest (not run) the flip is a separate adjudication.

---

## Phase 2 — Ledger bootstrap (before the S6 proof run)

```sh
sudo -u hermes mkdir -p /persist/eden/hermes/workspace/ledgers
sudo -u hermes touch /persist/eden/hermes/workspace/ledgers/officers.jsonl
```

Schema + rules: `eden-wiki/raw/doctrine/OFFICER_LEDGER.md` (PROPOSED).

---

## Phase 3 — S6 proof loop (one officer end-to-end before scaling six)

S6 is the proof officer (only one already verified live, per the stand-up
audit). Run its loop once on the fallback brain:

```sh
sudo -u hermes env --chdir=/persist/eden/hermes/workspace HOME=/persist/eden/hermes \
  HERMES_HOME=/persist/eden/hermes/.hermes \
  /run/current-system/sw/bin/hermes --profile s6_comms chat \
  -m deepseek/deepseek-v4-pro --provider nous \
  -q "Run one full six-step loop of your primary dispatch duty. Every Act step must be a real tool call; if a tool or credential is unavailable report BLOCKED and stop — never describe work you did not perform. Append a loop_tick line to workspace/ledgers/officers.jsonl at adapt via a real file write, citing evidence. Report BLUF."

Command-shape gotchas (learned 2026-07-06, session evidence in
/home/eden/s6-proof-output.txt): the prompt MUST go via `-q` (positional
prompts are rejected); the profile MUST go via the top-level `--profile`
flag (the HERMES_PROFILE env var does NOT select a profile); `HOME` and
`--chdir` must point into /persist or agent init dies on /home/eden perms.
```

**PASS criteria (all four):**
1. Session completes with >0 tool calls (dashboard `/api/sessions` —
   zero-tool-work is the dead-provider signature). Officer capability on
   Hermes-family models is unproven — watch tool-calling fidelity closely.
2. One `loop_tick` line appended to the ledger with a real `evidence` path.
3. Output is DATA-RULE clean (no fabricated observational claims).
4. Watchdog tick shows the session
   (`/home/eden/eden-ops/ledger.jsonl`).

On PASS: apply the skill trim to S6 only
(`sudo python3 trim_officer_skills.py --apply s6_comms`), re-run the same
drill on the trimmed profile, then roll trim + ledger duty to the other
five per the GO/NO-GO board. On FAIL: flip S6 back
(`to-codex`), attach the session id to the ledger as `outcome:fail`, and
stop — do not scale.

---

## Phase 4 — Skill trim (rest of the staff, post-proof)

```sh
sudo python3 /home/eden/eden-ops/officer-fallback/trim_officer_skills.py            # dry-run all
sudo python3 /home/eden/eden-ops/officer-fallback/trim_officer_skills.py --apply    # quarantine
```

Keep-lists: `raw/doctrine/officers/Officer-Skill-Manifest-2026-07-06.md`.
Quarantine is reversible (`mv` back from `skills-quarantine-2026-07-06/`).
`--strict` also quarantines ADJUDICATE items — only after the Commander
rules on them.

---

## Rollback summary

| Change | Undo |
|---|---|
| Officer flip | `flip_officer_models.py to-codex --apply` (or restore `.bak-*`) |
| Skill trim | `mv` skills back out of `skills-quarantine-2026-07-06/` |
| Gateway default | `hermes config set model.default gemini-3.1-pro-preview` (don't) |
| Credential | `hermes auth remove nous <idx>` |
| Doctrine | branch `draft/anthropic-fallback-2026-07-06` — merge = adjudicate, delete = reject |
