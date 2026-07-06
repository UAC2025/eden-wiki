---
title: EDEN Skill Authoring Standard
status: DRAFT
version: 1.0
owner: Commander (Chad)
maintainer: EDEN
adopted: 2026-07-06
source_files: []
source_note: "Adopted from Commander-provided SKILLS.md draft in Telegram on 2026-07-06; corrected by operator direction that the current EDEN vault is source of truth and legacy Git is reference only."
---

# EDEN Skill Authoring Standard

A skill is verified procedural memory: a portable folder containing a `SKILL.md` that teaches a competent model the non-obvious parts of a recurring task. The model reading a skill is already smart and already knows general knowledge. A skill's value is therefore:

> environment-specific + hard-won + verified knowledge per token.

This standard has three layers:

1. **General skill design** — trigger accuracy, progressive disclosure, footguns, and verification.
2. **EDEN overlay** — DRAFT/canonical governance, no-fabrication doctrine, operator gates, and vault-as-truth.
3. **Framework binding** — Claude/Hermes loading mechanics, documented only after live verification.

## 0. BLUF

Walk the path first. Write the description like it is the product. Teach only the footguns. Pair every state-changing step with a check. Save canonical doctrine into the current EDEN vault, not the legacy Git backup.

Three failure modes kill skills:

1. **It does not trigger.** The description failed.
2. **It teaches what the model already knows.** Bloat wastes context and hides the payload.
3. **It describes a path nobody walked.** In EDEN, that is fabrication, not a style issue.

## 1. Definitions and scope

A skill is procedural memory. It is not system configuration, agent identity, current state, event history, task state, or secrets.

| Not a skill | Lives instead in |
|---|---|
| System configuration | NixOS flakes / modules |
| Agent identity, roles, authority | Agent charters / roster |
| Current system state | Current EDEN status notes / live checks |
| Event history | Journals / operation logs |
| Task lists | Hermes `todo` / task ledgers |
| Secrets | agenix / approved secret store only |

Creation test — all three must be true for a **canonical** skill:

1. **Recurrence:** the task is expected to happen at least two more times.
2. **Non-obviousness:** a competent fresh model would get it wrong, slow, or dangerous without the skill.
3. **Walked path:** the procedure has been executed successfully at least once, with evidence.

A **DRAFT** skill may capture a partially walked path only when every unverified step is marked `UNVERIFIED — needs live run` and the status remains DRAFT.

## 2. The ten laws

1. **Walk the path first.** Canonical skills document procedures executed with evidence.
2. **The description is the trigger.** Name + description are the always-loaded routing surface.
3. **Footguns, not tutorials.** Assume a competent model; document deltas, traps, exact incantations, and environment quirks.
4. **Verification is procedure.** Every state-changing step has an immediate check and expected signal.
5. **Progressive disclosure.** Metadata always loaded; body on trigger; references/scripts on demand.
6. **Explain why.** Models generalize from reasons. Reserve absolutes for safety and verification.
7. **One concept, one term.** Put synonyms in the description for triggering; use one term in the body.
8. **Drafts until adjudicated.** Agents do not self-promote skills to canonical.
9. **The current vault is truth.** Canonical EDEN skills/doctrine live in the current EDEN vault. Legacy Git backups are read-only reference unless the operator explicitly promotes an artifact.
10. **Never touch the security floor.** Skills never inline secrets, never change sudo/auth policy, and mark privileged steps as `OPERATOR ACTION`.

## 3. Anatomy of a skill

```text
skill-name/
├── SKILL.md
├── scripts/       # optional deterministic helpers
├── references/    # optional bulky docs loaded only when needed
└── assets/        # optional templates, fonts, icons, examples
```

`SKILL.md` frontmatter:

```yaml
---
name: skill-name
description: <capability + triggers + negative triggers>
status: DRAFT
version: 0.1
---
```

Required fields:

| Field | Rule |
|---|---|
| `name` | lowercase letters/digits/hyphens; max 64 chars; matches directory |
| `description` | max 1024 chars; target 300–600; third person; trigger-focused |
| `status` | EDEN recommended: `DRAFT` or `CANONICAL` |
| `version` | EDEN recommended |

Body order:

1. Title + orientation — 1–3 sentences explaining the artifact/task mechanically.
2. Approach selection — if multiple paths exist.
3. Prerequisites — only non-obvious ones, with checks.
4. Procedure — walked path, paired checks.
5. Verify final output — exact commands/evidence format.
6. Failure modes — observed symptom → confirmed cause → actual fix.
7. References — one-line pointers saying when to open each file.

## 4. The description is the trigger

Only name + description are always in context. The body loads after the model decides to use the skill. A perfect body behind a weak description is a skill that does not exist operationally.

