---
title: Receipt Commander Decisions Applied 2026-07-04
type: receipt-decision-packet
created: 2026-07-04
status: commander-corrected
---

# Receipt Commander Decisions Applied — 2026-07-04

## BLUF
Commander corrected Heller’s Gas classification: **all Heller’s Gas rows are TNR**. S-1 applied Commander decisions for Heller’s, TNR 2025 tax receipt, Anthropic, and Tractor Supply, then rebuilt decisions.

## Applied Commander correction
- Heller’s Gas: **TNR** for all Heller’s rows.
- Heller’s Gas `19f246595de4083d`: amount `$484.24`.
- TNR 2025 Tax Receipt `19df0ed34dc0f4a6`: amount `$985.16`.
- Anthropic receipts: **UAC**.
- Tractor Supply receipts: **TNR**.

## Verified candidate rows
| Message ID | Subject | Entity | Category | Amount | Reason |
|---|---|---|---|---:|---|
| `19f28b56c00edf3a` | Fwd: Your receipt from Nous Research Inc. #2318-0117 | UAC | software_ai | $50.00 | single_amount_known_entity |
| `19f246595de4083d` | Fwd: Heller's Gas - Back Mountain - Statement | TNR | utilities | $484.24 | commander_corrected_hellers_tnr_selected_amount |
| `19f1e64d8f6cb87f` | Fwd: Invoice from Dependable Disposal of Southern Tier LLC f | UAC | waste_disposal | $98.68 | single_amount_known_entity |
| `19e1737edb913a54` | Fwd: Heller's Gas - Back Mountain - Statement | TNR | utilities | $191.28 | resolved_amount_from_attachment_text |
| `19e1737ca3f38aea` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | UAC | software_ai | $26.50 | resolved_amount_from_attachment_text |
| `19e173796437ac86` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | UAC | software_ai | $26.50 | resolved_amount_from_attachment_text |
| `19e17374a4070e51` | Fwd: Your receipt from Anthropic, PBC #2989-4202-3281 | UAC | software_ai | $53.00 | resolved_amount_from_attachment_text |
| `19df4e8bf7178500` | Fwd: Invoice from Dependable Disposal of Southern Tier LLC f | UAC | waste_disposal | $100.59 | single_amount_known_entity |
| `19df0ed34dc0f4a6` | Fwd: TNR 2025 Tax Receipt | TNR | utilities | $985.16 | commander_selected_tnr_tax_receipt_amount |
| `19df0ea8d3ef9f5e` | Fwd: Your receipt from Anthropic, PBC #2884-5493-9091 | UAC | software_ai | $26.50 | resolved_amount_from_attachment_text |
| `19df0a5453a35cf1` | Fwd: Your receipt from Anthropic, PBC #2826-4596-2114 | UAC | software_ai | $15.90 | resolved_amount_from_attachment_text |
| `19df0a50b0e5a7a0` | Fwd: Your receipt from Anthropic, PBC #2808-7751-4791 | UAC | software_ai | $26.50 | resolved_amount_from_attachment_text |
| `19c4fb946a80a5c3` | Fwd: Your receipt from Anthropic, PBC #2157-3235-7979 | UAC | software_ai | $26.50 | resolved_amount_from_attachment_text |
| `19c4fb7c224be089` | Fwd: Your receipt from Anthropic, PBC #2541-1806-8382 | UAC | software_ai | $53.00 | resolved_amount_from_attachment_text |
