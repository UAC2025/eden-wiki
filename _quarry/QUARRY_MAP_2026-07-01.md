---
title: Quarry Map — /mnt/kb Recon 2026-07-01
type: quarry-recon
status: awaiting-adjudication
surveyed_by: EDEN
surveyed_on: 2026-07-01
source_mount: /mnt/kb (ext4, label EDEN_KNOWLEDGE, /dev/sdb2, mounted read-only)
disk: 1.8T total, ~85G used
note: >
  /mnt/kb is a read-only quarry, not a memory surface. Nothing listed here enters
  raw/ without the Commander's adjudication. This map is survey output only —
  it contains no observational farm claims of its own; every characterization
  below is a description of what a source file/DB contains, pending verification
  at adjudication time.
---

# Quarry Map — /mnt/kb Recon 2026-07-01

Read-only reconnaissance of the EDEN_KNOWLEDGE external disk. Inventory method:
`find`/`du` sweep plus light sampling (file heads, sqlite read-only probes with
`immutable=1`). No file on /mnt/kb was modified; nothing was copied into raw/ or wiki/.

## Top-Level Size Map

| Path | Size | Character |
|---|---|---|
| `_SAFE_BACKUP_20260626/` | 35G | Full system backup: eden-core, entire old home dir (incl. old vault), .hermes spine |
| `backups/` | 22G | Daily DB backups 2026-06-14 → 2026-06-20 + March 30 point-in-time set |
| `eden-data/` | 15G | vision_events (~1.52M detection JSONs), yolo26_pipeline, crosslink-archive, archived-home-files |
| `EDEN_SAFE_BACKUP_20260626.tar.gz` | 8.6G | Compressed duplicate of `_SAFE_BACKUP_20260626/` |
| `memory/` | 2.9G | claude-mem episodic store (chroma.sqlite3 1.4G + claude-mem.db 830M) |
| `eden-live-snapshots/2026-06-26/` | 2.5G | Freshest DB/chroma/hermes/git snapshot |
| `vectors/` + `vectors_corrupted_backup/` + `vectors_old_20260122/` | ~1.1G | Chroma vector stores (one marked corrupted) |
| `knowledge_archive_20260121/` | 55M | Jan 21 taxonomy archive (~2,850 md, 30+ topic dirs) |
| `archives/` | 41M | `duplicates_20260120/`, `scaffolds_20260120/` dedup piles |
| `knowledge/` | 720K | `UAC_BRAND_BIBLE.md` + `generated/` AI-reference docs |
| `documents/` | 132K | `breed-standards/` (curated, June 7) |
| `_MANIFEST/`, READMEs | <150K | Boot manifests, memory-layer inventory, Hermes first-paste doc |

File-type distribution (whole disk): 1.54M json (almost all vision detections),
67.6k py, 63k txt, 55k jpg, 44.2k md, 35.8k jsonl. The code/JSON bulk is machine
output, not knowledge.

## The 8 Mining Clusters (priority order)

### 1. Commander's GOLD list — `EDEN_FRESH_HERMES_FIRST_PASTE.md`
- **Path:** `/mnt/kb/EDEN_FRESH_HERMES_FIRST_PASTE.md` (10.4K, root-owned, written 2026-06-26)
- **What it is:** Commander-authored bootstrap doctrine for a fresh Hermes install. Contains the GOLD-vs-slop allowlist, backup locations (both physical copies), MCP wiring, Mission Command dashboard runbook, identity/doctrine section, and first-loop target.
- **Mining value: HIGHEST.** It is a pre-made adjudication guide for the entire migration — the Commander's own judgment of what carries forward, written 5 days before this recon. Candidate for raw/decisions/ or raw/operator-notes/ nearly verbatim.
- **⚠️ Security flag:** contains a live `EDEN_BRIDGE_TOKEN` in plaintext (line ~101). `backups/*/secrets/` and `eden-live-snapshots/2026-06-26/secrets/` directories also exist on the disk. Recommend rotating the token and deciding secret handling before anything derived from these files circulates.

