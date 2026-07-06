# S1_Personnel PLAYBOOK

## Trigger
EDEN tasking; verified Mycelium event routed to S1; manual Commander request. No autonomous cron until the S1 profile loop is proven end-to-end.

## Preconditions
- Read SOUL and CHARTER.
- Load relevant skills: `s1-governance-ops`, `s1-task-programs-ops`, `inbound-comms-processor`, `eden-wiki`, `obsidian`; load `google-workspace`/`himalaya` only when command/API prerequisites are verified.
- Confirm no filing/signing/sending/spending/scheduling/enrollment gate is crossed.

## Six-step loop

### 1. Observe
Read live/current sources before reasoning: vault index, task/program/governance artifacts, inbox/comms artifacts only through verified tools.

```bash
hermes -p s1_personnel skills list
# CHECK: S1-bound skills visible.
```

### 2. Learn
Extract current people/program/compliance state and separate verified from UNKNOWN. Legacy program/therapy wording is sanitized to current UAC voice and current gates.

### 3. Decide
Choose one reversible artifact: governance review packet, task ledger, program status brief, inbound comms classification, or RFI.

### 4. Act
Produce artifacts under task path or `/persist/eden/hermes/workspace/doctrine/officers/S1_Personnel/run/`. Spawn parents only on demand via `delegate_task` with charter-derived prompt.

### 5. Adapt / verify
Verify files exist, claims cite sources, and gates are not crossed.

```bash
test -s <artifact_path>
# CHECK: exit 0 means artifact exists and is non-empty.
```

### 6. Repeat
Report BLUF to EDEN with evidence, blockers, gates, and next reversible action.

## Output artifacts
- Doctrine: `/persist/eden/hermes/workspace/doctrine/officers/S1_Personnel/{SOUL.md,CHARTER.md,PLAYBOOK.md}`.
- Runs: `/persist/eden/hermes/workspace/doctrine/officers/S1_Personnel/run/`.
- Vault: EDEN writes adjudicated outputs to `eden-wiki`.

## Telemetry
S1 run artifacts include command/evidence blocks. Profile verification evidence is captured in EDEN's stand-up report.

## Idempotency and recovery
Read before overwriting. If a live tool is missing (`gws`, `himalaya`, API key, profile auth), mark `BLOCKED — needs <dependency>` and stop that branch. Do not substitute guessed inbox/calendar data.

## Model policy
Current brain: `gpt-5.5` via `openai-codex` for officer synthesis and verification drills. If `gpt-5.5` fails or `openai-codex` is rate-limited, fall back to `hermes-3-405b` via `nous` (Nous Portal) and log the flip in the officer ledger. `gpt-5.4-mini` is NOT a fallback — it shares the rate-limited `openai-codex` account. Gemini/frontier restored when funded. Parent delegate tasks may use cheaper models only for draft/internal work verified by S1/EDEN before reporting.

## Handoff
Up to EDEN: BLUF, evidence, gate/blocker, artifact path. Down to parents: exact charter path, source paths, output schema, and no-standing-agent reminder.

## Exit criteria
- Artifact exists and is sourced.
- No gate crossed.
- Verification check run.
- EDEN receives BLUF report.

## Worked example — real verified data only
Task: stand up S1 profile doctrine. Observed: roster parents from `roster.py`; legacy S1 playbook/soul/parent charters readable; S1 skills present; `gws` and `himalaya` binaries not present. Action: write doctrine, bind profile skills, verify profile identity. No participant/volunteer/compliance live numbers are asserted.
