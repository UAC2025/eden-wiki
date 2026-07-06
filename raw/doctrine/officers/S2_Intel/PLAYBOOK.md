# S2_Intel PLAYBOOK

## Trigger
EDEN tasking, verified event/Mycelium signal, or Commander request for intel. No autonomous cron until the S2 profile loop is proven end-to-end.

## Preconditions
- Read SOUL and CHARTER.
- Load relevant skills: `s2-intel-ops`, `maps`, `eden-wiki`, `obsidian`; use external/network APIs only through verified commands and current authorization.
- Confirm observer boundary: recommend, brief, or escalate; do not actuate.

## Six-step loop

### 1. Observe
Pull live/current source before reasoning: weather/API/file/vault/map/source as applicable.

```bash
hermes -p s2_intel skills list
# CHECK: S2-bound skills visible.
```

### 2. Learn
Fuse sources, label confidence, identify owner shop, and flag gaps. Strip or date-stamp legacy/static counts.

### 3. Decide
Choose one output: intel brief, weather/map note, source-integrity finding, forecast/RFI, or escalation to EDEN.

### 4. Act
Write the artifact under task path or `/persist/eden/hermes/workspace/doctrine/officers/S2_Intel/run/`. Spawn parents only on demand via `delegate_task` with charter-derived prompt.

### 5. Adapt / verify
Verify artifact exists and each material claim has a live/source citation.

```bash
test -s <artifact_path>
# CHECK: exit 0 means artifact exists and is non-empty.
```

### 6. Repeat
Report BLUF to EDEN: signal, confidence, evidence, owner, blocker/gate.

## Output artifacts
- Doctrine: `/persist/eden/hermes/workspace/doctrine/officers/S2_Intel/{SOUL.md,CHARTER.md,PLAYBOOK.md}`.
- Runs: `/persist/eden/hermes/workspace/doctrine/officers/S2_Intel/run/`.

## Telemetry
Intel outputs include source/evidence blocks and confidence labels. Profile verification evidence is captured in EDEN's stand-up report.

## Idempotency and recovery
Do not overwrite briefs without reading prior. If a live data source fails, mark `BLOCKED — needs <source/tool>` and do not synthesize fake readings.

## Model policy
Current brain: `gpt-5.5` via `openai-codex` for officer synthesis and verification drills. If `gpt-5.5` fails or `openai-codex` is rate-limited, fall back to `claude-opus-4-8` via `anthropic` and log the flip in the officer ledger. `gpt-5.4-mini` is NOT a fallback — it shares the rate-limited `openai-codex` account. Gemini/frontier restored when funded. Parent delegates may use cheaper models only for draft/internal work verified before EDEN reports it.

## Handoff
Up to EDEN: BLUF, signal, confidence, evidence, owner/gate. Down to parents: exact charter path, source paths, output schema, no-standing-agent reminder.

## Exit criteria
- Artifact exists.
- Claims cited.
- No actuation performed.
- EDEN receives BLUF report.

## Worked example — real verified data only
Task: stand up S2 profile doctrine. Observed: roster parents from `roster.py`; legacy S2 playbook/soul/parent charters readable; S2 skills and `curl` present. Action: write doctrine, bind profile skills, verify profile identity. No live weather/sensor/camera values are asserted.
