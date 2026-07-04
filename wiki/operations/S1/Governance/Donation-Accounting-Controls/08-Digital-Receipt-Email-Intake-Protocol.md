---
title: Digital Receipt Email Intake Protocol
type: accounting-control
created: 2026-07-03
entity_scope: [UAC, TNR]
owner: S-1 Personnel / SecretarialAI
status: active-draft
---

# Digital Receipt Email Intake Protocol

## BLUF
Commander will forward digital receipts to email for taxes. S-1 will treat forwarded receipts as source evidence, classify them by entity, file them, and prepare tax/accounting registers without mixing UAC nonprofit and Terra Nova Roots LLC records.

## Intake rule

When a digital receipt arrives by email, SecretarialAI should:

1. preserve the original email and attachments,
2. label the message without deleting or marking read by default,
3. classify entity: `UAC`, `TNR`, or `unknown_review_required`,
4. extract vendor, date, amount, tax, payment method if visible, category, and source message ID,
5. file receipt evidence to Obsidian / evidence store,
6. add row to receipt register,
7. create review task if entity/category/amount is unclear,
8. include source path/message ID in any totals.

## Gmail labels

Recommended labels:

| Label | Use |
|---|---|
| `EDEN-processed` | Receipt was seen by S-1. |
| `Finance/Receipt` | Receipt/invoice/payment evidence. |
| `Finance/UAC` | UAC nonprofit receipt. |
| `Finance/TNR` | Terra Nova Roots LLC receipt. |
| `Finance/Review` | Needs Commander/accountant review. |
| `Taxes/2026` | Tax-year filing bucket, adjusted by receipt date/year. |

## Required extracted fields

| Field | Required | Notes |
|---|---:|---|
| source_message_id | yes | Gmail message ID or exported email path. |
| source_file_path | if attachment/filed | PDF/image/email export path. |
| receipt_date | yes if visible | If missing, use `unknown_review_required`. |
| vendor/payee | yes if visible | Keep exact vendor text. |
| amount | yes if visible | No inferred totals. |
| sales_tax | if visible | Separate if shown. |
| payment_method | if visible | Last 4 only if shown; no credential exposure. |
| entity | yes | UAC/TNR/unknown_review_required. |
| category | yes or review | e.g., feed, equipment, software, filing, office, travel. |
| deductible/tax treatment | no | Accountant review, not S-1 conclusion. |

## Entity classification hints

| Clue | Likely entity | Caveat |
|---|---|---|
| 501(c)(3), donation, grant, filing, nonprofit, animal sanctuary/conservation admin | UAC | Verify if paid by UAC account/card. |
| farm product, sales, Terra Nova Roots, Schedule F, commercial farm expenses | TNR | Verify if paid by TNR/personal account. |
| shared utilities/tools/software | unknown_review_required | May need split or accountant review. |

## Outputs

S-1 should maintain:

- receipt evidence folder,
- receipt intake register,
- unresolved receipt review list,
- monthly/annual source-backed totals by entity,
- accountant export packet when requested.

## Gate

S-1 may classify, file, extract, calculate, and draft reports from forwarded receipts. S-1 may not claim tax treatment, deductibility, or filing position without accountant/Commander approval.
