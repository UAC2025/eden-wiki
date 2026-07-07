---
title: Node Architecture — EDEN Hardware Layer
type: doctrine
status: CANONICAL
date: 2026-07-06
source_files: []
---

# EDEN Node Architecture

Four nodes, one surface. Each has a single canonical role. No node does
another node's job.

## Node Map

| Node | IP | Hardware | Role | Control Channel |
|---|---|---|---|---|
| **AEGIS-ARK** | 10.0.4.43 | i7-4790K, NixOS | Cognition — EDEN O-6, all officers, all reasoning | Local |
| **AEGIS-ARCOS** | 10.0.4.26 | Pi 5, Debian | Hardware HAL — all physical devices register here | SSH + :6100 API |
| **AEGIS-LLM** | 10.0.4.32 | Pi 5 + Hailo-10H (40 TOPS) | Vision — camera monitoring, object detection, local inference fallback | HTTP :11434 |
| **AEGIS-DESK** | 10.0.4.31 | i7 9th gen, Win 11, 4 monitors | Operator surface — DESKAI runtime, app control, visual output | HTTP :8791 (Mission Cmd) |
| **Advansync Pi** | TBD | Pi + Heltec LoRa | LoRa gateway — SPLat mesh, field sensors, actuators | Needs reflash |

## What lives where

### AEGIS-ARK (cognition)
- EDEN O-6 + all 6 staff officers
- All 28 parent agents (on-demand)
- Hermes Agent gateway (Telegram, all messaging)
- Vault (eden-wiki)
- All cron jobs
- Reach engine (social media)
- Mycelium adapters (Gmail, Wix, Calendar, Farmbrite)
- Ledgers, doctrine, skills

### AEGIS-ARCOS (hardware HAL)
- **Printers:** EPSON ET-5170, Xerox C600 (default), Godex G500 (label), Phomemo PM249 (thermal)
- **Scanners:** SANE + BRIO camera via go2rtc
- **Voice:** TTS endpoint (:6100/tts)
- **Registration:** All physical devices register here first
- **Control:** EDEN controls hardware through ARCOS API; SSH is admin/fallback
- **Status:** SSH hung — needs physical restart

### AEGIS-LLM (vision + inference)
- **Vision:** Camera monitoring, object detection (Hailo-10H, 40 TOPS)
- **Models:** YOLOv8m, pose estimation, RTSP proxy
- **Inference fallback:** 6 Ollama models (qwen3:8b strongest)
- **Cameras:** Garage interior (NVR ch6), Garage exterior (NVR ch7)
- **Formerly:** aegis-vision (offline 82 days) — role absorbed into LLM node

### AEGIS-DESK (operator surface)
- **DESKAI:** EDEN-tier agent controlling the operator workstation
- **Mission Command:** Dashboard on :8791
- **Apps:** Blender (design), Office suite, browser, slicer, Adobe/Affinity
- **4 monitors:** Mission Control TV, Pixel Farm, Workbench, Mobile
- **Operator sees EDEN work through this surface**

### Advansync Pi (LoRa gateway)
- **Radio:** Heltec LoRa module → SPLat mesh controller
- **Reach:** Field sensors, greenhouse, pasture monitors
- **Status:** Needs reflash — not yet on Tailscale
- **After reflash:** Registers on ARCOS as sensor node; data flows ARK → LLM for vision

## Data Flow

```
Field sensors → Advansync Pi (LoRa) → ARK (Mycelium) → Officers (reasoning)
                                                    → LLM (vision processing)
Cameras → LLM (Hailo detection) → ARK (S2 Intel alerts)
ARCOS ← ARK (print/scan/voice commands) → physical output
DESK ← ARK (DESKAI app control) → operator visual surface
```

## Current Reachability

| Node | Tailscale | HTTP | SSH | Status |
|---|---|---|---|---|
| ARK | Local | — | — | Live |
| ARCOS | ✅ | :6100 intermittent | 🔴 Hung | Needs restart |
| LLM | ✅ | :11434 Ollama | 🔴 No key | API reachable |
| DESK | ✅ | :8791 up | 🔴 No key | Dashboard live |
| Advansync | ❌ | — | — | Needs reflash |

---
Changelog:
- 2026-07-06 — CANONICAL, Commander-defined node architecture