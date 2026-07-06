# Rulings Execution Report — 2026-07-06

EDEN executed Commander RULINGS EXECUTED directive (2026-07-06),
5 items, all closed or proposed.

## Item 1: Memory pointers re-pointed ✓

All six profile MEMORY.md files rewritten:

| Profile | Charter | Playbook | SOUL |
|---|---|---|---|
| s1_personnel | raw/doctrine/officers/S1_Personnel/CHARTER.md | ...PLAYBOOK.md | ...SOUL.md |
| s2_intel | raw/doctrine/officers/S2_Intel/CHARTER.md | ...PLAYBOOK.md | ...SOUL.md |
| s3_operations | raw/doctrine/officers/S3_Operations/CHARTER.md | ...PLAYBOOK.md | ...SOUL.md |
| s4_logistics | raw/doctrine/officers/S4_Logistics/CHARTER.md | ...PLAYBOOK.md | ...SOUL.md |
| s5_plans | raw/doctrine/officers/S5_Plans/CHARTER.md | ...PLAYBOOK.md | ...SOUL.md |
| s6_comms | raw/doctrine/officers/S6_Comms/CHARTER.md | ...PLAYBOOK.md | ...SOUL.md |

VERIFIED: 18/18 doctrine files confirmed present at new paths via `test -f`.
All profile configs already default to gpt-5.5/openai-codex.

## Item 2: Parent rosters updated ✓

- Aligned parents-on-demand to vault `raw/doctrine/parents/<shop>/` directory
- S2: Removed stale SecurityAI (belongs to S3). Now: WeatherAI, VisionAI,
  TelemetryAI, PredictiveAI, MapAI, ForgeAI, CodexAI
- S5: EngineeringAI promoted from PROPOSED to ADOPTED canonical with path
  `raw/doctrine/parents/S5_Plans/EngineeringAI.md`
- All parents cited with vault-relative paths in MEMORY.md

## Item 3: Gateway model — PROPOSED (not applied)

NixOS-managed. hermes.nix lines 17-18 currently:
```nix
provider = "gemini";
default = "gemini-3.1-pro-preview";
```

Proposed diff:
```diff
-      provider = "gemini";
-      default = "gemini-3.1-pro-preview";
+      provider = "openai-codex";
+      default = "gpt-5.5";
```

Rebuild required: `sudo nixos-rebuild switch`
Commander gate: NixOS config change + rebuild

## Item 4: TELEMETRY_POLICY enacted ✓

Per `raw/doctrine/TELEMETRY_POLICY.md` (Commander ruling 2026-07-06):

- s2_alive_loop.py patched: `write_intel_brief()` no longer writes per-tick
  `S2-Intel-Brief-{date}.md` to `wiki/operations/S2/`
- Output redirected to workspace ledger: `s2_operational/data/s2_intel_brief_{date}.json`
- Workspace `s2_operational/data/s2_alive_latest.json` unchanged (already correct)
- No existing alive-loop cron jobs write to wiki
- No alive-loop packets remain in `wiki/operations/S1/Officer-Packets/`
  (history preserved per policy §3)

## Item 5: Firecrawl fix — PROPOSED (not applied)

Root cause from 2026-07-02 audit: `search.firecrawl` feature requires
`firecrawl-py` Python package; `pip install` fails on immutable NixOS.

Proposed fix: add `python3Packages.firecrawl-py` to `environment.systemPackages`
in `configuration.nix` or to the Hermes service environment.

```diff
  environment.systemPackages = with pkgs; [
    (python3.withPackages (ps: with ps; [
      google-api-python-client
      google-auth
      google-auth-oauthlib
      google-auth-httplib2
      requests
+     firecrawl-py
    ]))
    uv
    git
  ];
```

Rebuild required: `sudo nixos-rebuild switch`
Note: if `firecrawl-py` is not in nixpkgs, alternative is to configure
Hermes to use a different web_search provider (e.g., `brave`, `tavily`).

## Verification summary

| Item | Status | Evidence |
|---|---|---|
| 1. Memory pointers | DONE | 18/18 files verified |
| 2. Parent rosters | DONE | 28 parent cards match vault |
| 3. Gateway model | PROPOSED | hermes.nix diff above |
| 4. Telemetry policy | DONE | s2_alive_loop.py patched; zero wiki writes |
| 5. Firecrawl | PROPOSED | configuration.nix diff above |

---
Changelog:
- 2026-07-06 — rulings executed; items 1-2-4 done, 3+5 proposed for rebuild