### 2. Freshest herd database — live snapshot sqlite
- **Path:** `/mnt/kb/eden-live-snapshots/2026-06-26/sqlite/data_eden_farm.db` (108M)
- **Access note:** plain read-only open fails on this mount; open with `sqlite3 'file:...?mode=ro&immutable=1'`.
- **Contents (probed):** 22 animals (Farmbrite-synced schema: farmbrite_id, registry_number, FAMACHA, breeding/bred status, death_date, etc. — e.g. Arapawa doe "CP Storm", registry L11/CP, conservation critical), 6 registries, 19 paddocks, 20 donors, 19 donations, 11 grants, 13 therapy participants, 11 programs, 287 climate_logs, 30 predictions. Also 171,383-row `decision_ledger` and 71,234-row `_changelog` — machine noise, not herd data.
- **Mining value: HIGHEST for observational data.** Natural ancestor of `farm.sqlite`. This single file could seed animal entities, donor/grant records, and paddock structure — all with DB-level provenance.
- Sibling copies (staleness ladder): `backups/2026-06-{14..20}/sqlite/data_eden_farm.db` (108M each) plus `data_conservation_pedigree.db`, `data_nonprofit_nonprofit.db`, `data_finance_finance.db` etc. in the same dirs — same-schema variants worth one adjudication pass each.

### 3. The old vault — obsidian-vault-sync
- **Path:** `/mnt/kb/_SAFE_BACKUP_20260626/home_urbanarkconsole/eden/obsidian-vault-sync/` (git repo UAC2025/eden-vault; 18,536 md)
- **Human-authored farm records concentrated in:** `Animals/` (70 md — per-species dirs, Arapawa-Comprehensive-Guide, species indexes), `Grants/` (65), `Infrastructure/` (60), `Equipment/` (8), `SOPs/` (5), `Health/` (6), `Sessions/` (9), `Map/`, `Decisions/` human subset.
- **Contamination to avoid:** `Decisions/` is 11,392 files — overwhelmingly machine ledger entries; `wiki/` is 6,319 derived pages (old synthesis layer — foreign agent output, left behind per constitution); `_EDEN/` (570) is agent scaffolding; Syncthing `*.sync-conflict-*` duplicates are scattered throughout every dir sampled.
- **Mining value: HIGH but per-file.** This is exactly the "old vault (~18k notes plus OpenClaw contamination)" the constitution names. Mine the small human dirs (Animals, Grants, Infrastructure, Equipment, SOPs, Health) one file at a time; skip wiki/, _EDEN/, and the machine bulk of Decisions/.

### 4. Curated breed standards
- **Path:** `/mnt/kb/documents/breed-standards/` — `2026-06-07-breed-standards-full-archive.md` (32K), `2026-06-07-obsolete.md` (32K), `pending/` subdir.
- **Mining value: HIGH, partially done.** The Arapawa standard from this set is already in raw/ (git log 2026-06-30). The full archive, the `pending/` contents, and the explicit obsolete marker are natural next adjudications.

### 5. March point-in-time databases
- **Path:** `/mnt/kb/backups/databases_20260330/` (182M, 23 files)
- **Contents (probed):** all differently-named .db files there (`pedigree.db`, `therapy.db`, `nonprofit.db`, `agriculture.db`, …) are byte-identical copies of the same eden_farm database: 22 animals, 199 climate_logs, 19 paddocks, 6 registries. Five timestamped `eden_farm_2026032*.db` snapshots span Mar 28–30.
- **Mining value: MEDIUM.** Redundant with cluster 2 for current state, but useful for temporal diffing (what changed in the herd between March 30 and June 26) if adjudication wants change-history.

### 6. January knowledge taxonomy archive
- **Path:** `/mnt/kb/knowledge_archive_20260121/` (55M, ~2,850 md across 30+ dirs: ANIMALS, AGRICULTURE, SOP/{daily,weekly,monthly,seasonal,emergency,maintenance,procedures}, OPERATIONS, GOVERNANCE, FINANCE, COMPLIANCE, CONSERVATION, …)
- **Provenance is MIXED:** sampled `ANIMALS/goats/belle_kidding_prep.md` is an operational checklist (Belle, due date Jan 28 2026); but the sibling `knowledge/generated/` corpus carries an explicit "AI-generated reference document — verify with expert" banner, and this archive shares lineage.
- **Mining value: MEDIUM, adjudicate per-file.** The SOP tree and animal-specific operational notes are candidates; anything reference-flavored should be presumed AI-generated unless it names dates/animals/observations traceable to the operator.

