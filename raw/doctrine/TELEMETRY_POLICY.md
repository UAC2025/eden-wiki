---
title: Telemetry Policy — ledger for heartbeats, wiki for synthesis
type: doctrine
status: CANONICAL — Commander ruling 2026-07-06
date: 2026-07-06
source_files: []
---

# Telemetry Policy (Commander ruling 2026-07-06)

The vault is institutional memory; a ledger is a heartbeat monitor. They do
not mix.

1. **Machine telemetry** (loop ticks, alive-packets, per-run traces) goes to
   append-only operational ledgers in the agent's workspace (e.g.
   `workspace/logs/`, or the watchdog ledger pattern:
   `/home/eden/eden-ops/ledger.jsonl`) — never committed to the wiki.
2. **The wiki receives synthesis only**: per officer, a daily/weekly outcome
   summary a human would re-read, citing its ledger. This is THE_SPEC
   Property 7 ("operator output is narrative, not log") applied to storage.
3. Existing `S1-Alive-Loop-*` packets under `wiki/operations/S1/Officer-Packets/`
   remain as history — the faucet is off going forward; do not add new
   per-tick packets to the vault.
4. Evidence artifacts (a real filing, a real email digest, a real brief) are
   NOT telemetry — they stay in the wiki as before.
