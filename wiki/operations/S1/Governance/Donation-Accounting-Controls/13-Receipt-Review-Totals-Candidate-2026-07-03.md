---
title: Receipt Review and Totals Candidate 2026-07-03
type: accounting-review-packet
created: 2026-07-03
status: candidate-not-final
entity_scope: [UAC, TNR]
---

# Receipt Review + Totals Candidate — 2026-07-03

## BLUF
S-1 built candidate totals from the attachment register. Total source rows: **29**. Totalable rows: **3**. Review rows: **26**. These are **candidate accounting totals**, not tax conclusions.

## Candidate totals by entity/category
| Entity | Category | Candidate total |
|---|---|---:|
| UAC | software_ai | $50.00 |
| UAC | waste_disposal | $199.27 |

## Totalable source rows
| Message ID | Subject | File | Entity | Category | Amount | SHA256 |
|---|---|---|---|---|---:|---|
| `19f28b56c00edf3a` | Fwd: Your receipt from Nous Research Inc. #2318-0117 | Invoice-EO6GGHDX-0003.pdf | UAC | software_ai | $50.00 | `6b0cc7bf2748...` |
| `19f1e64d8f6cb87f` | Fwd: Invoice from Dependable Disposal of Southern Tier LLC f | Dependable_Disposal_of_Southern_Tier_LLC | UAC | waste_disposal | $98.68 | `f97279cb8305...` |
| `19df4e8bf7178500` | Fwd: Invoice from Dependable Disposal of Southern Tier LLC f | Dependable_Disposal_of_Southern_Tier_LLC | UAC | waste_disposal | $100.59 | `c2735e8ee993...` |

## Review queue
| Message ID | Subject | File | Entity | Category | Amount candidates | Reason |
|---|---|---|---|---|---|---|
| `19f28b56c00edf3a` | Fwd: Your receipt from Nous Research Inc. #2318-0117 | Receipt-2318-0117.pdf | UAC | software_ai | 50.00 | duplicate_receipt_invoice_pair |
| `19f246595de4083d` | Fwd: Heller's Gas - Back Mountain - Statement | Statement_2118487.pdf | UAC | utilities | 484.24; 278.84; 191.28; 470.12; 200.00 | multiple_amount_candidates |
| `19e9aad60e9bc3ea` | LCM Grant — Arapawa Ark Narrative (Submission-Ready, $2K ask | Livestock-Conservancy-Microgrant-Draft-v | UAC | grant |  | needs_review_flag |
| `19e4ce73cf971b62` | Fwd: Beginning Farmer and Rancher Development Program | FY26-BFRDP-NOFO-P.pdf | UAC | software_ai |  | needs_review_flag |
| `19e1737edb913a54` | Fwd: Heller's Gas - Back Mountain - Statement | Statement_2118487.pdf | UAC | utilities | 494.60; 484.24; 384.24; 878.84; 100.00 | multiple_amount_candidates |
| `19e1737ca3f38aea` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Invoice-ZVCGN1CH-0017.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | needs_review_flag |
| `19e1737ca3f38aea` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Receipt-2771-5987-0288.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | needs_review_flag |
| `19e173796437ac86` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Invoice-ZVCGN1CH-0017.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | needs_review_flag |
| `19e173796437ac86` | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Receipt-2771-5987-0288.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | needs_review_flag |
| `19e17374a4070e51` | Fwd: Your receipt from Anthropic, PBC #2989-4202-3281 | Invoice-ZVCGN1CH-0018.pdf | unknown_review_required | software_ai | 53.00; 50.00; 3.00 | needs_review_flag |
| `19e17374a4070e51` | Fwd: Your receipt from Anthropic, PBC #2989-4202-3281 | Receipt-2989-4202-3281.pdf | unknown_review_required | software_ai | 53.00; 50.00; 3.00 | needs_review_flag |
| `19df4ccfde80d6a1` | Fwd: Heller's Gas - Back Mountain - Statement | Statement_2118487.pdf | UAC | utilities | 494.60; 484.24; 384.24; 878.84; 100.00 | multiple_amount_candidates |
| `19df0ed34dc0f4a6` | Fwd: TNR 2025 Tax Receipt | Statement_2118487.pdf | TNR | utilities | 974.16; 985.16; 1,959.32; 29.39; 9.95 | multiple_amount_candidates |
| `19df0eca607f87c1` | Fwd: Heller's Gas - Back Mountain - Invoice | Invoice EA452E49-BE6D-4414-B9BD-9560D753 | UAC | utilities | 165.00; 9.95; 5.50; 10.83; 191.28 | multiple_amount_candidates |
| `19df0eb3b9b25d03` | Fwd: Your Tractor Supply Receipt | Customer_E_Receipt_2146_36_1065.pdf | unknown_review_required | equipment_hardware |  | needs_review_flag |
| `19df0ea8d3ef9f5e` | Fwd: Your receipt from Anthropic, PBC #2884-5493-9091 | Invoice-ZVCGN1CH-0016.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | needs_review_flag |
| `19df0ea8d3ef9f5e` | Fwd: Your receipt from Anthropic, PBC #2884-5493-9091 | Receipt-2884-5493-9091.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | needs_review_flag |
| `19df0a5453a35cf1` | Fwd: Your receipt from Anthropic, PBC #2826-4596-2114 | Invoice-L0FIYBE9-0008.pdf | UAC | software_ai | 15.90; 15.00; 0.90 | multiple_amount_candidates |
| `19df0a5453a35cf1` | Fwd: Your receipt from Anthropic, PBC #2826-4596-2114 | Receipt-2826-4596-2114.pdf | UAC | software_ai | 15.90; 15.00; 0.90 | multiple_amount_candidates |
| `19df0a50b0e5a7a0` | Fwd: Your receipt from Anthropic, PBC #2808-7751-4791 | Invoice-L0FIYBE9-0010.pdf | UAC | software_ai | 26.50; 25.00; 1.50 | multiple_amount_candidates |
| `19df0a50b0e5a7a0` | Fwd: Your receipt from Anthropic, PBC #2808-7751-4791 | Receipt-2808-7751-4791.pdf | UAC | software_ai | 26.50; 25.00; 1.50 | multiple_amount_candidates |
| `19df0a24cecbd82f` | Fwd: Your Tractor Supply Receipt | Customer_E_Receipt_2146_36_1065.pdf | unknown_review_required | equipment_hardware |  | needs_review_flag |
| `19c4fb946a80a5c3` | Fwd: Your receipt from Anthropic, PBC #2157-3235-7979 | Invoice-ZVCGN1CH-0003.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | needs_review_flag |
| `19c4fb946a80a5c3` | Fwd: Your receipt from Anthropic, PBC #2157-3235-7979 | Receipt-2157-3235-7979.pdf | unknown_review_required | software_ai | 26.50; 25.00; 1.50 | needs_review_flag |
| `19c4fb7c224be089` | Fwd: Your receipt from Anthropic, PBC #2541-1806-8382 | Invoice-L0FIYBE9-0005.pdf | UAC | software_ai | 53.00; 50.00; 3.00 | multiple_amount_candidates |
| `19c4fb7c224be089` | Fwd: Your receipt from Anthropic, PBC #2541-1806-8382 | Receipt-2541-1806-8382.pdf | UAC | software_ai | 53.00; 50.00; 3.00 | multiple_amount_candidates |

## Controls
- Duplicate receipt/invoice pairs are not double-counted.
- Rows with multiple amount candidates are routed to review.
- Unknown entity rows are routed to review.
- Message IDs and attachment hashes are retained for audit trail.
- No tax treatment or deductibility conclusion is made.
