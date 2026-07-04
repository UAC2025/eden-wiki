---
title: Receipt Totals After Review Decisions 2026-07-03
type: accounting-totals-candidate
created: 2026-07-03
status: candidate-not-final
entity_scope: [UAC, TNR]
---

# Receipt Totals After Review Decisions — 2026-07-03

## BLUF
S-1 rebuilt candidate totals using only rows marked `verified_candidate` by the review decision packet. Verified rows totaled: **9**. These are candidate accounting totals, not tax conclusions.

## Totals
| Entity | Category | Candidate total |
|---|---|---:|
| UAC | software_ai | $145.40 |
| UAC | utilities | $573.84 |
| UAC | waste_disposal | $199.27 |

## Source rows
| Message ID | Subject | File | Entity | Category | Amount | Decision reason | SHA256 |
|---|---|---|---|---|---:|---|---|
| `19f28b56c00edf3a` | Fwd: Your receipt from Nous Research Inc. #2318-0117 | Invoice-EO6GGHDX-0003.pdf | UAC | software_ai | $50.00 | single_amount_known_entity | `6b0cc7bf2748...` |
| `19f1e64d8f6cb87f` | Fwd: Invoice from Dependable Disposal of Southern Tier  | Dependable_Disposal_of_Southern_Tie | UAC | waste_disposal | $98.68 | single_amount_known_entity | `f97279cb8305...` |
| `19e1737edb913a54` | Fwd: Heller's Gas - Back Mountain - Statement | Statement_2118487.pdf | UAC | utilities | $191.28 | resolved_amount_from_attachment_text | `49f97fee96be...` |
| `19df4e8bf7178500` | Fwd: Invoice from Dependable Disposal of Southern Tier  | Dependable_Disposal_of_Southern_Tie | UAC | waste_disposal | $100.59 | single_amount_known_entity | `c2735e8ee993...` |
| `19df4ccfde80d6a1` | Fwd: Heller's Gas - Back Mountain - Statement | Statement_2118487.pdf | UAC | utilities | $191.28 | resolved_amount_from_attachment_text | `49f97fee96be...` |
| `19df0eca607f87c1` | Fwd: Heller's Gas - Back Mountain - Invoice | Invoice EA452E49-BE6D-4414-B9BD-956 | UAC | utilities | $191.28 | resolved_amount_from_attachment_text | `d2b696d75a5a...` |
| `19df0a5453a35cf1` | Fwd: Your receipt from Anthropic, PBC #2826-4596-2114 | Invoice-L0FIYBE9-0008.pdf | UAC | software_ai | $15.90 | resolved_amount_from_attachment_text | `bfd92bc07515...` |
| `19df0a50b0e5a7a0` | Fwd: Your receipt from Anthropic, PBC #2808-7751-4791 | Invoice-L0FIYBE9-0010.pdf | UAC | software_ai | $26.50 | resolved_amount_from_attachment_text | `2ffefb962ae7...` |
| `19c4fb7c224be089` | Fwd: Your receipt from Anthropic, PBC #2541-1806-8382 | Invoice-L0FIYBE9-0005.pdf | UAC | software_ai | $53.00 | resolved_amount_from_attachment_text | `580762600266...` |

## Controls
- Only `verified_candidate` rows are totaled.
- Commander-review, amount-review, and excluded rows are not totaled.
- Duplicate receipt/invoice pairs remain excluded from totals.
- Totals cite message IDs and attachment hashes for audit trail.
