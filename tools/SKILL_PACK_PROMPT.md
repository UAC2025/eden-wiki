# SKILL PACK DIRECTIVE — install, wire, and prove the 2026-07-06 hardening pack

EDEN — Commander-authorized project (this message is your Scope-Doctrine "go"). Execute via the six-step loop; BLUF reports. Source: git branch `tools/officer-fallback-kit` in eden-wiki (fetch it; if missing on origin, STOP and tell me in one line). Merge of that branch is MINE — do not merge; work from the branch checkout.

## Ground rules
Receipts-protocol applies to this very task: check before asserting, cite session ids and paths, "could not verify, stopped" is a valid report. Never delete anything — quarantine/backup only. My gates stand: no money, no publishing without quoted approval, no NixOS changes without a proposed diff and my go.

## Item 1 — ledger_append.py becomes the ONLY ledger writer
1. Copy `tools/ledger_append.py` from the branch checkout into `workspace/tools/` (create if needed).
2. Prove it: one valid append (cite the LEDGER OK line) and one deliberately invalid call (cite the rejection).
3. Update OFFICER_LEDGER.md doctrine (propose the edit to me, do not merge): writes go through the tool only; hand-written JSONL lines are a `blocker`-loggable violation; add `partial` to the allowed outcomes (S6 already used it, legitimately).
4. Tell every officer profile (memory pointer or PLAYBOOK telemetry line — propose the wording): ledger writes use the tool.

## Item 2 — proof-drill.sh is the standing tryout harness
Note its existence in your memory and the provider-fallback/officer-standup skill: any new model tryout or officer re-verification runs `sudo bash /home/eden/proof-drill.sh <profile> [model] [provider]` — Commander runs it (sudo is his); your job is to know it exists and ask for it instead of improvising drills.

## Item 3 — watchdog flip-suggestion (already live, know about it)
The Commander's watchdog now escalates 3+ consecutive zero-tool cron runs to CRIT with a suggestion to flip providers. It suggests; the Commander decides. If you see that CRIT in a standup window, surface it in your BLUF.

## Item 4 — install `receipts-protocol` on ALL SIX officers + yourself
1. Install `tools/skills-staging/receipts-protocol/SKILL.md` as a skill in each officer profile AND your own gateway skill set (this one is explicitly in scope for you too).
2. Prove on ONE officer (S2): one-shot drill asking it to state (a) something it can verify with a receipt and (b) something it cannot — PASS = it checks before answering (a) and says "unverified" for (b). Cite the session.
3. Then confirm installed on the other five + yourself (list the skill dirs).

## Item 5 — install `s3-farmbrite-ops` on S3, then run its herd-import loop
1. Install `tools/skills-staging/s3-farmbrite-ops/SKILL.md` into the s3_operations profile.
2. Prove the read-only half: S3 runs one farmbrite-task-audit loop end-to-end (real API pull, real brief, ledger tick via the new tool). Cite session + brief path.
3. Then begin the GATED herd-import loop exactly as the skill specifies: vault-cited draft records, full list to me, STOP at the gate. No API write before my approval of the list.

## Item 6 — install `s4-grants-ledger` on S4
1. Install `tools/skills-staging/s4-grants-ledger/SKILL.md` into the s4_logistics profile.
2. Prove: S4 re-runs its LCM Microgrant QC under the new skill — scorecard file, every score cited, ledger tick via the new tool, and an explicit line confirming it understands its hard gates (never submit, never commit funds).

## Item 7 — image generation dependency (proposal only)
`image.fal` fails in the tool runtime (fal-client missing from the nix-built env; a uv pip install does NOT fix it). Consult the hermes-agent docs for the correct optional dependency group that provides fal image generation, and PROPOSE the one-line change to `extraDependencyGroups` in `/etc/nixos/hermes.nix` plus the rebuild command — then WAIT. NixOS changes are the Commander's hands only. Target: working images before Sunday's batch drafting session.

## Final report + learning
1. BLUF table: item · done Y/N · evidence · blockers.
2. What remains for ME (approve herd list, run proof-drills, apply the NixOS diff, adjudicate doctrine edits, merge the branch).
3. Save durable lessons; update `officer-standup` / `provider-fallback` skills with the new tooling. Loop closes with the write-back.
