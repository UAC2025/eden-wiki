# OFFICER FALLBACK DIRECTIVE v2 — finish the rollout (proof already PASSED)

EDEN — Commander-authorized project (this message is your Scope-Doctrine "go"). Execute NOW via the six-step loop; do not defer to cron. BLUF reports throughout.

## STATUS — what the Commander and Claude already completed (2026-07-06)
- **Nous Portal login: DONE.** Device-code OAuth credential in the gateway pool AND imported into the `s6_comms` profile (shared store: `.hermes/shared/nous_auth.json`).
- **Officer ledger: LIVE** at `workspace/ledgers/officers.jsonl` — 3 entries (2 honest FAILs, 1 PASS). Schema: OFFICER_LEDGER.md.
- **S6 proof loop: PASSED** on `deepseek/deepseek-v4-pro` via `nous` — session `20260706_155253_852c1f`, 35 real tool calls, vault-sourced publish-gated draft at `workspace/doctrine/officers/S6_Comms/run/2026-07-06_arapawa-conservation-draft.md`.
- **Ruling: `nousresearch/hermes-4-405b` is DISQUALIFIED as an officer brain** (two fabrication failures, sessions `20260706_153742_063b14`, `20260706_154903_21dd64`). Officer fallback brain = `deepseek/deepseek-v4-pro` via `nous`.
- Doctrine (PROPOSED, follow but do NOT merge — merging is my adjudication): branch `draft/anthropic-fallback-2026-07-06` — PROVIDER_POLICY, OFFICER_LEDGER, Officer-Skill-Manifest, six PLAYBOOK Model-policy lines.

## Ground rules — non-negotiable
1. **NO FABRICATION.** Every claim cites a session id, file path, or command output. "I could not verify X, so I stopped" is always a correct report.
2. **Credential Doctrine:** the nous login already exists — no other credential actions, no key hunting.
3. **Never delete skills** — quarantine only (reversible `mv`), exactly per the manifest. ADJUDICATE items stay until I rule.
4. **My gates stand:** no money, no purchases, no publishing without my approval, no NixOS changes (propose diffs and WAIT), no new services.
5. **Command-shape gotchas (verified 2026-07-06):** one-shot prompts go via `chat -q`; a profile loads ONLY via the top-level `--profile` flag (HERMES_PROFILE env does nothing); each profile has its own auth store — import nous via `--profile <p> auth add nous --type oauth` (auto-imports from the shared store).

## Phase A — flip the staff to the fallback brain
For each officer profile (`s1_personnel` … `s6_comms`), in `profiles/<p>/config.yaml`: back up the file (timestamped copy beside it), then set `model.default: deepseek/deepseek-v4-pro`, `model.provider: nous`, and import the shared nous credential into that profile's auth store. Verify by re-reading each config. Log ONE ledger `flip` event citing the files changed. (The Commander may already have run `/home/eden/eden-ops/officer-fallback/flip_officer_models.py` — if configs already show nous/deepseek, verify + log and move on.)

## Phase B — fix the gateway default model (standing known-risk)
The gateway default is still depleted `gemini-3.1-pro-preview`: any cron that doesn't override its model is born dead. Set the gateway default to `gpt-5.5` / `openai-codex` (primary brain per PROVIDER_POLICY ruling 1) and cite the config-version bump. Hermes config change, not NixOS — authorized.

## Phase C — S6 skill trim + re-drill
Per Officer-Skill-Manifest: quarantine S6's off-list skills into `profiles/s6_comms/skills-quarantine-2026-07-06/`, then re-run the S6 proof drill on the trimmed profile (same PASS criteria: >0 tool calls, real ledger tick, DATA-RULE clean, real shop work). On PASS, trim the other five officers, one at a time, one ledger line each. On FAIL, restore from quarantine and report.

## Phase D — standup synthesis
Wire the daily standup per OFFICER_LEDGER doctrine: the `officer-standup` cron reads the last 24 h of ledger lines and writes ONE narrative synthesis page per day to `wiki/operations/Officer-Standups/` citing the ledger. No raw ticks in the vault (TELEMETRY_POLICY). Propose the cron entry; do not register it until the trimmed-S6 re-drill has passed.

## Final report + learning
1. BLUF table: phase · done Y/N · evidence (session ids, paths, config versions) · blockers.
2. What remains for ME, one line each (adjudicate ADJUDICATE skills; merge the doctrine branch; approve/reject the Arapawa draft; flip-back timing when the OpenAI quota resets ~2026-07-08).
3. Propose (do not push) wiki page updates for my adjudication.
4. Save durable lessons to memory and update the `officer-standup` skill (or create `provider-fallback`) with the proven flip/import/proof procedure — the loop is not closed without the write-back.
