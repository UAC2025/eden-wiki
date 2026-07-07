# S6_Comms PLAYBOOK

## Trigger
- EDEN tasking for communications, public-facing presentation, or social/reach loop work.
- S6 cron trigger for internal draft/review loop only after profile verification.
- Event/Mycelium input routed by EDEN when the source is already wired and verified.

## Preconditions
1. Load S6 SOUL/CHARTER.
2. Verify required skills are present in profile or default skill path.
3. Verify source data before using it in public-facing copy.
4. Confirm no gate is crossed: no public publish/send/deploy/stream, money, signature, or purchase without Commander approval.

## Six-step loop

### 1. Observe
- Read current tasking and relevant vault/source notes.
- Load applicable skills: `s6-dispatch-ops`, `uac-social-loop`, `reach-engine`, `uac-content-system`, `humanizer`, and platform skills only when relevant.
- Check live surface before claiming state.

```bash
hermes -p s6_comms skills list
# CHECK: S6-bound skills are visible or explicitly loaded by EDEN tasking.
```

```bash
ls /persist/eden/hermes/workspace/handoffs/s6_comms/inbox/ 2>/dev/null
# CHECK: empty → proceed. Non-empty → process every handoff per doctrine/OFFICER_COMMS.md before new tasking (S4 strategy → dispatch requests arrive here).
```

### 2. Learn
- Extract audience, channel, fact constraints, brand constraints, and source facts.
- Reconcile legacy playbook with EDEN current doctrine; current doctrine wins.
- Mark unverified facts `UNKNOWN — needs <source/check>`.

### 3. Decide
- Choose one reversible deliverable: draft, review packet, accessibility checklist, social copy, or visual brief.
- If any external/public action is required, create an escalation instead of acting.

### 4. Act
- Produce the artifact under the task-specified path or `workspace/doctrine/officers/S6_Comms/run/` for officer-run outputs.
- For parent work, instantiate UXAI only when needed, per the Parent invocation recipe below.

### 5. Adapt / verify
- Verify artifact exists and contains citations/checks for material claims.
- For dispatch/publication, require live URL/post ID/API status before saying done.

```bash
test -s <artifact_path>
# CHECK: exit 0 means file exists and is non-empty.
```

### 6. Repeat
- Report BLUF up to EDEN: outcome, evidence, gate/blocker, next reversible action.

## Parent invocation (procedure — full contract in doctrine/PARENT_INVOCATION.md)

Roster: UXAI. Card: `doctrine/parents/S6_Comms/UXAI.md`.
Spawn the parent only when the mission needs specialist depth a loaded skill does not cover. One mission, one spawn, torn down at return.

1. Read the parent card in full. No card, no spawn.
2. Call `delegate_task` with the entire card verbatim as role context, then append the mission block:

   ```text
   MISSION: <one sentence — the outcome required, not the activity>
   CONTEXT: <only inputs this officer verified — exact paths, data, constraints>
   DEADLINE/BUDGET: <turns or time>
   RETURN: BLUF · evidence paths · lessons · BLOCKED items with exact error
   ```

3. Model: cheaper model only for draft/internal missions (see Model policy); officer synthesis stays on the officer's brain.
4. Verify the return before it reaches EDEN: `test -s` every evidence path. A return without evidence is BLOCKED, not done. "BLOCKED — needs <X>" is always an acceptable return; a fabricated success never is.
5. Rails: parents never stand — no cron, no sub-spawn, no handoffs, no writes outside this shop's `run/` unless the card grants it. The publish gate passes through: UXAI never dispatches to a live surface.

## Output artifacts
- Officer doctrine: `/persist/eden/hermes/workspace/doctrine/officers/S6_Comms/{SOUL.md,CHARTER.md,PLAYBOOK.md}`.
- Run outputs: `/persist/eden/hermes/workspace/doctrine/officers/S6_Comms/run/`.
- Vault summaries: EDEN writes/syncs to `eden-wiki` when adjudicated.

## Telemetry
- Profile verification evidence is captured in EDEN session report.
- S6 run artifacts should include command/evidence blocks.
- Cron output, if used, remains internal until EDEN reviews.

## Idempotency and mid-loop recovery
- Re-running may overwrite draft artifacts only after reading existing file.
- Never duplicate public posts; use live post IDs and reach ledger checks.
- If a dependency is missing, mark `BLOCKED — needs <dependency>` and stop that branch.

## Model policy
Current brain: `gpt-5.5` via `openai-codex` for officer synthesis and verification drills. If `gpt-5.5` fails or `openai-codex` is rate-limited, fall back to `deepseek/deepseek-v4-pro` via `nous` (Nous Portal) and log the flip in the officer ledger. `gpt-5.4-mini` is NOT a fallback — it shares the rate-limited `openai-codex` account. Gemini/frontier restored when funded. UXAI delegated parent tasks may use cheaper models only when the output is draft/internal and verified before EDEN reports it.

## Handoff
- Up to EDEN: BLUF, evidence, gate/blocker, artifact path.
- Down to UXAI: charter-derived prompt, exact source paths, required output schema, verification expectations.
- Lateral to another officer: handoff file + ledger line per `doctrine/OFFICER_COMMS.md` — work moves sideways, authority never does; gates go up, not sideways.

## Exit criteria
- Required artifact produced.
- Evidence check run.
- No public/external gate crossed without approval.
- Report returned to EDEN.

## Worked example — real verified data only
Task: create S6 standing profile doctrine.

Observed checks:
- `roster.py` verified S6_Comms parent roster: `UXAI`.
- Legacy S6 playbook, S6 soul, UXAI charter, and UXAI draft playbook were readable.
- Skills verified present: `s6-dispatch-ops`, `uac-social-loop`, `reach-engine`, `meta-graph-api`, `xurl`, `uac-content-system`, `humanizer`.
- Commands verified missing: `node`, `npm`, `npx`.

Action: write S6 SOUL/CHARTER/PLAYBOOK and wire profile. Public dispatch is not performed in the worked example.