Formula:

```text
[What it does — third person, concrete capability]
+ Use when [trigger contexts, user phrases, file types, symptoms, situations]
+ Do NOT use for [near-miss cases]
```

Rules:

- Use third person: “Diagnoses and recovers X,” not “I” or “you.”
- Be pushy. Models under-trigger skills. Include formal and casual phrasings.
- Front-load matchable nouns: file extensions, service names, product names, error strings.
- Put synonyms in the description only. Use one term in the body.
- Include negative triggers for near-miss tasks.
- Put trigger/scoping information in the description. Put post-trigger approach selection in the body.

## 5. Progressive disclosure

| Level | What | When loaded | Budget |
|---|---|---|---|
| 1 | name + description | Always | about 100 words |
| 2 | `SKILL.md` body | On trigger | under 500 lines |
| 3 | scripts/references/assets | On explicit need | no prose budget, but keep navigable |

Splitting rules:

- Body near 500 lines → extract to `references/` or `scripts/`.
- Reference files over 300 lines need a table of contents.
- Keep references one level deep.
- Prefer scripts for deterministic repeated work.

## 6. Degrees of freedom

| Freedom | Use when | Form |
|---|---|---|
| None | Variation breaks the job | Exact command or bundled script |
| Low | Stable pattern with variable inputs | Parameterized steps + filled example |
| Medium | Several valid paths | Decision table + why |
| High | Judgment/creative work | Principles + 2–3 examples |

Mix levels inside a skill when needed: high freedom for content, zero freedom for validation or packaging.

## 7. Writing the body

- Use imperative mood: “Run X. Check Y.”
- BLUF every section.
- No hedging. If unknown, write `UNKNOWN — resolve with: <command>`.
- No time-relative language unless date-stamped.
- No aspirational framing: “eventually,” “deferred,” “demo-grade,” and “Phase 5+” are DRIFT flags.
- Ask of every line: would a strong model get this wrong without being told? If not, delete it.
- Explain why for generalization, except security and verification rules, which stay absolute.

## 8. Verification doctrine — EDEN overlay

Every state-changing step is incomplete without an immediate check.

Example:

```bash
systemctl restart hermes-agent.service
# CHECK: systemctl is-active hermes-agent.service -> active
# CHECK: journalctl -u hermes-agent.service --since "-2 min" --no-pager | tail -20 -> startup lines, no traceback
```

Evidence protocol:

```text
VERIFIED: <claim> — evidence: <command> -> <observed output>
```

No evidence means no success claim. Report actual state instead.

Banned report language without evidence: “should work,” “likely succeeded,” “presumably,” “appears to have,” “completed,” or any simulated output presented as observed output.

`UNKNOWN` is valid and required when a fact cannot be verified in-session.

Before claiming an integration, path, service, alias, port, or job exists, verify from live source: config grep, `systemctl`, `git`, file tree, or equivalent. Memory is not evidence.

Never invent metrics, test results, timing numbers, observational data, animal facts, health data, breeding data, or financial outcomes.

## 9. Authoring process — Fable method

1. Walk the path on the real system; keep transcript.
2. Harvest exact commands, outputs, errors, and corrections.
3. Distill reusable pattern from one-off context.
4. Write the description first.
5. Draft body in standard order; every state change gets checks.
6. Extract deterministic work to `scripts/`; bulky detail to `references/`.
7. Red-team as a naive agent with zero chat context.
8. Test-run 2–3 realistic prompts; read transcripts, not just final answers.
9. Trigger-eval 8–10 should-trigger and 8–10 near-miss should-not-trigger prompts.
10. Present to operator for adjudication; only then promote to canonical.

## 10. Testing protocol

Use messy, realistic prompts. Trivial prompts do not test skill loading.

Judge runs on:

1. Triggered correctly.
2. Procedure followed without harmful improvisation.
3. Verification evidence present.

A run that “succeeds” without evidence is a failed run under EDEN doctrine.

## 11. Anti-patterns

| Symptom | Why it fails | Fix |
|---|---|---|
| Tutorial bloat | Wastes budget | Footguns only |
| Aspirational procedure | Fabrication | Walk it or mark DRAFT/UNVERIFIED |
| Vague description | Does not trigger | Use the description formula |
| Kitchen-sink skill | Misfires and rots | Split by job |
| Ambiguous paths | Executor guesses | Absolute paths or anchored checks |
| MUST-spam | Narrow compliance | Explain why; reserve absolutes |
| Time-relative facts | Rot silently | Date-stamp or delete |
| Self-certified success | Core EDEN failure mode | Evidence protocol |
| Inline secrets | Security violation | agenix/approved secret references only |
| Building new instead of wiring existing | Split-brain | Search existing capability first |

