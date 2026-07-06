---
title: NixOS Ecosystem Commit/Push Plan
status: DRAFT
version: 0.1
owner: Commander (Chad)
maintainer: EDEN
created: 2026-07-06
source_files: []
source_note: "Created from Commander direction in Telegram on 2026-07-06: adopt the skill standard and plan to commit/push the NixOS ecosystem as the new version."
---

# NixOS Ecosystem Commit/Push Plan — 2026-07-06

## BLUF

The current NixOS workspace should be snapshotted as the new ecosystem baseline in controlled commits, not as one blind `git add -A` across everything. The current EDEN vault is the source of truth. Legacy Git material is reference-only unless explicitly promoted.

## Source-of-truth rule

1. Current EDEN vault/workspace on NixOS is the working source.
2. Legacy Git backups are historical reference.
3. Remote Git can be used as a backup/sync/export surface only after review.
4. No secrets, `.bak` drift, quarantined vault output, or accidental UI workspace state should be committed.

## Initial repo inventory observed 2026-07-06

| Repo | Branch | Observed state | Initial action |
|---|---:|---|---|
| `eden-wiki` | `main` | Modified wiki/raw files plus new operations doctrine and S-shop outputs | Review, exclude `.bak`, commit vault doctrine/S-shop evidence in logical commits |
| `eden-living-command` | `master` | Weather/farm-map UI changes and untracked files | Build/test before commit; commit as command-center weather/map baseline |
| `eden-hermes-config` | `master` | `data/reach_ledger.md` changed | Review content; commit only if it is current operational ledger |
| `eden` | `master` | `_MANIFEST/HARDENING_TRACKER.md` changed | Treat as legacy logic mine; commit only if this tracker is part of current migration record |
| `eden-infra` | `master` | Clean | No action until next declared NixOS config change |
| `eden-vault` | `master` | Untracked syntheses in quarantined old vault | Do not commit; quarantine/reference only |

## Commit order

1. **Vault doctrine first** — commit the adopted skill standard and this plan in `eden-wiki`.
2. **Vault operations evidence** — commit S-1/S-2 outputs after checking for stale counts, secrets, and `.bak` drift.
3. **Command center app** — run build/lint if available; commit `eden-living-command` only after successful verification.
4. **Hermes config ledger** — review `data/reach_ledger.md`; commit if it is valid current operational state.
5. **Legacy `eden` tracker** — commit only if the changed tracker represents current NixOS migration/hardening state.
6. **Push/export** — push only after Commander authorizes credential-backed remote write in-session.

## Verification gates before push

For each repo to push:

```bash
git -C <repo> status --short
git -C <repo> diff --stat
git -C <repo> diff --check
git -C <repo> log --oneline -3
```

For `eden-living-command`, also run the app's available validation command (`npm run build`, `npm run lint`, or the repo-defined equivalent) before commit.

## Exclusions

Do not commit:

- `eden-vault/` quarantine changes unless Commander explicitly promotes them.
- `*.bak` files unless a specific backup artifact is intentionally preserved.
- `.env`, secrets, auth files, tokens, local Obsidian workspace state, or generated caches.
- Any animal count/health/breeding claim without live/source citation.

## Operator gate

Remote push uses configured Git authentication. EDEN must not use those credentials unless the Commander authorizes push in the current session.

Ready command after review/gate, per repo:

```bash
git -C <repo> add <reviewed paths>
git -C <repo> commit -m "<scope>: <baseline description>"
git -C <repo> push origin <branch>
```

---
Changelog:
- 2026-07-06 v0.1 DRAFT — initial controlled closeout plan for making the NixOS workspace the new ecosystem baseline.
