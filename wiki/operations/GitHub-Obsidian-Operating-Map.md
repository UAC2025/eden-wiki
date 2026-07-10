---
date: 2026-07-10
type: operating-map
status: approved
owner: Commander
scope: GitHub and Obsidian
---

# GitHub–Obsidian Operating Map

## Decision

**`eden-wiki` is the canonical operational Obsidian vault.** Its Git remote, `UAC2025/eden-wiki`, is the versioned off-box record for the notes deliberately committed from this vault.

`eden-vault` is a **read-only legacy archive**. It is not a second active knowledge system and no material moves from it into the canonical vault without Commander adjudication.

## System boundaries

| System | Purpose | What belongs there | What does not |
|---|---|---|---|
| Obsidian / `eden-wiki` | Human-readable operating record | Briefings, decisions, SOPs, source-backed wiki pages, architecture maps | Credentials, raw Nix config, duplicate application code |
| GitHub | Versioned, off-box source control | The committed `eden-wiki` vault, application source, NixOS configuration, encrypted agenix files | Plaintext secrets, unreviewed scratch work |
| Honcho | Agent-to-agent operational recall | Short conclusions, decisions, lessons, closure evidence | Canonical documents or source archives |
| Command dashboard | Present-tense operating view | Live status, metrics, actionable items | Source-of-truth records |

## Repository roles

| Repository | Role | Operating rule |
|---|---|---|
| `UAC2025/eden-wiki` | Canonical Obsidian operations vault | Commit deliberate, reviewed note changes; push after verification. |
| `UAC2025/nixos-config` | ARK host configuration | Nix-only; commit reviewable configuration changes and encrypted agenix files. |
| `UAC2025/eden-living-command` | Dashboard code | Code and tests only; dashboard is not approved until visual QA passes. |
| `UAC2025/uac-brand-assets` | Brand assets | Approved source assets only. |
| `UAC2025/eden-vault` | Legacy archive | Read-only; no automatic ingestion or synchronization. |

## First working loop

1. A Commander-approved operating decision is recorded once in `eden-wiki`.
2. The note is reviewed for accuracy and no secrets.
3. Only that note is staged, committed, and pushed to `UAC2025/eden-wiki`.
4. GitHub is checked to confirm the commit reached the remote.
5. The note—not a duplicate—becomes the human reference for the decision.

## Current audit boundary — 2026-07-10

- The configured vault path is `/persist/eden/hermes/workspace/eden-wiki`.
- `eden-wiki` has pre-existing uncommitted July briefings and raw imports. They are intentionally **not included** in this first proof commit.
- `eden-vault` has pre-existing uncommitted legacy syntheses. They are intentionally untouched.
- `/etc/nixos` has separate mixed configuration work. It requires its own clean review and GitHub push; it is not part of the wiki loop.

## Guardrails

- Never use Obsidian as a blind backup of every repository.
- Never commit or push a plaintext credential.
- Never sweep unrelated uncommitted files into a “sync” commit.
- Do not automate broad synchronization until this one-note commit → push → remote-verification loop is proven.
