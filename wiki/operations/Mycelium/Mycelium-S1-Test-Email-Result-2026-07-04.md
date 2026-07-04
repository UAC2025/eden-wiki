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
