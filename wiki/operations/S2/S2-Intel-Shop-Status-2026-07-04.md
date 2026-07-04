---
title: S-2 Intel Shop Status 2026-07-04
type: shop-certification
shop: S2_Intel
status: active-local-certified
rating: operational
---

# S-2 Intel — Shop Status

## Capabilities

| Agent | Status | What |
|---|---|---|
| WeatherAI | LIVE | 3-source fusion (WeatherAPI, OpenWeather, NWS), 15-min updates, threshold alerts via Mycelium |
| MapAI | BUILT | GeoJSON boundary + Leaflet map; Tailscale serving parked pending debug |
| VisionAI | FUTURE | Hardware-gated, camera infrastructure not present |

## Officer Loop

- **S2 Officer**: `s2_alive_loop.py` — hourly, observes WeatherAI + MapAI, deliberates, writes intel brief to wiki, pushes gates to S-1 task store
- **Tests**: `test_s2_alive_loop.py` — 6/6 pass

## S-2 ↔ S-1 Connections

| Connection | Status |
|---|---|
| Weather fusion → SITREP | Active — SITREP pulls from S-2 `weather_fusion_latest.json` |
| Weather thresholds → S-1 tasks | Active — `s2_alive_loop.py` creates S-1 tasks for threshold breaches |
| Weather thresholds → Mycelium | Active — `s2_weather_watch.sh` routes via Mycelium core |
| S-2 source health → SITREP | Active — SITREP shows S-2 source health % |
| S-2 tests → S-1 auditor | Active — auditor runs S-2 test suite |

## Cron Inventory

| # | Job | Interval | Tokens |
|---|---|---|---|
| 5 | S2-Weather-Fusion | 15m | 0 |
| 6 | S2-Weather-Threshold-Watch | 15m | 0 |
| 7 | S2-Alive-Loop | 60m | 0 |

## Gaps

| Gap | Status |
|---|---|
| MapAI Tailscale serving | Parked — needs debug |
| S-2 live audit events | Not wired — S-2 doesn't emit to `s1_live_event_audit` |
| S-2 certification harness | Not built — no parent-agent cert like S-1 has |
| VisionAI | Hardware-gated |
| Breed registry monitoring | Not implemented — would pull Arapawa breeder group data |

## Rating

**Operational.** Weather intelligence is production-grade. MapAI data exists but display is blocked by Tailscale routing. Officer loop produces hourly briefs. S-1 connections are live.