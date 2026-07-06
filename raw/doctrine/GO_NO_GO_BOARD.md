---
title: GO/NO-GO Board — real-world outcome readiness per shop
type: doctrine
status: PROPOSED — snapshot 2026-07-06, update as wiring changes
date: 2026-07-06
source_files: []
system_sources:
  - live gateway skill manifest + session history (dashboard API, 2026-07-06)
  - Hermes loop audit 2026-07-02 (wiki/qa) — tool failure evidence
  - parent cards raw/doctrine/parents/ — per-domain BLOCKED lists
---

# GO/NO-GO Board — what can produce real-world outcomes TODAY

**GO** = a loop can close end-to-end on a live surface with current wiring.
**PARTIAL** = real deliverables possible from vault/staged data; live feeds missing.
**NO-GO** = identity preserved, execution blocked on hardware/keys.

| Shop | Verdict | Real outcome available today | Blocked on |
|---|---|---|---|
| **S6_Comms** | **GO** — officer verified 2026-07-06 | Social posts with engagement metrics (dispatch skills + meta-graph-api + reach ledger) | paid channels (gate) |
| **S1_Personnel** | **GO** | Email triage, governance packets, task ledgers, board evidence (already producing into the vault) | Google Workspace key (unverified) |
| **S5_Plans** | **GO** (DevelopmentAI) / PARTIAL (PlansAI) | Repo/skill/tooling changes on branches — fully wired; strategic plans from staged inputs | live capacity/finance feeds |
| **S4_Logistics** | **PARTIAL → GO for Grants** | Grant discovery + application drafts (web research is wired; submission = Commander gate); marketing content drafts; finance/inventory work from staged docs | Farmbrite, bank feeds (gated anyway), CRM |
| **S2_Intel** | **PARTIAL** | Vault fact-checking (CodexAI — fully wired); weather briefs from public APIs (WeatherAI — fixes the dead SITREP weather); forecasts from vault records | all sensors, cameras, MQTT — hardware rebuild |
| **S3_Operations** | **PARTIAL** | Herd/medical record reports, breeding plans, eligibility calendars from vault raw/ records | Farmbrite API key (the single highest-value unblock), live herd DB, all actuators |

## The unblock queue (ranked by outcome-per-effort)

1. **Farmbrite API key** on the gateway — unblocks S3's herd/medical loops, the
   morning SITREP's health checks, and PredictiveAI's inputs. One secret.
2. **Gateway default model** — still `gemini-3.1-pro-preview` (depleted);
   either refund Gemini or set default to gpt-5.5 so cron loops stop being
   born dead. One config change + rebuild.
3. **web_search on the gateway** — `search.firecrawl pip install failed`
   (2026-07-02 audit): blocks WeatherAI/GrantsAI research quality in cron
   context. One dependency fix.
4. **Watchdog timer install** (one command, eden-ops/INSTALL.md) — makes loop
   death visible within 30 minutes instead of days.
5. Google Workspace credentials — unblocks SecretarialAI calendar/docs.

## What this board does NOT claim

No shop is "done." GO means one real loop can close today — THE RULE is
satisfied per-capability, one at a time, and every claim above traces to a
verified skill, session, or audit finding. Sensor-dependent domains stay
honestly NO-GO until hardware exists — no amount of prompt engineering
changes that.
