---
title: Provider & Model Policy — verified state and fallback order
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
updated: 2026-07-06 (Commander directive — Anthropic claude-opus-4-8 adopted as officer fallback)
source_files: []
system_sources:
  - dashboard API /api/sessions model history, verified 2026-07-06
  - EDEN provider-failure report during S6 verification drill, 2026-07-06
  - hermes-agent 0.18.0 provider registry source audit (plugins/model-providers/anthropic/), 2026-07-06
---

# Provider & Model Policy (as verified 2026-07-06)

## Verified provider state

| Provider / model | State (2026-07-06) | Evidence |
|---|---|---|
| `openai-codex` / **gpt-5.5** | ⚠️ WORKING but RATE-LIMITED ~53h (ChatGPT Plus quota) | officer roll-call blocked 2026-07-06 |
| `openai-codex` / gpt-5.4-mini | ⚠️ same account as gpt-5.5 — shares the exhausted quota; **not a real fallback** | provider audit 2026-07-06 |
| deepseek/deepseek-v4-pro | ✅ worked 2026-07-04 | session history |
| google / gemini-3.1-pro-preview | ⛔ DEPLETED — prepayment credits exhausted (HTTP 429) | drill failure + cron sessions doing zero tool work |
| anthropic / claude-opus-4-8 | 🟡 PROVIDER READY, CREDENTIAL PENDING — native Hermes provider verified in 0.18.0 source; prior dashboard credential exhausted; needs funded `ANTHROPIC_API_KEY` | source audit + EDEN drill report |
| nous | ⛔ no access token configured | EDEN drill report |
| openrouter | ⛔ empty API key | EDEN drill report |

## Policy (Commander rulings 2026-07-06, amended same day)

1. **Current production brain: `gpt-5.5` via `openai-codex`** — for EDEN and
   all officer profiles — until Gemini is refunded. Officer profiles must set
   this explicitly; never inherit the depleted default silently.
2. **Officer fallback brain: `claude-opus-4-8` via `anthropic`** (Commander
   directive 2026-07-06). Used when `openai-codex` fails or is rate-limited.
   Every flip to/from the fallback is logged in the officer ledger
   (see OFFICER_LEDGER doctrine). `gpt-5.4-mini` is demoted from fallback
   duty — it rides the same rate-limited account and fails together with
   gpt-5.5.
3. **Credential Doctrine amendment (this ruling):** one new funded Anthropic
   API key is authorized, installed via `hermes auth add anthropic` into the
   gateway credential pool (`auth.json`). No other new keys; no credential
   hunting. Fable-class models (`claude-fable-5`) are NOT used for officer
   loops — pricing tier and refusal stop-reason semantics are wrong for
   unattended operation; Opus 4.8 is the ceiling for officers.
4. Delegated parent children may run cheaper models (`claude-haiku-4-5` is
   the anthropic aux default); officer synthesis stays on the frontier model.
5. When Gemini (or another frontier provider) is funded, the swap is a config
   change + a one-line update to this file and each officer PLAYBOOK's Model
   policy section. Update this file in the same commit as the config change.

## Known risks

1. The **gateway default model is still `gemini-3.1-pro-preview`** (verified
   via /api/config 2026-07-06): any session or cron that does not override
   the model is born on a depleted provider. Fix: set the gateway default to
   `gpt-5.5`/`openai-codex` in the same pass that installs the Anthropic
   credential (see `/home/eden/eden-ops/officer-fallback/RUNBOOK.md`).
2. Hermes 0.18.0 has **no cross-provider automatic fallback chain** at the
   profile level (per-provider `fallback_models` exists only inside
   aggregator provider plugins). The officer fallback is therefore an
   **operational flip** — a scripted config change triggered by the operator
   or the loop watchdog when openai-codex 429s — not an automatic in-request
   retry. The flip scripts live in `/home/eden/eden-ops/officer-fallback/`.
3. `claude-opus-4-8` requests will fail until the funded key is installed.
   Until then the staff has NO working fallback; treat openai-codex outages
   as full-stop events.
