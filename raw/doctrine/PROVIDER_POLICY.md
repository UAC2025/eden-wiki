---
title: Provider & Model Policy — verified state and fallback order
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
source_files: []
system_sources:
  - dashboard API /api/sessions model history, verified 2026-07-06
  - EDEN provider-failure report during S6 verification drill, 2026-07-06
---

# Provider & Model Policy (as verified 2026-07-06)

## Verified provider state

| Provider / model | State (2026-07-06) | Evidence |
|---|---|---|
| `openai-codex` / **gpt-5.5** | ✅ WORKING — current brain | ran EDEN's officer-standup session (173 msgs) and the S6 verification drill |
| `openai-codex` / gpt-5.4-mini | ✅ worked 2026-07-02 | session history |
| deepseek/deepseek-v4-pro | ✅ worked 2026-07-04 | session history |
| google / gemini-3.1-pro-preview | ⛔ DEPLETED — prepayment credits exhausted (HTTP 429) | drill failure + cron sessions doing zero tool work |
| anthropic / claude-fable-5 | ⛔ dashboard credential exhausted | EDEN drill report |
| nous | ⛔ no access token configured | EDEN drill report |
| openrouter | ⛔ empty API key | EDEN drill report |

## Policy (Commander rulings 2026-07-06)

1. **Current production brain: `gpt-5.5` via `openai-codex`** — for EDEN and
   all officer profiles — until Gemini is refunded. Officer profiles must set
   this explicitly; never inherit the depleted default silently.
2. Fallback for drills and loops: `gpt-5.4-mini` (same account), then report.
3. Existing configured credentials only — no new keys, no credential hunting
   (Credential Doctrine).
4. Delegated parent children may run cheaper models; officer synthesis stays
   on the frontier model.
5. When Gemini (or another frontier provider) is funded, the swap is a config
   change + a one-line update to this file and each officer PLAYBOOK's Model
   policy section. Update this file in the same commit as the config change.

## Known risk

The **gateway default model is still `gemini-3.1-pro-preview`** (verified via
/api/config 2026-07-06): any session or cron that does not override the model
is born on a depleted provider. The loop watchdog (`/home/eden/eden-ops/`)
flags cron runs that do zero tool work — the signature of this failure.
