# S3_Operations PLAYBOOK

## Trigger
EDEN tasking, verified event routed from S2/Mycelium, or Commander farm-operations request. No autonomous cron until the S3 profile loop is proven end-to-end.

## Preconditions
- Read SOUL and CHARTER.
- Verify live source for any animal/farm/environment claim.
- Confirm no physical actuation or living-being gate is crossed.

## Six-step loop

### 1. Observe
Read live/source farm state before reasoning. If no live source is available, state UNKNOWN.

```bash
hermes -p s3_operations skills list
# CHECK: profile skills visible.
```

```bash
ls /persist/eden/hermes/workspace/handoffs/s3_operations/inbox/ 2>/dev/null
# CHECK: empty → proceed. Non-empty → process every handoff per doctrine/OFFICER_COMMS.md before new tasking (S2 weather/intel alerts arrive here).
```

### 2. Learn
Separate operational need, welfare risk, safety risk, and source confidence. Current EDEN data rules override legacy claims.

### 3. Decide
Choose a reversible output: checklist, RFI, safety gate, parent-on-demand analysis, or recommendation to EDEN.

### 4. Act
Write artifact under `/persist/eden/hermes/workspace/doctrine/officers/S3_Operations/run/` or task path. Spawn parents only on demand per the Parent invocation recipe below.

### 5. Adapt / verify
Verify artifact exists and living-being claims cite live/source evidence.

```bash
test -s <artifact_path>
# CHECK: exit 0 means artifact exists and is non-empty.
```

### 6. Repeat
Report BLUF to EDEN: risk, evidence, owner/action, gate/blocker.

## Parent invocation (procedure — full contract in doctrine/PARENT_INVOCATION.md)

Roster: AquaponicsAI, BotanyAI, GreenhouseAI, LivestockAI, RoboticsAI, SecurityAI, VetAI (VetAI covers Medical — Commander ruling 2026-07-06). Cards: `doctrine/parents/S3_Operations/<Agent>.md`.
Spawn a parent only when the mission needs specialist depth a loaded skill does not cover. One mission, one spawn, torn down at return.

1. Read the parent card in full. No card, no spawn.
2. Call `delegate_task` with the entire card verbatim as role context, then append the mission block:

   ```text
   MISSION: <one sentence — the outcome required, not the activity>
   CONTEXT: <only inputs this officer verified — exact paths, data, constraints>
   DEADLINE/BUDGET: <turns or time>
   RETURN: BLUF · evidence paths · lessons · BLOCKED items with exact error
   ```

   Parallel missions to several parents: one `delegate_task` call with a `tasks` list; monitor via `/agents`.
3. Model: cheaper model only for draft/internal missions (see Model policy); officer synthesis stays on the officer's brain. Welfare/health analysis (VetAI) is never a cheaper-model mission.
4. Verify the return before it reaches EDEN: `test -s` every evidence path. A return without evidence is BLOCKED, not done. "BLOCKED — needs <X>" is always an acceptable return; a fabricated success never is.
5. Rails: parents never stand — no cron, no sub-spawn, no handoffs, no writes outside this shop's `run/` unless the card grants it. No physical actuation and no living-being gate crossing pass through to parents.

## Output artifacts
- Doctrine: `/persist/eden/hermes/workspace/doctrine/officers/S3_Operations/{SOUL.md,CHARTER.md,PLAYBOOK.md}`.
- Runs: `/persist/eden/hermes/workspace/doctrine/officers/S3_Operations/run/`.

## Telemetry
Run artifacts include command/evidence blocks. Profile verification evidence is captured by EDEN.

## Idempotency and recovery
Do not overwrite without reading. If live animal/sensor/tool source missing, mark `BLOCKED — needs <source>` and stop that branch.

## Model policy
Current brain: `gpt-5.5` via `openai-codex` for officer synthesis and verification drills. If `gpt-5.5` fails or `openai-codex` is rate-limited, fall back to `deepseek/deepseek-v4-pro` via `nous` (Nous Portal) and log the flip in the officer ledger. `gpt-5.4-mini` is NOT a fallback — it shares the rate-limited `openai-codex` account. Gemini/frontier restored when funded. Parent delegates may use cheaper models only for draft/internal work verified before EDEN reports it.

## Handoff
Up to EDEN: BLUF, evidence, welfare/safety gate, blocker. Down to parents: charter path, source paths, exact question, no-standing-agent reminder. Lateral to another officer: handoff file + ledger line per `doctrine/OFFICER_COMMS.md` — work moves sideways, authority never does; gates go up, not sideways.

## Exit criteria
- Artifact exists.
- No physical actuation.
- Living-being claims sourced or omitted.
- EDEN receives report.

## Worked example — real verified data only
Task: stand up S3 profile doctrine. Observed: roster parents from `roster.py`; legacy S3 playbook/soul/parent charters readable; no dedicated S3 skill verified. Action: write doctrine, bind profile, verify identity. No live animal/sensor/operation state is asserted.
