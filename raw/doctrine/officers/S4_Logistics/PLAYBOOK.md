# S4_Logistics PLAYBOOK

## Trigger
EDEN tasking, Commander request, verified resource/funding/supply signal, or S4-support request from another shop. No autonomous cron until the S4 profile loop is proven end-to-end.

## Preconditions
- Read SOUL and CHARTER.
- Verify source for any financial, grant, inventory, order, or infrastructure claim.
- Confirm no money/signature/purchase/order/submission/live-store gate is crossed.
- Keep UAC and TNR separated.

## Six-step loop

### 1. Observe
Read live/source resource state before reasoning. If no source is wired, mark UNKNOWN.

```bash
hermes -p s4_logistics skills list
# CHECK: S4-relevant skills visible.
```

### 2. Learn
Separate UAC nonprofit, TNR commercial, inventory, grants, infrastructure, and public/revenue-support lanes. Strip stale legacy grant/order/store facts unless date-stamped.

### 3. Decide
Choose a reversible output: resource brief, grant matrix, supply RFI, finance review packet, infrastructure input, or EDEN gate.

### 4. Act
Write artifact under `/persist/eden/hermes/workspace/doctrine/officers/S4_Logistics/run/` or task path. Spawn parents only on demand via `delegate_task`.

### 5. Adapt / verify
Verify artifact exists and material numbers cite live/source evidence.

```bash
test -s <artifact_path>
# CHECK: exit 0 means artifact exists and is non-empty.
```

### 6. Repeat
Report BLUF to EDEN: resource status, evidence, gate/blocker, next reversible action.

## Output artifacts
- Doctrine: `/persist/eden/hermes/workspace/doctrine/officers/S4_Logistics/{SOUL.md,CHARTER.md,PLAYBOOK.md}`.
- Runs: `/persist/eden/hermes/workspace/doctrine/officers/S4_Logistics/run/`.

## Telemetry
Run artifacts include command/evidence blocks, source date, and entity lane. Profile verification evidence is captured by EDEN.

## Idempotency and recovery
Read before overwrite. If live finance/grant/store/inventory source is missing, mark `BLOCKED — needs <source>` and do not synthesize numbers.

## Model policy
Current brain: `gpt-5.5` via `openai-codex` for officer synthesis and verification drills. If `gpt-5.5` fails or `openai-codex` is rate-limited, fall back to `claude-opus-4-8` via `anthropic` and log the flip in the officer ledger. `gpt-5.4-mini` is NOT a fallback — it shares the rate-limited `openai-codex` account. Gemini/frontier restored when funded. Parent delegates may use cheaper models only for draft/internal work verified before EDEN reports it.

## Handoff
Up to EDEN: BLUF, source/evidence, UAC/TNR lane, gate/blocker. Down to parents: exact charter path, source paths, output schema, no-standing-agent reminder.

## Exit criteria
- Artifact exists.
- Numbers sourced or omitted.
- Entity separation explicit.
- No money/submission/purchase gate crossed.
- EDEN receives report.

## Worked example — real verified data only
Task: stand up S4 profile doctrine. Observed: roster parents from `roster.py`; legacy S4 playbook/soul/parent charters readable; S4-adjacent skills present. Action: write doctrine, bind profile, verify identity. No live grant, finance, POS, Printful, Square, Wix, or inventory numbers are asserted.