### 7. eden-core data and doctrine
- **Path:** `/mnt/kb/_SAFE_BACKUP_20260626/eden-core/` (1,892 md; also `app/data/` which the Commander's GOLD list names for "herd / org / grant / financial data")
- **Also contains:** `_QUARANTINED_2026-06-10_openclaw-units/`, `_QUARANTINED_2026-04-20/`, `_QUARANTINED_2026-04-29_parent_doctrine/` (already-adjudicated contamination — useful as a what-not-to-carry reference), audits/, docs/, `secrets/` (flag as with cluster 1).
- **Mining value: MEDIUM.** Value is in `app/data/` payloads and decision/audit records, not code. The quarantine dirs document prior contamination boundaries.

### 8. Brand and generated reference corpus
- **Path:** `/mnt/kb/knowledge/` — `UAC_BRAND_BIBLE.md` (already ingested, git log 2026-06-30) + `generated/` (~30 md: arapawa health protocols, kidding emergency protocols, FAMACHA-adjacent scoring refs, Bradford County growing guide, grant-writing guides).
- **Mining value: LOW-MEDIUM, with a hard caveat.** Every `generated/` file is self-declared AI output. Under the Cardinal Rule these can never source an observational claim; at most they could enter raw/ as clearly-labeled AI reference material if the Commander wants the concepts available. Default recommendation: leave behind, cite real veterinary/breed-association sources instead.

## Leave-Behind List (with rationale)

| Path | Size | Rationale |
|---|---|---|
| `memory/claude-mem/` | 2.9G | Foreign agent episodic memory (chroma + db). Constitution: foreign agent output is left behind, not carried forward. |
| `vectors/`, `vectors_corrupted_backup/`, `vectors_old_20260122/` | ~1.1G | Derived embeddings of contaminated corpus; regenerable; one copy explicitly corrupted. |
| `*/hermes/hermes_state.db` (8 copies) + `_SAFE_BACKUP_20260626/.hermes/state.db` | ~5G | Agent runtime state, not farm knowledge. |
| `eden-data/vision_events/` | 6.0G | ~1.52M machine detection JSONs. Machine telemetry, not adjudicable knowledge. Could someday back a synthesis if camera-event evidence is wanted — park, don't mine. |
| `eden-data/yolo26_pipeline/` | 3.8G | CV training pipeline artifacts; regenerable tooling. |
| `eden-data/crosslink-archive/`, `eden-data/archived-home-files/` | 4.4G | Bulk home-dir archaeology; anything of value is better reached via clusters 2–3. |
| `EDEN_SAFE_BACKUP_20260626.tar.gz` | 8.6G | Byte-duplicate of `_SAFE_BACKUP_20260626/`; keep as backup, never mine. |
| `backups/2026-06-{14..19}/` (older dailies) | ~15G | Superseded by 06-20 daily and 06-26 live snapshot; retain as backups only. |
| `archives/duplicates_20260120/`, `archives/scaffolds_20260120/` | 41M | Already-identified duplicates and empty scaffolds from the January cleanup. |
| Old vault `wiki/` (6,319 md) and `_EDEN/` (570 md) | — | Old derived/synthesis layer = foreign agent output; the new wiki/ is rebuilt from raw/, not from an old wiki. |
| Old vault `Decisions/` machine bulk (~11.4k md) | — | Machine decision-ledger spam; human decision notes should be fished out individually during cluster-3 adjudication, not bulk-carried. |
| `knowledge/generated/` AI-reference docs | <1M | Self-declared AI-generated; can never source observational claims (Cardinal Rule). |
| `models/`, `ml_training_data/`, `cache/`, `knowledge_clean/`, `lost+found/` | ~40K | Empty or near-empty scaffolding. |

## Suggested Adjudication Order

1. Cluster 1 (GOLD list doc) — it accelerates every later decision. Handle the embedded token first.
2. Cluster 2 (June 26 farm DB) — seeds farm.sqlite / animal entities with DB provenance.
3. Cluster 4 (breed standards `pending/`) — small, curated, half-done already.
4. Cluster 3 (old vault human dirs) — one file at a time: Animals → Grants → Infrastructure → Equipment → SOPs → Health.
5. Clusters 5–7 as needed; cluster 8 default-decline.
