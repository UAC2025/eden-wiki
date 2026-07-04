---
title: S-1 Action Ledger
type: action-ledger
created: 2026-07-03
owner: S-1 Personnel / TaskAI
status: active
source_files:
  - wiki/operations/S1/Governance/IRS-Annual-Filing-Matrix.md
  - wiki/operations/S1/Governance/PA-Compliance-Matrix.md
  - wiki/operations/S1/Governance/Board-Governance-Packet-Index.md
  - wiki/operations/S1/Governance/Donation-and-Accounting-Controls-Index.md
---

# S-1 Action Ledger — 2026-07-03

## BLUF
TaskAI converted the current S-1 governance/admin gaps into an owned action ledger. This is the next backbone layer: gaps are no longer just prose; each has status, owner, gate, and next action.

## Action register

| ID | Domain | Action | Owner | Status | Gate | Next action |
|---|---|---|---|---|---|---|
| S1-IRS-2016-2024 | IRS compliance | Obtain/locate accepted annual IRS filing evidence for 2016–2024. | GovernanceAI / Commander / accountant | Open | Evidence from Commander/accountant; no inference. | Build Accountant Request Packet listing missing years. |
| S1-PA-BCO | PA compliance | Determine PA charitable registration / BCO status. | GovernanceAI | Open | No filing/submission without Commander approval. | Search Drive/Gmail for BCO/charitable/exemption; if absent, add to accountant request. |
| S1-PA-SALES-TAX | PA compliance | Determine PA sales tax exemption applicability/renewal evidence. | GovernanceAI | Open | Accountant/operator review. | Add to PA compliance request list. |
| S1-BOARD-FORMATION | Board governance | Formal board formation/adoption package needed because UAC has never had a real board. | GovernanceAI / Commander | Draft-ready | Appointment/adoption/signature gate. | Templates created; next is Commander/accountant/legal review. |
| S1-BYLAWS-ADOPT | Board governance | Review/adopt/revise bylaws draft. | GovernanceAI / Commander | Draft-ready | Adoption/signature gate. | Use bylaws adoption resolution template. |
| S1-CHARTER-ADOPT | Board governance | Review/adopt/replace board charter draft. | GovernanceAI / Commander | Draft-ready | Adoption/signature gate. | Use charter adoption/replacement template. |
| S1-BANKING-AUTH | Board governance | Establish banking authority resolution. | GovernanceAI / Commander | Draft-ready | Signature/bank gate. | Use banking authority template. |
| S1-FILING-AUTH | Board governance | Establish filing/compliance authority resolution. | GovernanceAI / Commander | Draft-ready | Signature/submission gate. | Use filing authority template. |
| S1-COI-POLICY | Board controls | Create/adopt conflict-of-interest policy/acknowledgment. | GovernanceAI | Draft-ready | Adoption/signature gate. | Use COI acknowledgment template; decide standalone policy language. |
| S1-DOC-RETENTION | Board controls | Create/adopt document retention policy. | GovernanceAI | Draft-ready | Adoption/signature gate. | Use retention policy template; accountant/legal review. |
| S1-DONATION-POLICY | Donation controls | Create donation acknowledgment policy. | GovernanceAI / SecretarialAI | Evidence-active | Commander approval before operational use/sending. | Packet + Gmail attachment ingestion + review-decision candidate totals created: [[Governance/Donation-Accounting-Controls/15-Receipt-Totals-After-Review-Decisions-2026-07-03]]. |
| S1-DONOR-RECEIPTS | Donation controls | Send donor receipts from verified source records after Commander approval. | SecretarialAI / GovernanceAI | Draft-ready | Send gate + verified donor/payment/source data. | Receipt workflow/template created: [[Governance/Donation-Accounting-Controls/02-Donation-Receipt-Template]]. |
| S1-DONOR-SUBSTANTIATION | Donation controls | Gather/organize major donor substantiation records if any. | SecretarialAI / GovernanceAI | Open | PII/finance handling; no public disclosure. | Search Drive/Gmail for donation acknowledgments/receipts/grants. |
| S1-CPA-CORRESPONDENCE | Accounting controls | Gather accountant/CPA emails/reviews. | SecretarialAI | Open | Credential/privacy limits; no sends. | Search Gmail/Drive for accountant/tax preparer correspondence. |
| S1-DIGITAL-RECEIPTS | Tax records | Ingest forwarded digital receipts from email for tax/accounting records. | SecretarialAI / TaskAI | Active-ready | No tax treatment claims; entity/category review if unclear. | Protocol created: [[Governance/Donation-Accounting-Controls/08-Digital-Receipt-Email-Intake-Protocol]]. |
| S1-TNR-SEPARATION | Entity boundary | Keep TNR Schedule F/tax records separate from UAC nonprofit records. | S-1 / S-4 | Active control | Financial data gate. | Maintain separate packet; do not mix ownership/compliance claims. |
| S1-CERT-HARNESS | S-1 certification | Build parent-agent certification harness for GovernanceAI, SecretarialAI, TaskAI, ProgramsAI. | EDEN / S-1 Officer | Open | No SOTA claim before pass. | Build harness after each parent produces live output. |
| S1-GRANT-SUBMISSION | Grants | Submit approved grants and archive verification evidence. | GovernanceAI / SecretarialAI / S-6 as needed | Draft-ready | Commander must approve the specific grant/submission and credential use. | Checklist created: [[Governance/Donation-Accounting-Controls/05-Grant-Submission-Approval-Verification-Checklist]]. |
| S1-PROGRAMS-OUTPUT | ProgramsAI | Produce program/volunteer/veteran-ag pipeline packet. | ProgramsAI | Open | PII handling; no booking confirmations. | Read Wix/forms/email/Drive surfaces and create pipeline packet. |

## Closed / draft-ready items

- Board formation/adoption templates exist under `wiki/operations/S1/Governance/Board-Formation-Templates/`.
- Bylaws and board charter evidence are filed but are unsigned draft/evidence only.
- 2025 Form 990-N is filed as accepted/submitted evidence.

## Next closeable loop

**Accountant Request Packet** — a one-page packet asking for the exact IRS/PA/accounting evidence still missing:

1. accepted annual IRS filing confirmations for 2016–2024,
2. PA BCO / charitable registration or exemption status,
3. PA sales tax exemption status if applicable,
4. accountant/CPA correspondence or review notes,
5. donation acknowledgment/substantiation records if any.

## S-1 rule

Every new gap must enter this ledger or a successor TaskAI store with owner/status/gate. If it does not enter the ledger, S-1 is relying on Chad's memory, which is failure.
