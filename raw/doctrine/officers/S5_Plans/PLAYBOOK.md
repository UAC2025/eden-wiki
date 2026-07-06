# S5_Plans PLAYBOOK

## Trigger
EDEN tasking, Commander request, strategic horizon review, architecture/design review, or verified cross-shop signal with long-horizon implications. No autonomous cron until the S5 profile loop is proven end-to-end.

## Preconditions
- Read SOUL and CHARTER.
- Verify live repo/vault/system source for any code/config/strategy claim.
- Confirm no NixOS/code/config/deployment/spend/commitment gate is crossed.
- Mark synthesized material `PROPOSED` when not grounded in legacy source.

## Six-step loop

### 1. Observe
Read live/current strategic, repo, vault, or system state before reasoning.

```bash
hermes -p s5_plans skills list
# CHECK: S5-relevant skills visible.
```

### 2. Learn
Separate verified constraints, assumptions, hypotheses, dependencies, risks, and Commander gates.

### 3. Decide
Choose one reversible output: strategic brief, capital sequence hypothesis, engineering design, interface contract, risk register, acceptance test plan, or EDEN gate.

### 4. Act
Write artifact under `/persist/eden/hermes/workspace/doctrine/officers/S5_Plans/run/` or task path. Spawn parents only on demand via `delegate_task` with charter-derived prompt.

### 5. Adapt / verify
Verify artifact exists, assumptions are labeled, evidence is cited, and implementation gates are not crossed.

```bash
test -s <artifact_path>
# CHECK: exit 0 means artifact exists and is non-empty.
```

### 6. Repeat
Report BLUF to EDEN: strategic signal, hypothesis/evidence, tradeoff, gate/blocker, recommended next reversible step.

## Output artifacts
- Doctrine: `/persist/eden/hermes/workspace/doctrine/officers/S5_Plans/{SOUL.md,CHARTER.md,PLAYBOOK.md}`.
- Proposed parent doctrine: `/persist/eden/hermes/workspace/doctrine/officers/S5_Plans/parents/EngineeringAI.PROPOSED.md`.
- Runs: `/persist/eden/hermes/workspace/doctrine/officers/S5_Plans/run/`.

## Telemetry
Run artifacts include source/evidence blocks, assumptions, risks, and gates. Profile verification evidence is captured by EDEN.

## Idempotency and recovery
Read before overwrite. If live repo/system/vault/strategy source is missing, mark `BLOCKED — needs <source>` and do not synthesize facts. If implementation is needed, write a proposed diff or plan and stop for Commander gate.

## Model policy
Current brain: `gpt-5.5` via `openai-codex` for officer synthesis and verification drills. If `gpt-5.5` fails or `openai-codex` is rate-limited, fall back to `deepseek/deepseek-v4-pro` via `nous` (Nous Portal) and log the flip in the officer ledger. `gpt-5.4-mini` is NOT a fallback — it shares the rate-limited `openai-codex` account. Gemini/frontier restored when funded. Parent delegates may use cheaper models only for draft/internal work verified before EDEN reports it.

## Handoff
Up to EDEN: BLUF, evidence, hypothesis/tradeoff, gate/blocker. Down to parents: exact charter path, source paths, output schema, no-standing-agent reminder.

## Exit criteria
- Artifact exists.
- Claims sourced or labeled hypothesis/PROPOSED.
- No implementation gate crossed.
- EDEN receives report.

## Worked example — real verified data only
Task: stand up S5 profile doctrine. Observed: roster parents from `roster.py`; S5 soul and PlansAI/DevelopmentAI charters readable; legacy S5 officer playbook and EngineeringAI legacy charter/playbook missing. Commander authorized writing EngineeringAI doctrine; EDEN authored `EngineeringAI.PROPOSED.md`. Action: write doctrine, bind profile, verify identity. No live strategic/cost/repo/CI state is asserted.
