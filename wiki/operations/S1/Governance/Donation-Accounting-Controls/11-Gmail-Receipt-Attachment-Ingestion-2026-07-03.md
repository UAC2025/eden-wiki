---
title: Gmail Receipt Attachment Ingestion 2026-07-03
type: accounting-intake-register
created: 2026-07-03
source: Gmail attachment API
entity_scope: [UAC, TNR]
---

# Gmail Receipt Attachment Ingestion — 2026-07-03

## BLUF
S-1 downloaded and extracted attachments/body evidence for **20 Gmail messages** matching receipt/invoice/bill/order attachment search. Register rows created: **29**. This is evidence extraction only; no tax treatment conclusions.

- Query: `has:attachment (receipt OR invoice OR bill OR statement OR order) newer_than:365d`
- Evidence folder: `/persist/eden/hermes/workspace/eden-wiki/wiki/operations/S1/Governance/Donation-Accounting-Controls/Evidence/Gmail-Attachments`
- CSV register: `/persist/eden/hermes/workspace/eden-wiki/wiki/operations/S1/Governance/Donation-Accounting-Controls/receipt_attachment_register_2026-07-03.csv`

## Register
| Message ID | Subject | Attachment | Entity | Category | Amount candidates | Review |
|---|---|---|---|---|---|---|
| `19f28b56c00edf3a` | Fwd: Your receipt from Nous Research Inc. #2318-0117 | Invoice-EO6GGHDX-0003.pdf | UAC | software_ai | 50.00 | no |
| `19f28b56c00edf3a` | Fwd: Your receipt from Nous Research Inc. #2318-0117 | Receipt-2318-0117.pdf | UAC | software_ai | 50.00 | no |
| `19f246595de4083d` | Fwd: Heller's Gas - Back Mountain - Statement | Statement_2118487.pdf | UAC | utilities | 484.24; 278.84; 191.28; 470.12; 200.00 | no |
| `19f1e64d8f6cb87f` | Fwd: Invoice from Dependable Disposal of Southern Tier LLC for Urban A | Dependable_Disposal_of_Southern_Tier_LLC_6376 | UAC | waste_disposal | 98.68 | no |
| `19e9aad60e9bc3ea` | LCM Grant — Arapawa Ark Narrative (Submission-Ready, $2K ask) | Livestock-Conservancy-Microgrant-Draft-v2-FIN | UAC | grant |  | yes |
| `19e4ce73cf971b62` | Fwd: Beginning Farmer and Rancher Development Program | FY26-BFRDP-NOFO-P.pdf | UAC | software_ai |  | yes |
| `19e1737edb913a54` | Fwd: Heller's Gas - Back Mountain - Statement | Statement_2118487.pdf | UAC | utilities | 494.60; 484.24; 384.24; 878.84; 100.00 | no |
| `19e1737ca3f38aea` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Invoice-ZVCGN1CH-0017.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | yes |
| `19e1737ca3f38aea` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Receipt-2771-5987-0288.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | yes |
| `19e173796437ac86` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Invoice-ZVCGN1CH-0017.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | yes |
| `19e173796437ac86` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Receipt-2771-5987-0288.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | yes |
| `19e17374a4070e51` | Fwd: Your receipt from Anthropic, PBC #2989-4202-3281 | Invoice-ZVCGN1CH-0018.pdf | unknown_review_required | software_ai | 53.00; 50.00; 3.00 | yes |
| `19e17374a4070e51` | Fwd: Your receipt from Anthropic, PBC #2989-4202-3281 | Receipt-2989-4202-3281.pdf | unknown_review_required | software_ai | 53.00; 50.00; 3.00 | yes |
| `19df4e8bf7178500` | Fwd: Invoice from Dependable Disposal of Southern Tier LLC for Urban A | Dependable_Disposal_of_Southern_Tier_LLC_6376 | UAC | waste_disposal | 100.59 | no |
| `19df4ccfde80d6a1` | Fwd: Heller's Gas - Back Mountain - Statement | Statement_2118487.pdf | UAC | utilities | 494.60; 484.24; 384.24; 878.84; 100.00 | no |
| `19df0ed34dc0f4a6` | Fwd: TNR 2025 Tax Receipt | Statement_2118487.pdf | TNR | utilities | 974.16; 985.16; 1,959.32; 29.39; 9.95 | no |
| `19df0eca607f87c1` | Fwd: Heller's Gas - Back Mountain - Invoice | Invoice EA452E49-BE6D-4414-B9BD-9560D75372DD. | UAC | utilities | 165.00; 9.95; 5.50; 10.83; 191.28 | no |
| `19df0eb3b9b25d03` | Fwd: Your Tractor Supply Receipt | Customer_E_Receipt_2146_36_1065.pdf | unknown_review_required | equipment_hardware |  | yes |
| `19df0ea8d3ef9f5e` | Fwd: Your receipt from Anthropic, PBC #2884-5493-9091 | Invoice-ZVCGN1CH-0016.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | yes |
| `19df0ea8d3ef9f5e` | Fwd: Your receipt from Anthropic, PBC #2884-5493-9091 | Receipt-2884-5493-9091.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | yes |
| `19df0a5453a35cf1` | Fwd: Your receipt from Anthropic, PBC #2826-4596-2114 | Invoice-L0FIYBE9-0008.pdf | UAC | software_ai | 15.90; 15.00; 0.90 | no |
| `19df0a5453a35cf1` | Fwd: Your receipt from Anthropic, PBC #2826-4596-2114 | Receipt-2826-4596-2114.pdf | UAC | software_ai | 15.90; 15.00; 0.90 | no |
| `19df0a50b0e5a7a0` | Fwd: Your receipt from Anthropic, PBC #2808-7751-4791 | Invoice-L0FIYBE9-0010.pdf | UAC | software_ai | 26.50; 25.00; 1.50 | no |
| `19df0a50b0e5a7a0` | Fwd: Your receipt from Anthropic, PBC #2808-7751-4791 | Receipt-2808-7751-4791.pdf | UAC | software_ai | 26.50; 25.00; 1.50 | no |
| `19df0a24cecbd82f` | Fwd: Your Tractor Supply Receipt | Customer_E_Receipt_2146_36_1065.pdf | unknown_review_required | equipment_hardware |  | yes |
| `19c4fb946a80a5c3` | Fwd: Your receipt from Anthropic, PBC #2157-3235-7979 | Invoice-ZVCGN1CH-0003.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | yes |
| `19c4fb946a80a5c3` | Fwd: Your receipt from Anthropic, PBC #2157-3235-7979 | Receipt-2157-3235-7979.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | yes |
| `19c4fb7c224be089` | Fwd: Your receipt from Anthropic, PBC #2541-1806-8382 | Invoice-L0FIYBE9-0005.pdf | UAC | software_ai | 53.00; 50.00; 3.00 | no |
| `19c4fb7c224be089` | Fwd: Your receipt from Anthropic, PBC #2541-1806-8382 | Receipt-2541-1806-8382.pdf | UAC | software_ai | 53.00; 50.00; 3.00 | no |

## Next action
Review `unknown_review_required` rows, then produce source-backed UAC and TNR totals from the CSV register. Totals must cite message IDs and attachment hashes.

