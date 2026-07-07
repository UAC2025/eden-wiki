---
title: Parent Invocation — how officers delegate to on-demand parents
type: doctrine
status: CANONICAL
date: 2026-07-06
source_files: []
---

# Parent Invocation Playbook

Every officer has on-demand parent agents. This is the recipe for spawning
them correctly — pasting the right context, enforcing the return contract,
and logging the delegation. A cheap model following this playbook should
produce the same quality delegation as an expensive one.

## When to spawn a parent

| Situation | Action |
|---|---|
| Task requires domain expertise the officer doesn't hold | Spawn the domain parent |
| Task is draft/internal work (no external surface) | Spawn; cheaper model OK |
| Task involves public content, money, or signatures | Officer does it directly; parent assists only |
| Parent output will be verified by the officer anyway | Spawn freely |

## Delegation recipe (exact `delegate_task` pattern)

Every parent spawn follows this template. Copy it verbatim; fill in the
`<placeholder>` fields only. Do not improvise the structure.

```
delegate_task(
  goal="<one-sentence task description — what the parent should produce>",
  context="<paste the parent card verbatim from raw/doctrine/parents/<Shop>/<Agent>.md>
            TASK: <specific instruction>
            OUTPUT PATH: <absolute path for the deliverable>
            RETURN: <what format, what evidence to include>
            RULES: <any domain-specific constraints>
            SOURCES: <paths to any input files the parent needs>",
  role="leaf"
)
```

## Return contract — what the parent must deliver

Every parent response must include:
1. **BLUF** — one sentence describing what was done
2. **Evidence** — file paths, session IDs, API responses
3. **Blockers** — anything that prevented completion, with exact errors
4. **Unverified facts** — claims the parent couldn't verify, flagged as `UNKNOWN`

The officer **verifies** the parent's return before reporting up the chain:
- Do the evidence files exist? (`test -s <path>`)
- Are all claims sourced? (check for receipts)
- Are any gates crossed? (publish, spend, sign, reconfigure)

If verification fails, the officer returns the output to the parent
with specific corrections requested — do not silently fix and pass up.

## Officer-level invocation examples

### S1_Personnel → SecretarialAI

```
goal="Governance review packet for Commander board prep"
context="TASK: Read governance recommendations from /persist/eden/hermes/workspace/eden-wiki/wiki/operations/S1/Governance/Governance-Recommendations-2026-07-06.md, format into a Commander-ready review packet with severity-ranked items. OUTPUT: /persist/eden/hermes/workspace/doctrine/officers/S1_Personnel/run/governance-packet-YYYY-MM-DD.md. RETURN: Packet file + ledger tick. RULES: No filing, signing, or sending. No fabricated compliance data."
```

### S4_Logistics → GrantsAI

```
goal="Score new grant opportunity against UAC eligibility"
context="TASK: Read grant RFP at <path>, score against UAC's mission (heritage breed conservation, veteran ag programs, 501c3). OUTPUT: /persist/eden/hermes/workspace/doctrine/officers/S4_Logistics/run/grant-score-<funder>-YYYY-MM-DD.md. RETURN: Scorecard with criteria, scores, citations. RULES: Never submit. Never commit funds. Score only."
```

### S2_Intel → WeatherAI

```
goal="48-hour farm weather forecast with livestock impact assessment"
context="TASK: Pull 3-source weather fusion, produce farm-specific forecast. Highlight: frost risk, heat stress >85°F, rain >0.5", wind >25mph. OUTPUT: /persist/eden/hermes/workspace/doctrine/officers/S2_Intel/run/weather-brief-YYYY-MM-DD.md. RETURN: Brief + source citations. RULES: No fabrication — if a source is down, report the outage."
```

### S6_Comms → UXAI

```
goal="Produce visual assets for conservation social post"
context="TASK: Using the approved post copy at <path>, design 1-2 visual variants for Facebook. Dimensions: 1200x630. Style: conservation-heritage, farm photography aesthetic. OUTPUT: /persist/eden/hermes/workspace/doctrine/officers/S6_Comms/run/visual-<topic>-YYYY-MM-DD.png. RETURN: Image path + alt text. RULES: No public posting. Commander approves before dispatch."
```

### S5_Plans → EngineeringAI

```
goal="Design review for proposed NixOS module change"
context="TASK: Review the proposed configuration change at <path>, produce an ENGINEERING_DESIGN.md with risk assessment, interface impacts, and verification criteria. OUTPUT: /persist/eden/hermes/workspace/doctrine/officers/S5_Plans/run/engineering-review-<change>-YYYY-MM-DD.md. RETURN: Design artifacts + risk register. RULES: No implementation. No NixOS rebuild. Review only."
```

### S3_Operations → LivestockAI

```
goal="Draft breeding schedule for Arapawa herd based on vault records"
context="TASK: Read animal records from raw/animals/ and entities/, produce a breeding eligibility calendar for the next 6 months. Flag any missing data. OUTPUT: /persist/eden/hermes/workspace/doctrine/officers/S3_Operations/run/breeding-calendar-YYYY-MM-DD.md. RETURN: Calendar + source citations + data gaps. RULES: No fabricated health/breeding data. Data Rule applies."
```

## Model policy for parent delegates

- Parent delegates **may** use cheaper models for draft/internal work.
- Every parent output is **verified by the sponsoring officer** before
  it reaches EDEN or the Commander.
- If the parent model fabricates or produces uncited claims, the officer
  returns it, logs a `blocker fail`, and re-runs on the officer's own
  model (currently `deepseek/deepseek-v4-pro/nous`).

---
Changelog:
- 2026-07-06 — CANONICAL, delegation recipes for all 6 shops
