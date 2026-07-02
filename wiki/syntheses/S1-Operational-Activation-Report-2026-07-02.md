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

## Code and artifacts

- Operational module: `s1_operational/s1_ops.py`
- Data root: `s1_operational/data/`
- Latest verification report: `s1_operational/data/reports/s1_verification_20260702_194830.md`
- Cron script: `.hermes/scripts/s1_inbound_shadow_loop.sh`
- Cron job: `3e5d671ba286` — `S1-Inbound-Task-Governance-Shadow-Loop`, every 30 minutes, local delivery, no-agent script mode.
- E2E verification harness: `s1_verification_harness/s1_e2e_verify.py`
- Harness artifact from verified rerun: `eden-data/s1-verification/20260702T235043Z-1483b30e/S1_E2E_REPORT.md`

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
- No email was marked read.
- No Drive, Calendar, Farmbrite, Wix, or printer write was executed.
- Credential-shaped email content was not copied or used; it was redacted and routed into a secure review task.
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
| Wix | `WIX_API_KEY` unset in Hermes env; credential-bearing email detected but not used | Provision key through approved secret path; first test must be read-only `list_services`/booking query. |
| Himalaya | CLI not installed/configured | Not required for current loop because Google Workspace OAuth works; optional if IMAP path is still desired. |
| Event-driven Mycelium | Current S-1 loop is cron-triggered shadow mode | Replace or supplement with webhook/session injection when source systems can emit events. |

## Next activation order

1. Authorize Hermes SSH on ARCOS and rerun ARCOS audit.
2. Verify printer inventory via `lpstat` and route map against `printer_roles.json`.
3. Provision Wix and Farmbrite credentials through approved secret handling, then run read-only smoke tests.
4. Promote inbound-comms from shadow mode to controlled mode only after review of the first task batch.
5. Add event-driven Mycelium hooks where source systems support them; keep cron only as fallback/heartbeat.
