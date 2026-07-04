---
title: UAC TNR Entity Separation Rule
type: accounting-control
created: 2026-07-03
entities: [UAC, TNR]
status: active-draft
---

# UAC / TNR Entity Separation Rule

> **DRAFT CONTROL DOCUMENT — NOT LEGAL/TAX ADVICE.** S-1 may use this internally as a control framework. External use, donor sends, grant submissions, filings, or official adoption require Commander approval and appropriate reviewer input.

## Rule
Urban Ark Conservation Inc. and Terra Nova Roots LLC records must remain separated unless a report explicitly states it is cross-entity analysis.

## UAC records
Include nonprofit donations, grants, charitable program expenses, conservation/education records, IRS 990 filings, PA charitable compliance, and board/governance records.

## TNR records
Include commercial farm sales, Schedule F/tax records, product revenue, commercial expenses, and LLC operations.

## S-1 control
Every financial or compliance row must carry an entity field:

```text
entity = UAC | TNR | unknown_review_required
```

Unknown entity rows cannot be used in totals until resolved.