## 12. Lifecycle and governance

The canonical skills root lives inside the current EDEN vault or the vault-designated runtime skill tree. Read the current vault manifest/canonical-path note before writing; never assume from memory.

Legacy Git backups are not canonical. They are reference material for what existed before the NixOS rebuild. Use them to recover ideas, names, and lessons; rewrite and adjudicate into the current vault before treating anything as current.

Versioning:

- Procedure change = major version.
- Wording/description tuning = minor version.
- Changelog at foot: date, version, change, evidence reference.

Update triggers:

- Failed run using a skill → same-session patch or mark affected step `UNVERIFIED`.
- Environment change → re-verify affected paths/services/ports before next use.
- Deletion/supersession → operator call.

Vault sync and security:

- Writers save canonical work into the current EDEN vault, not the legacy Git backup.
- If the vault uses Git, Obsidian Git, Syncthing, Drive, or another sync mechanism, verify that mechanism according to the current vault operating note.
- Legacy Git repositories are read-only archaeological sources unless the operator explicitly promotes a file/procedure.
- Commit/push requirements apply only where the current vault’s active sync mechanism is Git-backed.
- Secrets never appear in skills.
- Privileged steps are `OPERATOR ACTION`; agents stop at that gate.

## 13. Framework bindings

Claude Code / Claude.ai / Cowork: discovery is automatic where the runtime scans skill directories, keeps name + description in context, and loads body when selected.

Hermes: verified local behavior as of this NixOS environment:

- `skill_manage(action='create')` writes to the active Hermes profile under `~/.hermes/skills/`.
- In-repo or vault skills may require direct file writes plus a fresh session before they appear in `skills_list`.
- The current session’s skill loader may be cached.
- Do not claim auto-loading by any framework unless verified from live config or current docs.

Portability comes from keeping skills as plain Markdown folders with `SKILL.md` plus optional `scripts/`, `references/`, and `assets/`.

## 14. Template

```markdown
---
name: verb-noun-name
description: [Third person capability.] Use when [trigger contexts, symptoms,
  casual phrases, file types, situations]. Also use when [indirect phrasings].
  Do NOT use for [near-miss cases and owner instead].
status: DRAFT
version: 0.1
---

# [Skill Title]

[1–3 sentences: what this task/artifact is mechanically.]

## Approach selection

| Task | Approach |
|---|---|
| [variant A] | [route] |
| [variant B] | [route] |

## Prerequisites

- [Non-obvious requirement + check command -> expected signal]

## Procedure

1. [Step]

   ```bash
   <exact command>
   # CHECK: <check command> -> <expected signal>
   ```

2. OPERATOR ACTION: <privileged command> — agent does not execute.

## Verify final output

```bash
<command that proves the whole job succeeded>
# EVIDENCE FORMAT: VERIFIED: <claim> — evidence: <cmd> -> <output>
```

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| [observed symptom] | [confirmed cause] | [actual fix] |

## References

- `references/x.md` — read when [specific condition].

---
Changelog:
- [date] v0.1 DRAFT — initial capture from walked path [evidence ref].
```

## 15. Quality gate — pre-merge checklist

- [ ] Creation test passed: recurrence + non-obviousness + walked path, or DRAFT/UNVERIFIED labels are present.
- [ ] Description is third person, max 1024 chars, explicit triggers, casual phrasing, and negative triggers.
- [ ] Trigger/scoping info is in description; post-trigger routing is in body.
- [ ] Body under 500 lines; heavy detail extracted to references/scripts.
- [ ] Tutorial content deleted; footguns and environment deltas remain.
- [ ] Every state-changing step has a paired check.
- [ ] Final-output verification exists with exact command/evidence format.
- [ ] No banned language or unevidenced success claims.
- [ ] UNKNOWNs carry resolve commands.
- [ ] Every path/port/unit/alias is live-observed or flagged UNVERIFIED.
- [ ] No fabricated data, including examples.
- [ ] No secrets; privileged steps marked OPERATOR ACTION.
- [ ] No DRIFT framing.
- [ ] Test-run on at least two realistic prompts before canonical promotion.
- [ ] Trigger eval run against should-trigger and near-miss negatives.
- [ ] Status/version/changelog present.
- [ ] Saved to current EDEN vault source-of-truth location.
- [ ] Vault sync/export verified using the current vault mechanism.
- [ ] Any legacy Git material used was treated as reference only and re-adjudicated before inclusion.

---
Changelog:
- 2026-07-06 v1.0 DRAFT — adopted from Commander-provided SKILLS.md draft; corrected to make the current EDEN vault the source of truth and legacy Git reference-only.
