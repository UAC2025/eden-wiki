---
title: S-1 Full Stand-Up — Intelligence & Gap Analysis
type: synthesis
date: 2026-07-02
tags:
  - synthesis
  - s1-personnel
  - legacy-migration
  - gap-analysis
confidence: medium
source_files:
  - ../eden/_MANIFEST/EDEN_CAPABILITIES_MASTER.md
  - ../eden/_MANIFEST/autonomy/sessions/S1_CAPABILITY_AUDIT_2026-05-06.md
  - ../eden/_MANIFEST/autonomy/charters/TaskAI.md
  - ../eden/_MANIFEST/autonomy/charters/ProgramsAI.md
  - ../eden/_MANIFEST/autonomy/charters/GovernanceAI.md
  - ../eden/_MANIFEST/autonomy/charters/SecretarialAI.md
  - ../eden/_MANIFEST/autonomy/charters/S1_Officer.md
---

# S-1 Full Stand-Up — Intelligence & Gap Analysis

> **BLUF:** The legacy EDEN registry exposed **36 distinct REAL S-1 topics** across four parent agents plus the [[wiki/entities/S1-Personnel|S1_Personnel]] coordinator. On Hermes, roughly a third of that surface is ported (governance/compliance/document doctrine via the `s1-governance-ops` skill), a third is blueprint-only (inbound email, calendar sync), and a third is **not ported at all** (task lifecycle, programs/participants, Wix intake, printing). The single Commander is the sole operator; the highest-leverage remaining stand-up is **inbound-comms + task lifecycle**, activated one loop at a time per THE RULE.

Sources for every claim in this page: the generated capability registry (`_MANIFEST/EDEN_CAPABILITIES_MASTER.md`, regen 2026-06-13), the locked S-1 capability audit (`_MANIFEST/autonomy/sessions/S1_CAPABILITY_AUDIT_2026-05-06.md`), and the four S-1 charters. Per [[concepts/UAC-Canonical-Voice]], no herd counts or observational animal data appear here — this is a systems analysis, not an operational report.

---

## §1 — Full S-1 Capability Inventory

Legend for Hermes status:
- **PORTED** — a native Hermes skill or cron loop covers the function today.
- **PARTIAL** — doctrine/blueprint exists in a Hermes skill but the executable path is unverified or a dependency is missing.
- **NOT PORTED** — no Hermes-side equivalent exists.

Legacy classification is from the registry legend: REAL = reads/writes a real store or emits a real artifact.

### TaskAI — task lifecycle authority (charter: `eden/_MANIFEST/autonomy/charters/TaskAI.md`)

| REAL topic | Function | Hermes status |
|---|---|---|
| `task_create_request` | Persist task from any agent; canonical CRUD entry | **NOT PORTED** — no Hermes task store; cron loops exist but no task DB |
| `task_list_due` | Due/overdue task listing | **NOT PORTED** |
| `task_query` | Task lookup by id/filter | **NOT PORTED** |
| `task_update_status` | Status transitions (pending→completed etc.) | **NOT PORTED** |
| *(charter, not registry)* recurring templates, weather/animal/equipment task triggers | Event-driven task generation | **NOT PORTED** — legacy stubs only, per the 2026-05-06 audit these were extraction stubs even in EDEN |

### ProgramsAI — veteran/first-responder programming (charter: `eden/_MANIFEST/autonomy/charters/ProgramsAI.md`)

| REAL topic | Function | Hermes status |
|---|---|---|
| `participant_register` | Register participant (Wix form / manual) | **NOT PORTED** — depends on Wix webhook intake (§2) |
| `outcomes_record` | Program outcome / KPI capture (grant evidence) | **NOT PORTED** |
| `program_query` | Program schedule + roster read | **NOT PORTED** |
| *(charter)* curriculum generation | AGBA / veteran-program curriculum drafts | **PARTIAL** — content authoring covered generically by `uac-content-system` skill; the legacy `curriculum_generator.py` was import-broken (python-pptx) even in EDEN |

### GovernanceAI — 501c3 + LLC compliance (charter: `eden/_MANIFEST/autonomy/charters/GovernanceAI.md`)

