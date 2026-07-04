---
title: ProgramsAI Pipeline Packet 2026-07-04
type: programs-pipeline
created: 2026-07-04
status: live-output
owner: ProgramsAI
pii: hashed/contact-redacted
---

# ProgramsAI Pipeline Packet — 2026-07-04

## BLUF
ProgramsAI produced its first live/read-surface pipeline packet from existing PII-safe Wix booking snapshot and Gmail program-search metadata. No bookings were confirmed, changed, or contacted.

## Wix booking snapshot
- Services observed: **2**
- Bookings observed: **8**
- Status counts: `{"CANCELED": 1, "CONFIRMED": 3, "CREATED": 4}`

## Pipeline rows
| Source | Type | Status | PII-safe ref | Gate | Next action |
|---|---|---|---|---|---|
| wix_booking_snapshot | booking_review | CANCELED | `1e03ad2efe6a|841171f083a2|e3505b36617c` | operator_review_required | review booking status and decide whether follow-up/contact is needed; do not confirm/change booking automatically |
| wix_booking_snapshot | booking_review | CREATED | `1e03ad2efe6a|841171f083a2` | operator_review_required | review booking status and decide whether follow-up/contact is needed; do not confirm/change booking automatically |
| wix_booking_snapshot | booking_review | CONFIRMED | `1e03ad2efe6a|841171f083a2|e3505b36617c` | operator_review_required | review booking status and decide whether follow-up/contact is needed; do not confirm/change booking automatically |
| wix_booking_snapshot | booking_review | CREATED | `1e03ad2efe6a|841171f083a2|e3505b36617c` | operator_review_required | review booking status and decide whether follow-up/contact is needed; do not confirm/change booking automatically |
| wix_booking_snapshot | booking_review | CREATED | `1e03ad2efe6a|841171f083a2` | operator_review_required | review booking status and decide whether follow-up/contact is needed; do not confirm/change booking automatically |
| wix_booking_snapshot | booking_review | CONFIRMED | `63b063f5b637|011bab91f23a|53403af24191` | operator_review_required | review booking status and decide whether follow-up/contact is needed; do not confirm/change booking automatically |
| wix_booking_snapshot | booking_review | CONFIRMED | `1e03ad2efe6a|841171f083a2|e3505b36617c` | operator_review_required | review booking status and decide whether follow-up/contact is needed; do not confirm/change booking automatically |
| wix_booking_snapshot | booking_review | CREATED | `1e03ad2efe6a|841171f083a2|e3505b36617c` | operator_review_required | review booking status and decide whether follow-up/contact is needed; do not confirm/change booking automatically |
| gmail_program_search | program_research_or_inquiry | needs_review | `message_id_only` | operator_review_if_contacting_external_person | review message body if relevant; create follow-up only after classification |
| gmail_program_search | program_research_or_inquiry | needs_review | `message_id_only` | operator_review_if_contacting_external_person | review message body if relevant; create follow-up only after classification |

## Non-negotiables
- Do not confirm, cancel, contact, or schedule bookings without Commander/operator approval.
- Keep PII hashed/redacted unless raw PII is specifically authorized for a task.
- Convert validated rows into TaskAI follow-ups after review.
