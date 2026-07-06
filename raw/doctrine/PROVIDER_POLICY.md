---
title: Provider & Model Policy — verified state and fallback order
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
updated: 2026-07-06 (Commander directive — Nous Portal adopted as officer fallback; Anthropic route declined)
source_files: []
system_sources:
  - dashboard API /api/sessions model history, verified 2026-07-06
  - EDEN provider-failure report during S6 verification drill, 2026-07-06
  - hermes-agent 0.18.0 provider registry source audit (plugins/model-providers/nous/, anthropic/), 2026-07-06
---

# Provider & Model Policy (as verified 2026-07-06)

## Verified provider state

| Provider / model | State (2026-07-06) | Evidence |
|---|---|---|
| `openai-codex` / **gpt-5.5** | ⚠️ WORKING but RATE-LIMITED ~53h (ChatGPT Plus quota) | officer roll-call blocked 2026-07-06 |
| `openai-codex` / gpt-5.4-mini | ⚠️ same account as gpt-5.5 — shares the exhausted quota; **not a real fallback** | provider audit 2026-07-06 |
| `nous` (Nous Portal) | ✅ LOGGED IN (device-code OAuth, 2026-07-06) — portal serves 267 models via /v1/models; frontier Hermes = `nousresearch/hermes-4-405b`. ⚠️ plugin's built-in chain still names stale hermes-3 IDs that 404 | login verified + live /v1/models query 2026-07-06 |
| deepseek/deepseek-v4-pro | ✅ worked 2026-07-04 | session history |
| google / gemini-3.1-pro-preview | ⛔ DEPLETED — prepayment credits exhausted (HTTP 429) | drill failure + cron sessions doing zero tool work |
| anthropic | ⛔ DECLINED as route — Commander's Anthropic subscription covers claude.ai/Claude Code surfaces only; gateway use would need separate API billing (prior dashboard credential exhausted) | Commander ruling 2026-07-06 |
| openrouter | ⛔ empty API key | EDEN drill report |

## Policy (Commander rulings 2026-07-06, amended same day)

1. **Current production brain: `gpt-5.5` via `openai-codex`** — for EDEN and
   all officer profiles — until Gemini is refunded. Officer profiles must set
   this explicitly; never inherit the depleted default silently.
2. **Officer fallback brain: `deepseek/deepseek-v4-pro` via the Nous
   Portal (`nous` provider)** — proven in the S6 proof loop 2026-07-06
   (session `20260706_155253_852c1f`, PASS). `nousresearch/hermes-4-405b`
   is DISQUALIFIED as an officer brain (two fabrication failures, see Known
   risk 3). Do NOT rely on the plugin's built-in degradation chain — it
   still names stale hermes-3 ids that 404. Every flip
   to/from the fallback is logged in the officer ledger (OFFICER_LEDGER
   doctrine). `gpt-5.4-mini` is demoted from fallback duty — it rides the
   same rate-limited account and fails together with gpt-5.5.
3. **Credential Doctrine amendment (this ruling):** connecting the
   Commander's existing Nous Portal subscription via the provider's
   device-code OAuth login (`hermes auth add nous`) is authorized. This is
   an existing credential, not a new key — no raw API keys are minted or
   stored by hand. No other new credentials; no credential hunting.
4. Delegated parent children may run cheaper models (e.g. `hermes-3-70b`);
   officer synthesis stays on the frontier model.
5. When Gemini (or another frontier provider) is funded, the swap is a config
   change + a one-line update to this file and each officer PLAYBOOK's Model
   policy section. Update this file in the same commit as the config change.

## Known risks

1. The **gateway default model is still `gemini-3.1-pro-preview`** (verified
   via /api/config 2026-07-06): any session or cron that does not override
   the model is born on a depleted provider. Fix: set the gateway default to
   `gpt-5.5`/`openai-codex` in the same pass that connects the Nous login
   (see `/home/eden/eden-ops/officer-fallback/RUNBOOK.md`).
2. Hermes 0.18.0 has **no cross-provider automatic fallback** at the profile
   level (`fallback_models` chains exist only inside a provider). The
   codex→nous fallback is therefore an **operational flip** — a scripted
   config change triggered by the operator or flagged by the loop watchdog
   when openai-codex 429s — not an automatic in-request retry. Flip scripts:
   `/home/eden/eden-ops/officer-fallback/`.
3. Officer capability on Hermes-family models is UNPROVEN — the S6 proof
   loop (GO/NO-GO board) must pass on the nous brain before any officer
   loop is trusted on it. Watch especially tool-calling fidelity and
   DATA-RULE compliance in the proof drill.
   **Proof run 1 (session `20260706_153742_063b14`): FAIL** — 0 tool
   calls, fabricated dispatch/ledger claims (harness fault contributed: the
   s6_comms profile never loaded; profile selection is the top-level
   `--profile` flag, not the HERMES_PROFILE env var).
   **Proof run 2 (session `20260706_154903_21dd64`, hermes-4-405b, profile
   + full toolkit loaded): FAIL — DISQUALIFIED.** 0 tool calls; printed a
   write_file call as prose and claimed "Logged" while the ledger was
   unchanged; did honor BLOCKED on the empty dispatch queue.
   **Proof run 3 (session `20260706_155253_852c1f`,
   deepseek/deepseek-v4-pro): PASS.** 35 real tool calls; vault-sourced,
   quality-gated, publish-gated Facebook draft produced at
   `workspace/doctrine/officers/S6_Comms/run/2026-07-06_arapawa-conservation-draft.md`;
   honest BLOCKED reports (fal image gen, no Google Drive); real ledger
   loop_tick appended, outcome self-graded "partial". Minor caveat: its
   ledger detail undercounted its own tool calls (said 8; harness counted
   35) — an undercount of real work, not fabrication. deepseek-v4-pro is
   the proven officer fallback brain; hermes-4-405b may still serve
   NON-officer, non-ledger duties at Commander discretion only.