| REAL topic | Function | Hermes status |
|---|---|---|
| `filing_logistics` | Form 990 (UAC) + Schedule F (TNR) draft logistics | **PORTED (doctrine)** — `s1-governance-ops` skill carries the filing-engine doctrine incl. the hard DRAFT-only/never-auto-file gate |
| `compliance_calendar_sync` | Registration/permit/filing deadline calendar | **PARTIAL** — skill defines 30/90-day reminder doctrine; no live deadline store confirmed on Hermes |
| `audit_trail_query` | Hash-chained governance audit log | **PARTIAL** — skill mandates append-only audit log; chain implementation not verified on Hermes |
| `board_meeting_facilitation` | Board minutes / votes / actions | **PORTED (doctrine)** — RFI-default board-records handling in `s1-governance-ops` |
| `signatures_required` | Signature escalation queue | **PARTIAL** — escalation rule stated in skill; no queue mechanism |
| `mailing_dispatch` | Governance mailings | **NOT PORTED** — no outbound postal/print path (see printers gap, §2) |
| `registration_status_query` [STATUS] | SAM.gov / CAGE / UEI snapshot | **PARTIAL** — tracked in skill scope; no live tracker |

### SecretarialAI — administrative operations (charter: `eden/_MANIFEST/autonomy/charters/SecretarialAI.md`)

| REAL topic | Function | Hermes status |
|---|---|---|
| `email_send_request` | Outbound email | **PARTIAL** — `himalaya` CLI is the designated tool but **is not installed** on the Hermes host (verified: `which himalaya` → not found) |
| `document_query`, `docs_action`, `drive_action`, `sheets_action`, `forms_action` | Google Workspace read/write | **PORTED** — `s1-governance-ops` routes through the `google-workspace` skill (`gws` CLI) |
| `pdf_generate_request` | UAC-branded PDFs (intake forms, waivers, certificates) | **PARTIAL** — doctrine in skill; generation pipeline unverified |
| `intake_form_query` | Intake form generation/lookup | **PARTIAL** — same |
| `webform_fill_request` | Web form automation | **NOT PORTED** — browser automation not currently selected on this Hermes install |
| `farmbrite_sync_request` | Farmbrite calendar/task sync | **NOT PORTED** — no Farmbrite API adapter on Hermes (§2) |
| `list_printers`, `print_document`, `print_request` | CUPS print dispatch (canonical paper output for ALL agents) | **NOT PORTED** — printers hang off AEGIS-ARCOS (Pi 5); Hermes host has no CUPS path to them (§2) |
| `compliance_calendar_sync`, `filing_logistics`, `mailing_dispatch`, `signatures_required` | Shared with GovernanceAI | see GovernanceAI rows |
| `task_create_request` | Task creation proxy | **NOT PORTED** (see TaskAI) |
| *(charter)* Wix bookings/contacts/intake ownership | Booking webhook receiver, Contacts CRM | **NOT PORTED** — Wix webhooks gap (§2); note the legacy `wix_integration.py` was already DEAD/pruned in EDEN itself |
| *(charter)* calendar management | Event creation, conflict detection | **PARTIAL** — doctrine in `s1-governance-ops` §4; Google Calendar path available via `gws`, Farmbrite leg missing |

### S1_Personnel coordinator (charter: `eden/_MANIFEST/autonomy/charters/S1_Officer.md`)

| REAL topic | Function | Hermes status |
|---|---|---|
| `s1_delegate_task` | Route tasking to S-1 parents | **PORTED (pattern)** — Hermes `delegate_task` subagents with charter context, per the OpenClaw→Hermes mapping doctrine |
| `s1_domain_picture` | S-1 common operating picture | **PARTIAL** — morning `SITREP-Morning-Loop` cron exists; S-1-specific COP not confirmed |
| `print_document` | Print proxy | **NOT PORTED** |
| `authorize_degradation_response` | Degradation authorization | **NOT PORTED** — n/a in Hermes architecture (no always-on agent fleet to degrade); retire rather than port |
| `authorize_etsy_candle_marketing_launch` | One-off campaign authorization | **NOT PORTED** — one-off; retire |

**Inventory summary:** ~36 distinct REAL S-1 topics in the legacy registry → on Hermes: **~6 ported, ~10 partial, ~15 not ported, ~2–3 retire-not-port.** The pattern mirrors the 2026-05-06 audit's headline in a new key: back then the code existed but had no operator surface; now the *operator surface* (Hermes chat + skills) exists but roughly half the executable backends are not yet re-attached.

---

## §2 — Gap Analysis: Missing Integrations

Four integration seams block full S-1 function. Each was a live (or charter-planned) daemon in the legacy stack; none currently runs under Hermes.

