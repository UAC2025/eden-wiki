---
title: S-1 Operational Activation Report — 2026-07-02
type: synthesis
date: 2026-07-02
tags:
  - synthesis
  - s1-personnel
  - operational-verification
  - arcos
confidence: high
source_files:
  - ../../s1_operational/s1_ops.py
  - ../../s1_operational/data/reports/s1_verification_20260702_194830.md
  - ../../.hermes/scripts/s1_inbound_shadow_loop.sh
---

# S-1 Operational Activation Report — 2026-07-02

> **BLUF:** S-1 is now partially operational in Hermes on a verified live loop: Gmail unread headers are pulled through the authorized Google Workspace token, classified in shadow mode, written to an S-1 inbound ledger, and converted into review-gated S-1 tasks. The loop is scheduled every 30 minutes as `S1-Inbound-Task-Governance-Shadow-Loop` and was manually run successfully. ARCOS hardware audit is blocked by SSH authentication, not by code.

## Verified real-world outcome

On 2026-07-02 19:48 EDT, the S-1 loop processed live Gmail data from `operations@urbanarkconservation.org`:

- **6** unread Gmail messages observed.
- **6** inbound ledger entries written.
- **4** operator-review tasks created/updated from real inbound messages:
  - Heller's Gas statement → S4/Finance + S1/Filing review task.
  - Dependable Disposal invoice → S4/Finance + S1/Filing review task.
  - Anthropic privacy-policy notice → S1/Governance review task.
  - Wix Keys message → secure credential-review task; credential-shaped text was redacted and not used.
- **3** governance deadlines checked and stored:
  - IRS Form 990 draft review — due 2027-05-15.
  - PA BCO-10 annual report check — due 2026-12-31.
  - Insurance renewal review — due 2027-01-01.
- **1** internal ProgramsAI verification fixture persisted to prove ProgramsAI-compatible store read/write.

After Commander authorization to use email-held credentials, EDEN also executed the S-1 controlled-action phase:

- The credential-bearing Gmail message `Wix Keys` was read and used for a **read-only Wix smoke test**.
- The token was used transiently and **not printed or persisted**.
- Wix Bookings API verification succeeded against canonical UAC site `9a847b4e-ac97-4710-8ec8-472aab0e6551`:
  - `bookings/v2/services/query` → HTTP 200, **2** services observed.
  - `bookings/v2/bookings/query` → HTTP 200, **8** bookings observed.
- The UUID in the email body (`b22a55a0-...`) was tested and returned Wix 404 `meta-site ... not found`; the canonical site ID remained correct.
- A sanitized Wix snapshot was written to `s1_operational/data/wix/wix_bookings_snapshot.json`; contact names/emails/phones are hashed only.
- **8** Wix booking review tasks were created/updated in the S-1 task store.
- The 6 processed Gmail messages were labeled and marked read using existing Gmail labels:
  - invoices/statements → `Bills`, `Bills/Open`, `EDEN-processed`.
  - compliance/notice → `UAC`, `EDEN-processed`.
  - credential-bearing Wix key message → `Automation`, `EDEN-processed`.
  - marketing/vendor noise → `Promos`, `EDEN-processed`.

## Code and artifacts

- Operational module: `s1_operational/s1_ops.py`
- Data root: `s1_operational/data/`
- Latest verification report: `s1_operational/data/reports/s1_verification_20260702_194830.md`
- Cron script: `.hermes/scripts/s1_inbound_shadow_loop.sh`
- Cron job: `3e5d671ba286` — `S1-Inbound-Task-Governance-Shadow-Loop`, every 30 minutes, local delivery, no-agent script mode.
- E2E verification harness: `s1_verification_harness/s1_e2e_verify.py`
- Harness artifact from verified rerun: `eden-data/s1-verification/20260702T235043Z-1483b30e/S1_E2E_REPORT.md`
- Wix read-only probe: `s1_operational/wix_readonly_probe.py`
- Wix bookings sync: `s1_operational/wix_bookings_sync.py`
- Gmail categorizer: `s1_operational/gmail_categorize.py`

## E2E harness verification

After the live Gmail shadow loop was installed, a separate S-1 verification harness was present and rerun by EDEN:

```bash
cd /persist/eden/hermes/workspace && /persist/eden/hermes/workspace/.venv/bin/python s1_verification_harness/s1_e2e_verify.py
```

Actual rerun result: **PASS** for all required checks:

- `task_schema`
- `program_schema`
- `governance_schema`
- `fixture_inbound_route`
- `booking_registration_route`

Optional probes remained blocked/skipped:

- `arcos_printers`: **SKIP** — `Permission denied (publickey,password)`.
- `live_gmail_unread`: **SKIP** in this harness because it is designed around `himalaya`, which is not installed; live Gmail is separately verified through the Google Workspace Python fallback in the S-1 operational loop.

## Safety gates preserved

- No email was sent.
- In the initial shadow run, no email was marked read. After explicit Commander authorization, 6 already-processed messages were labeled and marked read.
- No Drive, Calendar, Farmbrite, Wix, or printer write was executed.
- Wix access was read-only: service and booking queries only.
- Credential-shaped email content was initially redacted and routed into a secure review task.
- After explicit Commander authorization, the Wix credential was used transiently for read-only API verification, but the secret value was not printed or persisted.
- Compliance filings remain draft/review-only; no filing or signature action was attempted.

## ARCOS status

ARCOS target: `urbanarkconsole@10.0.4.26`.

Attempted read-only probe:

```bash
ssh -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=accept-new urbanarkconsole@10.0.4.26 'lpstat -p -d; echo ---; hostname; uname -a'
```

Actual result:

```text
Permission denied (publickey,password).
```

Therefore the ARCOS hardware inventory — CUPS printers, USB devices, serial devices, LoRa/AdvanSync/SPLat services, voice/TTS services — is **not yet verified from Hermes**. This is the standing wall.

Hermes public key available for ARCOS authorization:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBOSugXK7oeBTMR+U3L66uJ0EBfVdQQoQTpWTs/RR3X/ hermes@nixos
```

## Remaining gaps to full S-1 shop

| Gap | Current state | Closure requirement |
|---|---|---|
| ARCOS hardware layer | SSH denied | Add Hermes public key to ARCOS `urbanarkconsole` authorized keys, then rerun full hardware audit. |
| Printer real-world verification | Not possible until ARCOS SSH works | Verify `lpstat -p -d`; then do a non-printing dry route check; physical print remains operator gate if > routine. |
| Farmbrite | `FARMBRITE_API_KEY` unset in Hermes env | Provision key through an approved secret path; first test must be read-only. |
| Wix | Read-only API verification succeeded from authorized Gmail-held credential; not persisted as a system secret | Provision key through approved persistent secret path for autonomous recurring sync, or keep manual/session-scoped credential use. |
| Himalaya | CLI not installed/configured | Not required for current loop because Google Workspace OAuth works; optional if IMAP path is still desired. |
| Event-driven Mycelium | Current S-1 loop is cron-triggered shadow mode | Replace or supplement with webhook/session injection when source systems can emit events. |

## Next activation order

1. Authorize Hermes SSH on ARCOS and rerun ARCOS audit.
2. Verify printer inventory via `lpstat` and route map against `printer_roles.json`.
3. Provision Farmbrite credentials through approved secret handling, then run read-only smoke tests.
4. Decide whether to persist the Wix key via the approved secret path for autonomous recurring booking sync.
5. Promote inbound-comms from shadow mode to controlled mode only after review of the first task batch.
6. Add event-driven Mycelium hooks where source systems support them; keep cron only as fallback/heartbeat.
