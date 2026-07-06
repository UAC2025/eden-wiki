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
| `nous` (Nous Portal) | 🟡 PROVIDER READY, LOGIN PENDING — native provider, device-code OAuth (`hermes auth add nous`), Commander holds a portal subscription; built-in model chain hermes-3-405b → hermes-3-70b | 0.18.0 source audit |
| deepseek/deepseek-v4-pro | ✅ worked 2026-07-04 | session history |
| google / gemini-3.1-pro-preview | ⛔ DEPLETED — prepayment credits exhausted (HTTP 429) | drill failure + cron sessions doing zero tool work |
| anthropic | ⛔ DECLINED as route — Commander's Anthropic subscription covers claude.ai/Claude Code surfaces only; gateway use would need separate API billing (prior dashboard credential exhausted) | Commander ruling 2026-07-06 |
| openrouter | ⛔ empty API key | EDEN drill report |

## Policy (Commander rulings 2026-07-06, amended same day)

1. **Current production brain: `gpt-5.5` via `openai-codex`** — for EDEN and
   all officer profiles — until Gemini is refunded. Officer profiles must set
   this explicitly; never inherit the depleted default silently.
2. **Officer fallback brain: Nous Portal (`nous` provider)** — Commander
   directive 2026-07-06. Default fallback model `hermes-3-405b` (the largest
   Hermes verified in the provider source); after portal login, verify the
   live model list and promote the newest frontier Hermes if one is offered —
   that promotion is a one-line update here + the flip-script `--model` flag.
   The nous provider carries its own built-in chain (hermes-3-405b →
   hermes-3-70b), so within-provider degradation is automatic. Every flip
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
