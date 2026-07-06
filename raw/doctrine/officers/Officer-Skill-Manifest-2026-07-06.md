---
title: Officer Skill Manifest — domain trim keep-lists
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
source_files: []
system_sources:
  - EDEN officer roll-call audit 2026-07-06 (skills-loaded tables; finding "⚠️ Overweight — 80+ skills each")
---

# Officer Skill Manifest (PROPOSED 2026-07-06)

EDEN's audit: every officer carries 60+ generic clone-template skills
(GitHub, ML, creative, productivity, social media…) burying the domain
skills in noise. This manifest defines per-officer KEEP lists. Everything
not on an officer's KEEP or ADJUDICATE list is quarantined (moved aside,
reversible — never deleted) by
`/home/eden/eden-ops/officer-fallback/trim_officer_skills.py`.

## Common baseline — every officer KEEPS

`officer-standup`, `eden-operations`, `eden-wiki`

## Per-officer

### s1_personnel (S1 Personnel — governance, tasking, roster)
- **KEEP:** `s1-governance-ops`, `s1-task-programs-ops`, `mdmp-council-protocol`, `eden-verdict-protocol`
- **ADJUDICATE (cross-shop, currently loaded on S1):** `s2-intel-ops`, `s6-dispatch-ops`, `inbound-comms-processor`, `forensic-mirror-analysis`, `cognitive-override-ceiling`, `s5-blind-spot-scanner`, `s2-neural-drift` — recommend each moves to its home shop (S2/S5/S6) unless S1 is the convening owner; MDMP convener role argues S1 keeps `mdmp-council-protocol` only.
- **DROP:** all generic template skills.

### s2_intel (S2 Intelligence)
- **KEEP:** `s2-intel-ops`, `s2-neural-drift`, `forensic-mirror-analysis`
- **ADJUDICATE:** research-class generic skills S2 genuinely uses for collection (name them individually at adjudication; default DROP).
- **DROP:** dev/creative/productivity template skills.

### s3_operations (S3 Operations — livestock, greenhouse, security)
- **KEEP:** baseline only — **no S3 domain skill exists yet** (LivestockAI/VetAI/etc. are vault-only parents). This is a capability gap, not a trim error.
- **DROP:** everything else (songwriting, petdex, and the rest of the template).

### s4_logistics (S4 Logistics — finance, grants, infrastructure)
- **KEEP:** baseline only — same gap as S3 (FinanceAI/GrantsAI not yet aboard).
- **DROP:** everything else.

### s5_plans (S5 Plans — development, engineering)
- **KEEP:** `claude-code`, `codex`, `opencode`, `s5-blind-spot-scanner`
- **ADJUDICATE:** `cognitive-override-ceiling` (if it is a planning guard, S5 owns it).
- **DROP:** everything else.

### s6_comms (S6 Communications — dispatch, content, brand)
- **KEEP:** `s6-dispatch-ops`, `inbound-comms-processor`
- **ADJUDICATE:** creative/content generics S6 actually dispatches with (e.g. reach/social/content skills if present on the profile — name individually; default KEEP for content-production ones EDEN already uses: `reach-engine`, `uac-social-loop`, `uac-content-system`, `meta-graph-api` if loaded).
- **DROP:** dev/ML/productivity template skills.

## Rules

1. Quarantine, never delete: skills move to
   `profiles/<p>/skills-quarantine-2026-07-06/`; restoring is a `mv`.
2. EDEN's own (gateway main-agent) skill set is NOT touched by this
   manifest — she legitimately carries cross-shop skills as the O-6.
3. A skill on no KEEP list anywhere but needed later comes back through the
   normal one-proven-capability-at-a-time door (THE RULE), not by bulk
   restore.
4. Trim is applied per officer AFTER that officer's proof loop passes on
   the trimmed set — S6 first, per the GO/NO-GO board.
