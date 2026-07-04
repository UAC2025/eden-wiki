---
title: Digital Receipt Email Search Snapshot 2026-07-03
type: accounting-intake-snapshot
created: 2026-07-03
entity_scope: [UAC, TNR]
source: Gmail metadata search
---

# Digital Receipt Email Search Snapshot — 2026-07-03

## BLUF
S-1 searched Gmail for tax/receipt evidence. Date-bounded 2027 search returned **0 messages**. Recent receipt/invoice/payment/order search returned **49 messages** up to the query cap; many are 2026-forwarded receipts and 2025 tax summaries that should be ingested into the receipt/tax ledger.

## 2027 bounded search
- Query: `(receipt OR invoice OR payment OR order) after:2027/01/01 before:2028/01/01`
- Results: 0
- Interpretation: no Gmail messages currently dated in 2027 were found by this query. If Commander means receipts for the 2027 tax-prep folder/forwarding stream, S-1 will bucket future forwarded receipts under the appropriate tax year from receipt date.

## Recent receipt-like messages sampled
| Date | Subject | From | Message ID |
|---|---|---|---|
| Fri, 3 Jul 2026 11:59:53 -0400 | Fwd: Your receipt from Nous Research Inc. #2318-0117 | Chad McCarthy <president@urbanarkconservation.org> | `19f28b56c00edf3a` |
| Fri, 3 Jul 2026 10:48:32 -0400 | Fwd: Google: We've received your payment for 5055-8248-2261 | Chad McCarthy <president@urbanarkconservation.org> | `19f2874194706079` |
| Thu, 2 Jul 2026 15:54:10 -0400 | Fwd: Heller's Gas - Back Mountain - Statement | Chad McCarthy <info@urbanarkconservation.org> | `19f246595de4083d` |
| Wed, 1 Jul 2026 11:55:40 -0400 | Fwd: Invoice from Dependable Disposal of Southern Tier LLC for Urban Ark Conservation | Chad Mccarthy <chadmmcc@gmail.com> | `19f1e64d8f6cb87f` |
| Mon, 8 Jun 2026 18:07:55 -0400 | Fwd: Your Nous Research Inc. receipt [#1822-9012] | Chad McCarthy <president@urbanarkconservation.org> | `19ea94762fbf2b0e` |
| Mon, 11 May 2026 09:26:27 -0400 | Fwd: Heller's Gas - Back Mountain - Statement | Chad McCarthy <info@urbanarkconservation.org> | `19e1737edb913a54` |
| Mon, 11 May 2026 09:26:19 -0400 | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Chad McCarthy <info@urbanarkconservation.org> | `19e1737ca3f38aea` |
| Mon, 11 May 2026 09:26:04 -0400 | Fwd: Your receipt from Anthropic, PBC #2771-5987-0288 | Chad McCarthy <info@urbanarkconservation.org> | `19e173796437ac86` |
| Mon, 11 May 2026 09:25:46 -0400 | Fwd: Your receipt from Anthropic, PBC #2989-4202-3281 | Chad McCarthy <info@urbanarkconservation.org> | `19e17374a4070e51` |
| Mon, 4 May 2026 17:32:52 -0400 | Fwd: Invoice from Dependable Disposal of Southern Tier LLC for Urban Ark Conservation | Chad Mccarthy <chadmmcc@gmail.com> | `19df4e8bf7178500` |
| Mon, 4 May 2026 17:02:34 -0400 | Fwd: Heller's Gas - Back Mountain - Statement | Chad McCarthy <info@urbanarkconservation.org> | `19df4ccfde80d6a1` |
| Sun, 3 May 2026 22:59:17 -0400 | Fwd: TNR 2025 Tax Receipt | Chad McCarthy <president@urbanarkconservation.org> | `19df0ed34dc0f4a6` |
| Sun, 3 May 2026 22:58:41 -0400 | Fwd: Heller's Gas - Back Mountain - Invoice | Chad McCarthy <info@urbanarkconservation.org> | `19df0eca607f87c1` |
| Sun, 3 May 2026 22:57:07 -0400 | Fwd: Your Tractor Supply Receipt | Chad Mccarthy <chadmmcc@gmail.com> | `19df0eb3b9b25d03` |
| Sun, 3 May 2026 22:56:45 -0400 | Fwd: Your Bill is Available | HQ Ops Urban Ark <operations@urbanarkconservation.org> | `19df0eab1bd57834` |
| Sun, 3 May 2026 22:56:23 -0400 | Fwd: Your receipt from Anthropic, PBC #2884-5493-9091 | Chad McCarthy <info@urbanarkconservation.org> | `19df0ea8d3ef9f5e` |
| Sun, 3 May 2026 21:40:58 -0400 | Fwd: Google: We've received your payment for 5055-8248-2261 | Chad McCarthy <president@urbanarkconservation.org> | `19df0a57f8105656` |
| Sun, 3 May 2026 21:40:41 -0400 | Fwd: Your receipt from Anthropic, PBC #2826-4596-2114 | Chad McCarthy <president@urbanarkconservation.org> | `19df0a5453a35cf1` |
| Sun, 3 May 2026 21:40:26 -0400 | Fwd: Your receipt from Anthropic, PBC #2808-7751-4791 | Chad McCarthy <president@urbanarkconservation.org> | `19df0a50b0e5a7a0` |
| Sun, 3 May 2026 21:40:15 -0400 | Fwd: Simple 990 e-filing receipt. | Chad McCarthy <president@urbanarkconservation.org> | `19df0a4d8888721b` |
| Sun, 3 May 2026 21:39:32 -0400 | Fwd: Your Bill is Available | Chad Mccarthy <chadmmcc@gmail.com> | `19df0a42ef2ad1bb` |
| Sun, 3 May 2026 21:37:28 -0400 | Fwd: Your Tractor Supply Receipt | Chad Mccarthy <chadmmcc@gmail.com> | `19df0a24cecbd82f` |
| Thu, 23 Apr 2026 10:59:08 -0400 | Fwd: Spark Good Local Grant – It is time to set up your payment | Chad McCarthy <president@urbanarkconservation.org> | `19dbada4a35453fc` |
| Thu, 12 Feb 2026 16:08:54 -0500 | Fwd: Claude by Anthropic subscription suspended due to payment issue | Chad Mccarthy <chadmmcc@gmail.com> | `19c53afaf0623375` |
| Wed, 11 Feb 2026 21:40:55 -0500 | Fwd: Your receipt from Anthropic, PBC #2157-3235-7979 | Chad McCarthy <info@urbanarkconservation.org> | `19c4fb946a80a5c3` |
| Wed, 11 Feb 2026 21:40:44 -0500 | Fwd: Your Amazon.com order of "AYWHP 3 Set LoRa...". | Chad McCarthy <info@urbanarkconservation.org> | `19c4fb917a0d3f14` |
| Wed, 11 Feb 2026 21:40:30 -0500 | Fwd: Your Amazon.com order of "USB to RS485 Converter...". | Chad McCarthy <info@urbanarkconservation.org> | `19c4fb8e6aac8799` |
| Wed, 11 Feb 2026 21:39:14 -0500 | Fwd: Your receipt from Anthropic, PBC #2541-1806-8382 | Chad McCarthy <president@urbanarkconservation.org> | `19c4fb7c224be089` |
| Mon, 19 Jan 2026 22:08:58 -0600 | Tax Receipt Summary - Terra Nova Roots LLC 2025 (84 receipts) | operations@urbanarkconservation.org | `19bd9976c3902cfa` |
| Mon, 19 Jan 2026 22:06:05 -0600 | Tax Receipt Summary - Terra Nova Roots LLC 2025 (84 receipts) | operations@urbanarkconservation.org | `19bd994ca9bede40` |

## S-1 action
Create a receipt-ingestion pass that reads these messages, preserves source IDs, classifies UAC/TNR/unknown, extracts amount/date/vendor when visible, and writes rows to the receipt register. Do not mark read/delete/send.

