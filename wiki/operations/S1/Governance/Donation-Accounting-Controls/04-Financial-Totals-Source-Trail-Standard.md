---
title: Financial Totals Source Trail Standard
type: accounting-control
created: 2026-07-03
entity: UAC
status: draft
---

# Financial Totals Source-Trail Standard

> **DRAFT CONTROL DOCUMENT — NOT LEGAL/TAX ADVICE.** S-1 may use this internally as a control framework. External use, donor sends, grant submissions, filings, or official adoption require Commander approval and appropriate reviewer input.

## Rule
S-1 may create financial totals from records Commander provides or from verified connected systems. Every total must be reproducible from retained source rows.

## Required fields per source row

| Field | Required |
|---|---:|
| entity: UAC or TNR | yes |
| date | yes |
| amount | yes |
| direction: income/expense/transfer | yes |
| category | yes |
| source system/document | yes |
| source ID/path | yes |
| notes/restrictions | if any |

## Output standard
Every total report must include:

- total amount,
- date range,
- entity,
- source count,
- excluded records count,
- file/source list,
- unresolved records,
- generation date.

## Prohibited

- No estimates from memory.
- No blended UAC/TNR totals unless explicitly marked as cross-entity analysis.
- No tax conclusion without accountant review.