### 2.1 Wix webhooks (bookings, form submissions, contacts)
- **Legacy state:** SecretarialAI charter names Wix Bookings, Contacts CRM, and intake as canonical S-1 territory on the sole in-scope site (`urbanarkconservation.org`, site ace92575); ProgramsAI reflexes fire on `wix.form_submitted` / `wix.booking_received`. Note: `wix_integration.py` was already pruned/DEAD in EDEN — this was a planned revive, not a working port candidate.
- **Hermes gap:** No webhook receiver, no polling loop. Program registrations, tour bookings, and store-driven contacts arrive only as email notifications — which are also unprocessed (see 2.4).
- **Impact:** `eden/_MANIFEST/autonomy/charters/ProgramsAI.md` capabilities are entirely gated behind this seam. Every booking is a manual Commander touch.
- **Port shape:** a cron-scheduled Wix REST API poll (bookings + form submissions since last cursor) is simpler and more robust than standing up a public webhook endpoint; write results to a local store + vault log.

### 2.2 Farmbrite API
- **Legacy state:** `farmbrite_sync.py` (1.5 KB adapter, ALIVE, 1 external caller) synced calendar/tasks; the S1_Officer charter lists Farmbrite as the shop's one live daily input.
- **Hermes gap:** No adapter, no credentials confirmed on this host. Farm-task and calendar state on Farmbrite is invisible to Hermes S-1.
- **Impact:** Calendar management runs one-legged (Google only); the `sync_calendar_to_farmbrite` function has no equivalent.
- **Port shape:** small — the legacy adapter was ~1.5 KB. A thin REST client invoked from a daily cron restores parity.

### 2.3 Printers on ARCOS
- **Legacy state:** SecretarialAI's 2026-04-27 amendment makes it the canonical dispatcher for **all paper printing** — CUPS `lp` wrapper (`print_manager.py`), audit-logged for sensitive jobs (donor receipts, board minutes, governance filings). Printers reach the network via AEGIS-ARCOS (Pi 5, 10.0.4.26, no Docker).
- **Hermes gap:** The Hermes host has no CUPS route to ARCOS-attached printers. `list_printers` / `print_document` / `print_request` have no backend.
- **Impact:** Intake forms, waivers, board minutes, and filing drafts can be *generated* but not *produced on paper* without the Commander manually printing.
- **Port shape:** `ssh urbanarkconsole@10.0.4.26 'lp ...'` from a Hermes skill script — the legacy pattern already ran ARCOS commands over SSH from ARK, so the same seam works from Hermes.

### 2.4 himalaya email polling (inbound comms)
- **Legacy state:** `email_manager.py` was the *most-used* S-1 specialist (5 external callers per the 2026-05-06 audit) — outbound only; the audit-era stack never had a robust IMAP inbound listener either.
- **Hermes gap:** The `inbound-comms-processor` skill blueprint exists (poll → categorize → route receipts to S-4, notices to S-1, bookings to ProgramsAI → mark seen), **but the `himalaya` binary is not installed** on this host. The loop has never run.
- **Impact:** Every inbound email — invoices, grant notices, government correspondence, booking notifications — is a Commander-only touch. This is the widest single funnel of unprocessed administrative load.
- **Port shape:** install `himalaya` (Nix package available), configure IMAP app password for the operations mailbox, dry-run the categorizer read-only before enabling flag-write.

---

## §3 — Risk Assessment: Sole-Operator Labor Shortage

**Operating fact:** the Commander (1SG, active-drilling E-8) is the sole operator of a 21-acre conservation operation plus a 501c3 and an LLC. Every S-1 function not automated is a direct draw on a single person's finite hours, competing with animal husbandry, drill weekends, and physical infrastructure work. The 2026-05-06 audit named the acceptance bar explicitly: *"filings stop piling up, intake forms generate, board records get kept."* That bar is unchanged; only the platform has changed.

**Risk framing:** the dominant risk is not system failure — it is **silent administrative accumulation**: unread notices ripening into compliance misses, unlogged receipts degrading grant reporting, unregistered participants degrading outcome evidence. Compliance deadlines (990, SAM.gov renewal, state registrations) are the only S-1 items with hard external consequences; they anchor the ranking.

### Workload-reduction ranking (highest leverage first)

