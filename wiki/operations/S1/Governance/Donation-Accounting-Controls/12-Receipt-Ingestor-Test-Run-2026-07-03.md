---
title: S-1 Receipt Ingestor Test Run 2026-07-03
type: test-report
created: 2026-07-03
component: s1_receipt_attachment_ingestor
status: pass
---

# S-1 Receipt Ingestor Test Run — 2026-07-03

## BLUF
S-1 added and ran a regression/smoke test harness for the Gmail receipt attachment ingestor. The harness now prevents smoke tests from overwriting production receipt registers.

## Commands verified

```bash
.venv/bin/python -m py_compile s1_operational/ingest_gmail_receipt_attachments.py s1_operational/test_receipt_ingestor.py
.venv/bin/python s1_operational/test_receipt_ingestor.py -v
.venv/bin/python s1_operational/ingest_gmail_receipt_attachments.py --max 1 --run-id smoke-20260703
```

## Results

| Check | Result |
|---|---|
| Python syntax compile | PASS |
| Unit/regression tests | PASS — 5 tests |
| Smoke run with `--run-id smoke-20260703` | PASS — wrote under `Test-Runs/smoke-20260703/` |
| Production register preserved after smoke test | PASS |

## Tests added

- `test_build_output_paths_uses_run_id_without_touching_production_register`
- `test_production_paths_require_explicit_production_run_id`
- `test_classifies_tnr_from_subject`
- `test_classifies_uac_from_urban_ark_text`
- `test_unknown_when_no_entity_signal`

## Outcome

The previous risk — a smoke test overwriting the full production receipt register — is now covered by regression tests and a run-id output path guard.

## Next S-1 run

Produce source-backed receipt totals from the extracted attachment CSV, but only after resolving `unknown_review_required` rows and choosing the correct total from multi-amount statements.
