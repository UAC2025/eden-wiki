---
title: Node Audit — EDEN Hardware Control Plane
type: synthesis
date: 2026-07-06
status: DRAFT
source_files:
  - tailscale status (live, 2026-07-06 14:48 EDT)
  - ARCOS API :6100 health endpoint
  - LLM Ollama :11434 /api/tags
  - DESK Mission Command :8791
  - workspace/eden/arcos/arcos_api.py (source code)
---

# EDEN Node Audit — 2026-07-06

## Reachable Nodes

| Node | Role | IP | Tailscale | OS | Status |
|---|---|---|---|---|---|
| **nixos** (AEGIS-ARK) | Primary cognition | 10.0.4.43 | 100.87.231.95 | NixOS gen-26 | Active (this box) |
| **aegis-arcos** | Hardware HAL / Voice | 10.0.4.33 | 100.91.161.111 | Linux (Debian) | Online |
| **aegis-llm** | Local LLM inference | 10.0.4.32 | 100.125.103.105 | Linux (Pi 5) | Online |
| **the-heartbeat** (AEGIS-DESK) | Operator workstation | 10.0.4.31 | 100.84.77.54 | Windows 11 | Online |
| **cm-vault** | Commander Android | 10.0.4.51 | 100.81.59.7 | Android | Active |

## Offline / Legacy

| Node | Last Seen | Notes |
|---|---|---|
| aegis-vision | 82 days ago | Hailo-10H vision processor — may be decommissioned |
| ark-aegis | 8 days ago | Old ARK hostname — replaced by nixos rebuild |
| chadmcc | 80 days ago | Old Commander phone |
| advansync-pi | Never on Tailscale | Not deployed or not registered |

---

## Node Capabilities

### AEGIS-ARCOS (Control Plane — Hardware HAL)

**Reachable:**
- ARCOS API :6100 — `{"status":"OPERATIONAL","role":"Control Plane — Hardware HAL","routes":14,"version":"3.0-cognition-migrated"}`
- `/health` — systems: finance OK, kb_router OK, root_system OK, weather OK
- `/tts` — POST-only (voice synthesis)
- `/upload` — POST-only

**Not reachable:**
- SSH (port 22) — banner exchange timeout. Service may be hung. Needs operator investigation.
- Other 12 routes return 404 when probed via GET — likely POST-only or require ARCOS-local filesystem context

**Hardware HAL role per source code:** forge (AI image gen) + tts (voice). Printers/scanners are managed via CUPS/SANE on the ARCOS node itself — requires SSH access to enumerate.

### AEGIS-LLM (Local Inference)

**Reachable:**
- Ollama :11434 — `Ollama is running`
- 6 models loaded:

| Model | Size | Quant |
|---|---|---|
| qwen3:8b | 8.2B | Q4_K_M |
| qwen2.5:7b | 7.6B | Q4_K_M |
| qwen3:4b | 4.0B | Q4_K_M |
| gemma3:4b | 4.3B | Q4_K_M |
| qwen2.5:3b | 3.1B | Q4_K_M |
| nomic-embed-text | 137M | F16 |

**Not reachable:**
- SSH — key not installed. Commander action required (see Operator Actions below).

### AEGIS-DESK (Operator Workstation)

**Reachable:**
- Mission Command :8791 — HTTP 200 (Next.js frontend online)

**Not tested:**
- Pixel Farm :8790 — timed out during probe
- Port :3000 — not probed
- SSH — key not installed on Windows

---

## ARCOS API Control Surface

From source code (`eden/arcos/arcos_api.py`, `EDEN_DEPLOY=arcos`):

| Blueprint | URL | Method | Status |
|---|---|---|---|
| health | `/health` | GET | ✅ Confirmed live |
| root | `/` | GET | ✅ Confirmed live |
| tts | `/tts` | POST | ✅ 405 (POST-only confirmed) |
| upload | `/upload` | POST | ✅ 405 (POST-only confirmed) |
| alerts | `/alerts` | ? | ⚠️ 404 on GET |
| trust | `/trust` | ? | ⚠️ 404 on GET |
| weather | `/weather` | ? | ⚠️ 404 on GET |
| finance | `/api/finance` | ? | ⚠️ 404 on GET |
| grants | `/api/grants` | ? | ⚠️ 404 on GET |
| development | `/api/development` | ? | ⚠️ 404 on GET |
| ai_swarm | `/ai_swarm` | ? | ⚠️ 404 on GET |
| memory | `/memory` | ? | ⚠️ 404 on GET |
| forge | `/forge` | ? | ⚠️ 404 on GET |

**Note:** 14 routes declared, 4 confirmed live (/, /health, /tts, /upload). Remaining 10 routes may require specific HTTP methods, authentication, or POST bodies. Full route enumeration requires SSH access to ARCOS to read `~/eden/arcos/routes/*.py`.

---

## Tiered Control Registry

### Tier 0 — Read / Discovery (auto, no gate)

| Capability | Node | Channel | Verified |
|---|---|---|---|
| Node health check | ARCOS | `GET :6100/health` | ✅ |
| Node identity | ARCOS | `GET :6100/` | ✅ |
| LLM model list | LLM | `GET :11434/api/tags` | ✅ |
| LLM health | LLM | `GET :11434/` | ✅ |
| DESK dashboard status | DESK | `GET :8791/` | ✅ |
| Tailscale node list | ARK | `tailscale status` | ✅ |

### Tier 1 — Physical Side-Effect (auto, logged)

| Capability | Node | Channel | Verified |
|---|---|---|---|
| TTS voice synthesis | ARCOS | `POST :6100/tts` | ⚠️ Endpoint exists, not tested |
| File upload | ARCOS | `POST :6100/upload` | ⚠️ Endpoint exists, not tested |
| LLM inference | LLM | `POST :11434/api/generate` | ⚠️ Available, not tested |

### Tier 2 — Destructive / Admin (operator gate)

| Capability | Node | Channel | Verified |
|---|---|---|---|
| SSH to ARCOS | ARCOS | `ssh info@aegis-arcos` | 🔴 Blocked (banner timeout) |
| SSH to LLM | LLM | `ssh president@aegis-llm` | 🔴 Blocked (no key) |
| SSH to DESK | DESK | `ssh info@the-heartbeat` | 🔴 Blocked (no key) |

---

## Operator Actions Required

### 1. ARCOS SSH recovery
SSH banner exchange timeout suggests hung SSHd. Requires physical access or console:
```bash
# From ARCOS console or existing session:
sudo systemctl restart sshd
```

### 2. Install SSH key on LLM and DESK
```bash
# From an existing login session on each node:
ssh president@aegis-llm "mkdir -p ~/.ssh && chmod 700 ~/.ssh && echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBOSugXK7oeBTMR+U3L66uJ0EBfVdQQoQTpWTs/RR3X/ hermes@nixos' >> ~/.ssh/authorized_keys && sort -u -o ~/.ssh/authorized_keys ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

### 3. ARCOS route enumeration
Once SSH is restored, read `~/eden/arcos/routes/*.py` on ARCOS to document full API surface including printers (CUPS) and scanners (SANE). Printer list from prompt: EPSON_ET_5170, xerox_c600, Godex_G500, Phomemo_PM249.

### 4. advansync-pi
Not found on Tailscale. If deployed, needs network registration.

---
Generated: 2026-07-06 14:50 EDT — live probes against all reachable nodes.