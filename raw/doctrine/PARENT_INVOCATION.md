---
title: Parent Invocation Contract — how officers call their parents
type: doctrine
status: PROPOSED — operator adjudication = merge to main
date: 2026-07-06
source_files: []
system_sources:
  - hermes chat CLI flags (-m/--provider), verified 2026-07-06
  - delegate_task tool (tools_config.py:78; batch tasks + /agents monitoring), verified in package source 2026-07-06
---

# Parent Invocation Contract

How a standing officer calls an on-demand parent agent. Parents are **never
standing**: durable identity (a parent card on file), lazy execution (spawned
per mission, torn down after the return).

## Invocation

1. The officer selects the parent from its charter's Parents-on-demand roster.
2. The officer reads the parent card at `doctrine/parents/<shop>/<Agent>.md`
   and spawns the child via **`delegate_task`**, passing:
   - the **entire parent card verbatim** as the child's role/system context,
   - the **mission block** (below) appended,
   - a **cheaper model** where the mission allows (officer synthesis stays on
     the frontier model; see [[PROVIDER_POLICY]]).
3. Parallel missions to several parents go in one `delegate_task` call with a
   `tasks` list; the officer monitors via `/agents`.

## Mission block (appended by the officer per call)

```
MISSION: <one sentence — the outcome required, not the activity>
CONTEXT: <live inputs the officer already verified — paths, data, constraints>
DEADLINE/BUDGET: <turns or time>
RETURN: BLUF outcome · evidence (commands run, artifacts produced, live-surface
proof) · lessons worth persisting · anything BLOCKED with the exact error
```

## Return contract (what the parent owes back)

- **BLUF first.** Outcome, then evidence, then lessons.
- Every claim grounded in a command actually run or a file actually produced.
  "BLOCKED — needs <X>" is always an acceptable return; a fabricated success
  never is.
- The **officer** (not the parent) closes the six-step loop: it verifies the
  return (Adapt), persists lessons to its profile memory, and reports upward
  to EDEN only synthesis, not raw child output.

## Rails

- Parents inherit every EDEN doctrine rail through their card: anti-fabrication,
  credential doctrine, scope doctrine, the Commander's gates.
- A parent may not spawn further agents, register cron, or write outside the
  officer's workspace unless its card grants it explicitly.
- If a parent's mission needs a tool that is not wired, it returns BLOCKED —
  the officer escalates to EDEN, who escalates to the Commander if it's a gate
  (keys, money).