| Rank | Capability | Why it ranks here |
|---|---|---|
| 1 | **Inbound email triage** (himalaya loop) | Widest funnel; every category of S-1/S-4 work enters here. Daily, unbounded, currently 100% manual. Also the *sensor* that feeds ranks 2–4 — without it the compliance calendar and task list run blind. |
| 2 | **Task lifecycle + reminders** (TaskAI port) | Converts everything else from "Commander must remember" to "system reminds Commander." Deadline-approaching emits at 14/7/3/1 days are the cheapest insurance against the compliance-miss risk. |
| 3 | **Compliance calendar with live deadline store** (GovernanceAI) | Hard external consequences (IRS, SAM.gov, state). Low volume but highest per-item severity. Doctrine already ported; needs a real store + reminder wiring into rank 2. |
| 4 | **Wix booking/registration intake** (ProgramsAI enabler) | Each booking currently costs a manual copy-into-calendar cycle; programs are also the grant-evidence engine, so unlogged participants are lost fundraising value. |
| 5 | **Farmbrite sync** | Removes double-entry between calendars. Moderate, steady friction. |
| 6 | **Filing drafts (990 / Schedule F) executable path** | Seasonal, not daily — but each cycle is many hours. Draft-only gate already in doctrine. |
| 7 | **Print dispatch via ARCOS** | Convenience tier; each print is minutes, not hours. Rises in rank during program season (sign-in sheets, waivers). |
| 8 | **Board records / signature queue** | Low volume; RFI-default anyway, so automation saves little Commander time per event. |

**Residual risks to log:** (a) enabling automated email *actions* (mark-seen, auto-file) before the categorizer is trusted risks silently burying a critical notice — mitigate with a read-only shadow period; (b) any auto-send/auto-file behavior violates the DRAFT-only doctrine in `s1-governance-ops` and must stay operator-gated; (c) per [[concepts/UAC-Canonical-Voice]], any S-1 surface that drafts outbound text (thank-you letters, program pages) inherits the banned-language list — enforcement belongs in the skill, not in the Commander's proofreading time.

---

## §4 — Recommended Activation Order (one loop at a time, per THE RULE)

Strict serial. Each loop is activated, run in shadow/observed mode, and confirmed by the Commander before the next opens — the same discipline the 2026-05-06 audit imposed on its slice sequence.

**Loop 1 — Inbound comms processor.**
Install `himalaya`; configure the operations mailbox. Run the `inbound-comms-processor` loop **read-only** (no mark-seen, no routing writes) for several days; Commander compares its categorization digest against the real inbox. Then enable mark-seen + vault logging. *Exit criterion:* Commander stops opening the inbox first thing; the digest is trusted.

**Loop 2 — Task lifecycle + reminder loop.**
Stand up a minimal task store (SQLite or JSON in the vault workspace) with `task_create_request` / `task_list_due` / `task_update_status` equivalents; wire Loop 1's "Notice/Compliance" and "Booking" categories to create tasks automatically. Add a daily-digest cron (feeds the existing `SITREP-Morning-Loop`). *Exit criterion:* deadline reminders fire at 14/7/3/1 days and appear in the morning SITREP.

**Loop 3 — Compliance calendar, live.**
Populate the deadline store (990, Schedule F, SAM.gov/CAGE/UEI, state registrations, permits) from Commander-adjudicated source documents — never invented dates. Wire into Loop 2's reminder engine. *Exit criterion:* next real compliance deadline is surfaced by the system before the Commander thinks of it.

**Loop 4 — Wix intake poll.**
Cron-poll Wix bookings + form submissions; route program registrations into a participant log and bookings into calendar + Loop 2 tasks. This activates the ProgramsAI surface (`participant_register`, `program_query`). *Exit criterion:* a real booking flows end-to-end with zero manual copying.

**Loop 5 — Farmbrite sync.**
Thin REST adapter; daily two-way calendar/task reconciliation with drift detection (the legacy `wix_drift` pattern, applied to Farmbrite). *Exit criterion:* one week without double-entry.

**Loop 6 — Print dispatch via ARCOS SSH.**
`list_printers` + `print_document` over SSH to 10.0.4.26; audit-log sensitive jobs per the SecretarialAI amendment. *Exit criterion:* an intake form generated and printed without the Commander touching a print dialog.

**Loop 7 — Filing-draft executable path (990 / Schedule F).**
Last, because it is seasonal and the doctrine gate (DRAFT-only, signature escalation) must sit on top of Loops 2–3. *Exit criterion:* a draft package assembled from real records, delivered for Commander signature — never filed autonomously.

**Explicitly retired, not ported:** `authorize_degradation_response`, `authorize_etsy_candle_marketing_launch`, and the legacy STATUS-ONLY alias topics — artifacts of the always-on agent-fleet architecture that Hermes's ephemeral-delegation model makes unnecessary.

---

## Related pages
- [[Night-Ops-Report-July2]] — the July 2 extraction session that produced `s1-governance-ops` and the inbound-comms blueprint
- [[concepts/UAC-Canonical-Voice]] — voice constraints inherited by every S-1 drafting surface
- [[entities/Urban-Ark-Conservation]] · [[entities/Terra-Nova-Roots]]
