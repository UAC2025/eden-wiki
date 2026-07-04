---
title: Mycelium S-1 Test Email Result 2026-07-04
type: live-event-test
created: 2026-07-04
status: pass-adapted
owner: EDEN / S-1
---

# Mycelium S-1 Test Email Result — 2026-07-04

## BLUF
Commander sent a live test email. Mycelium detected it on the first manual watch pass, routed it to S-1, created an artifact, and emitted audit evidence. Initial classifier marked it `unclassified`; adaptation updated order-fulfillment subjects as `receipt_or_invoice`, reran the event handler, created the correct S-1 task, and added a regression test.

## Live email observed

- Message ID: `19f2cd821068447e`
- Subject: `Fwd: Order #PF157768988 has been sent out`
- Source: Gmail live query
- Artifact: `s1_operational/run/mycelium_s1_gmail_4ea6647e651641914cfdee6d.json`

## Initial result

| Field | Value |
|---|---|
| Event ID | `4ea6647e651641914cfdee6d` |
| Initial category | `unclassified` |
| Initial action | local artifact/ledger only; no external side effects |

## Adaptation

Classifier updated so order-fulfillment signals route as receipt/order financial/admin work:

- `order #`
- `has been sent out`
- `shipped`
- `fulfillment`

Regression test added:

`test_order_fulfillment_email_routes_as_receipt_or_invoice`

## Corrected result

| Field | Value |
|---|---|
| Category | `receipt_or_invoice` |
| Priority | `high` |
| Route | `S4/Finance + S1/Filing` |
| Task | `task_97961e74f08f` |
| Task title | `Process inbound receipt or invoice: Fwd: Order #PF157768988 has been sent out` |
| Audit event | `ff38a85daeb31663df5c79afe06908ca16c5bde6ac540486ebd08d528bc39d54` |

## Safety
No email was sent, deleted, marked read, submitted, or replied to. This was local S-1 routing and audit only.

## Labeling fix

Commander correctly flagged that routed emails should not just sit in local S-1 state. Mycelium now applies the same Gmail label posture as the S-1 alive loop while preserving the mark-read gate.

Applied to this message:

| Label action | Result |
|---|---|
| Add `Bills` | PASS (`Label_11`) |
| Add `Bills/Open` | PASS (`Label_12`) |
| Add `EDEN-processed` | PASS (`Label_13`) |
| Remove `UNREAD` | NOT DONE — intentionally gated |

Live Gmail verification after the fix showed labels:

```text
UNREAD
IMPORTANT
Label_11
CATEGORY_PERSONAL
SENT
Label_12
INBOX
Label_13
```

Audit event for labeling fix:

`c22ad932e5a4af60f91f7b9ad5714db7ad7f092ef49857cb78e5b59839b64478`
