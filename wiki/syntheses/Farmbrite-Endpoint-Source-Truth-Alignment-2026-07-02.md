---
title: Farmbrite Endpoint and EDEN Source-of-Truth Alignment — 2026-07-02
type: synthesis
date: 2026-07-02
tags:
  - synthesis
  - farmbrite
  - s1-personnel
  - database-alignment
confidence: high
source_files:
  - ../../eden/integrations/farmbrite/farmbrite_client_v2.py
  - ../../eden/data/migrations/farmbrite_schema_LIVE_20260421.json
  - ../../eden/data/migrations/farmbrite_drift_report_20260421.json
  - ../../s1_operational/data/farmbrite/farmbrite_readonly_schema_probe.json
  - ../../s1_operational/data/farmbrite/farmbrite_endpoint_map_from_legacy.json
  - ../../s1_operational/data/farmbrite/farmbrite_schema_alignment_report.md
---

# Farmbrite Endpoint and EDEN Source-of-Truth Alignment — 2026-07-02

> **BLUF:** The Farmbrite map already exists in the legacy codebase. The canonical technical source is `eden/integrations/farmbrite/farmbrite_client_v2.py`, backed by the captured live endpoint schema `eden/data/migrations/farmbrite_schema_LIVE_20260421.json` and drift report `farmbrite_drift_report_20260421.json`. EDEN has now generated a Hermes-side source-of-truth SQLite schema at `s1_operational/data/farmbrite/eden_farmbrite_source.db` so EDEN tables match Farmbrite endpoint fields before any push sync is enabled.

## Commander doctrine

- **EDEN is the source of truth.**
- Farmbrite is an external operational surface / projection target.
- Pushes to Farmbrite must originate from EDEN-owned records.
- Farmbrite IDs are external references, not primary truth.
- No animal/health/breeding fact may be invented from schema files; live EDEN records remain the factual source.

## Verified live Farmbrite access

The Commander supplied a Farmbrite calendar subscription URL and Farmbrite API credential in-session. EDEN used the credential for read-only verification and did not print the secret.

Read-only API smoke test result: **success**.

| Endpoint | HTTP | Observed total records |
|---|---:|---:|
| `/animals` | 200 | 0 |
| `/tasks` | 200 | 1 |
| `/contacts` | 200 | 2 |
| `/tools` | 200 | 0 |
| `/inventory_types` | 200 | 4 |
| `/transactions` | 200 | 4 |
| `/activities` | 200 | 0 |
| `/places` | 200 | 5 |
| `/products` | 200 | 1 |
| `/orders` | 200 | 2 |
| `/warehouses` | 200 | 6 |
| `/plants` | 200 | 1 |
| `/crops` | 200 | 0 |
| `/plots` | 200 | 0 |
| `/climate_gauges` | 200 | 4 |
| `/climate_logs` | 200 | 300 |
| Calendar subscription ICS | 200 | 0 events in current feed |

## Verified EDEN → Farmbrite push

EDEN executed one controlled low-risk live push to verify the source-of-truth path:

- EDEN source task: `task_wix_service_brand_language_review`.
- Farmbrite endpoint: `POST /tasks`.
- Farmbrite returned ID: `6a470094cd898777a40a5c0a`.
- Readback: `GET /tasks/6a470094cd898777a40a5c0a` returned HTTP 200.
- Readback proof fields: title `Review Wix service names for UAC canonical voice`, status `Open`, and EDEN source task ID present in the Farmbrite description.

This proves the first real EDEN-owned record can project into Farmbrite. It does **not** authorize bulk push of animal, health, breeding, or financial records without source-of-truth validation.

## Endpoint map sources

| Artifact | Role |
|---|---|
| `eden/integrations/farmbrite/farmbrite_client_v2.py` | Gold client: 120+ method calls across animals, tasks, contacts, equipment/tools, inventory, transactions, places, crops, climate, notes/files/photos, etc. |
| `eden/data/migrations/farmbrite_schema_LIVE_20260421.json` | Captured live Farmbrite field schema by endpoint. |
| `eden/data/migrations/farmbrite_drift_report_20260421.json` | Existing drift report showing where EDEN DB tables were missing Farmbrite fields. |
| `s1_operational/data/farmbrite/farmbrite_endpoint_map_from_legacy.json` | Fresh Hermes-generated AST endpoint map from the legacy client. |
| `s1_operational/data/farmbrite/farmbrite_readonly_schema_probe.json` | Fresh read-only API probe results and current field keys where records exist. |
| `s1_operational/data/farmbrite/eden_farmbrite_source.db` | New EDEN-owned SQLite schema aligned to Farmbrite fields. |

## EDEN schema alignment result

EDEN created/updated `s1_operational/data/farmbrite/eden_farmbrite_source.db` with **27 Farmbrite-compatible tables** plus metadata/sync-log tables.

Core tables include:

| Table | Field count after alignment |
|---|---:|
| `animals` | 77 |
| `tasks` | 40 |
| `contacts` | 21 |
| `inventory_types` | 27 |
| `transactions` | 32 |
| `orders` | 43 |
| `climate_logs` | 23 |
| `climate_gauges` | 15 |
| `places` | 19 |
| `plants` | 42 |

Every table includes EDEN sync fields:

- `id`
- `farmbrite_id`
- `eden_updated_at`
- `farmbrite_updated_at`
- `sync_status`
- `raw_json`

This keeps EDEN primary while preserving Farmbrite compatibility.

## Current gap

The schema is aligned and a single EDEN→Farmbrite task push is proven. Bulk sync is not yet enabled. The reason is not authentication; the API key works. The remaining gap is **source-of-truth data policy and mapping discipline**:

1. Identify the EDEN-owned table/record that should project to Farmbrite.
2. Confirm all required Farmbrite endpoint fields exist in EDEN.
3. Transform EDEN record → Farmbrite payload.
4. Push to Farmbrite.
5. Store returned Farmbrite ID in `farmbrite_id`.
6. Use future updates as EDEN → Farmbrite, not Farmbrite → EDEN overwrite.

## Next required implementation

1. Harden `farmbrite_task_sync.py` with dedupe, update-vs-create behavior, and durable secret provisioning.
2. Keep **tasks** as the first live sync domain — lowest-risk S-1/S-4 workflow and already live in S-1.
3. Add contacts, inventory, transactions, tools/equipment, and finally animal records after source-of-truth validation.
4. Animal/health/breeding records must be last because incorrect projection there would violate EDEN's no-fabrication doctrine.

## Push priority

| Priority | Domain | Why |
|---:|---|---|
| 1 | Tasks | Lowest risk; directly supports S-1 closure loop. |
| 2 | Contacts | Supports bookings/vendors/donors; PII handling required. |
| 3 | Inventory | Operationally useful; moderate risk. |
| 4 | Transactions | Financial records; requires S-4 validation before push. |
| 5 | Equipment/tools | Needs ARCOS/S-4 audit alignment. |
| 6 | Animals/health/breeding | Highest factual-risk; only after live EDEN animal records are validated. |
