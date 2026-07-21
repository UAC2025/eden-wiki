---
title: Receipt Intake — Batch 01 Decision Packet
date: 2026-07-13
scope: Gmail read-only receipt intake
entity: UAC
status: evidence-classified; no financial-system posting performed
---

# Receipt Intake — Batch 01

## BLUF

Two new UAC Nous Research receipt/invoice pairs are classified as **paid receipt evidence** totaling **$100.00**. The invoices are paired duplicate evidence and are **not payables**. No payment, email mutation, or financial-system write occurred.

## Source-backed decisions

| Gmail message | Receipt evidence | Paired invoice | Entity | Category | Amount | Classification | Treatment |
|---|---|---|---|---|---:|---|---|
| `19f43bafc1cd8ac5` — 2026-07-08, “Your receipt from Nous Research Inc. #2391-9585” | `Receipt-2391-9585.pdf`; SHA-256 `e4e8cb7de46b4d863adfda77bcef82e622cd59afc46a6c094e81be3844d05dcd` | `Invoice-EO6GGHDX-0005.pdf`; SHA-256 `bdb0a29cdb281dad3ceddedee843829dfeef8ab629845460b50d2cb014b63a7d` | UAC | software/AI | $50.00 | paid receipt evidence | Record one expense when the approved financial register is available; exclude paired invoice from totals. |
| `19f3db2e224d0623` — 2026-07-07, “Your receipt from Nous Research Inc. #2965-5272” | `Receipt-2965-5272.pdf`; SHA-256 `f326e9ae233be04e9988406bf93af48cee485ca9ef2626def27a1ee7d686be25` | `Invoice-EO6GGHDX-0004.pdf`; SHA-256 `e51d39a3046b5988e781dfb28e49f36d75a654945aefef7f55f53743276b57dd` | UAC | software/AI | $50.00 | paid receipt evidence | Record one expense when the approved financial register is available; exclude paired invoice from totals. |

**Batch paid-receipt total: $100.00.**

## Evidence location

- Intake register: `receipt_attachment_register_receipt-intake-20260713.csv`
- Archived evidence root: `Evidence/`
- Search executed: `has:attachment {receipt invoice statement} after:2026/01/01`

## Controls applied

- Receipt/invoice pairs count once.
- A receipt is not an unpaid payable.
- UAC is kept separate from TNR.
- No tax treatment conclusion is made.
- No financial-system posting is claimed.

## Technical exception

This host has no installed PDF text extractor (`fitz`, `pdftotext`, `mutool`, `qpdf`, and `tesseract` were unavailable). Classification above relies only on Gmail’s source subject, attachment names, amounts exposed in the Gmail payload, and file hashes. Items needing document-content interpretation remain unresolved until a declaratively approved extractor exists.

## Next batch

Process the remaining evidence in this order: (1) receipt/invoice pairs, (2) standalone invoices with explicit balance/due-date proof, (3) statements and no-amount documents as review-only. Do not convert a statement or invoice into a payable without source proof of an unpaid balance and due date.
