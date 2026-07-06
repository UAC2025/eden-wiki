# Officer Fallback Kit — 2026-07-06

Backup of the provider-fallback toolkit built the day openai-codex rate-limited
the whole staff and the officers were flipped to `deepseek/deepseek-v4-pro`
via the Nous Portal. Live copies run from `/home/eden/` and
`/home/eden/eden-ops/officer-fallback/`; this is the durable copy.

Doctrine: `raw/doctrine/PROVIDER_POLICY.md`, `raw/doctrine/OFFICER_LEDGER.md`,
`raw/doctrine/officers/Officer-Skill-Manifest-2026-07-06.md` (all merged to
main via ac3b964, ratified post-hoc).

| File | What it does |
|---|---|
| `RUNBOOK.md` | Full operator procedure: nous login, flip, ledger, S6 proof, trim, rollback — including the hard-won CLI gotchas (`chat -q`, top-level `--profile`, per-profile auth stores, HOME/--chdir for sudo runs) |
| `flip_officer_models.py` | Flip all six officer profiles `to-nous` / `to-codex` (`--model X` overrides; dry-run default; timestamped .baks; ledger flip event) |
| `flip-on.sh` / `flip-back.sh` | Short wrappers for the above (terminal line-wrap defense) |
| `give-keys.sh` | Import the shared Nous OAuth credential into each officer profile's own auth store |
| `s6-proof.sh` | The proof-loop harness that disqualified hermes-4-405b (fabrication ×2) and proved deepseek-v4-pro (35 real tool calls) |
| `wake-eden.sh` | RETIRED — kept as documentation: gateway config is NixOS-managed; switch EDEN's model via Telegram `/model <model> --provider <provider>` instead |
| `OFFICER_FALLBACK_PROMPT.md` | The Commander directive (v2) EDEN executed for Phases C/D |

Flip-back when the OpenAI quota resets: `sudo bash flip-on.sh` reverses with
`flip-back.sh`; EDEN herself flips via Telegram `/model gpt-5.5 --provider
openai-codex`. The standup cron stays pinned to deepseek regardless.
