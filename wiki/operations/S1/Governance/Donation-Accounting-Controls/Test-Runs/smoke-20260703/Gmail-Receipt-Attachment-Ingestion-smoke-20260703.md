---
title: Gmail Receipt Attachment Ingestion 2026-07-03
type: accounting-intake-register
created: 2026-07-03
source: Gmail attachment API
entity_scope: [UAC, TNR]
---

# Gmail Receipt Attachment Ingestion — 2026-07-03

## BLUF
S-1 downloaded and extracted attachments/body evidence for **1 Gmail messages** matching receipt/invoice/bill/order attachment search. Register rows created: **2**. This is evidence extraction only; no tax treatment conclusions.

- Query: `has:attachment (receipt OR invoice OR bill OR statement OR order) newer_than:365d`
- Evidence folder: `/persist/eden/hermes/workspace/eden-wiki/wiki/operations/S1/Governance/Donation-Accounting-Controls/Test-Runs/smoke-20260703/Evidence`
- CSV register: `/persist/eden/hermes/workspace/eden-wiki/wiki/operations/S1/Governance/Donation-Accounting-Controls/Test-Runs/smoke-20260703/receipt_attachment_register_smoke-20260703.csv`

## Register
| Message ID | Subject | Attachment | Entity | Category | Amount candidates | Review |
|---|---|---|---|---|---|---|
| `19f28b56c00edf3a` | Fwd: Your receipt from Nous Research Inc. #2318-0117 | Invoice-EO6GGHDX-0003.pdf | UAC | software_ai | 50.00 | no |
| `19f28b56c00edf3a` | Fwd: Your receipt from Nous Research Inc. #2318-0117 | Receipt-2318-0117.pdf | UAC | software_ai | 50.00 | no |

## Next action
Review `unknown_review_required` rows, then produce source-backed UAC and TNR totals from the CSV register. Totals must cite message IDs and attachment hashes.

