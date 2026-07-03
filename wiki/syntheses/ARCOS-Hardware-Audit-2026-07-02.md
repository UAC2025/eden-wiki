---
title: ARCOS Hardware Audit — 2026-07-02
type: synthesis
date: 2026-07-02
tags:
  - arcos
  - s1-personnel
  - hardware
  - printers
confidence: high
---

# ARCOS Hardware Audit — 2026-07-02

> **BLUF:** ARCOS is reachable and authenticated from Hermes when the explicit Hermes key is used. S-1 hardware/printer discovery is now operational. CUPS is active; Epson and Xerox printers are idle/enabled; Godex and Phomemo label/thermal printers are present on USB but disabled as unplugged/offline.

## Verified access

Command path:

```text
ssh -i /persist/eden/hermes/.ssh/github -o IdentitiesOnly=yes urbanarkconsole@AEGIS-ARCOS
```

Verified readback:

```text
ARCOS_OK
AEGIS-ARCOS
Linux AEGIS-ARCOS 6.12.62+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.12.62-1+rpt1~bookworm (2026-01-19) aarch64 GNU/Linux
```

## Identity / OS

| Field | Value |
|---|---|
| Hostname | `AEGIS-ARCOS` |
| User | `urbanarkconsole` |
| Kernel | `6.12.62+rpt-rpi-2712` |
| OS base | Debian Bookworm Raspberry Pi build |
| Architecture | `aarch64` |
| Uptime at audit | 43 days, 6 hours |

## Network

| Interface | Address |
|---|---|
| `eth0` | `10.0.4.33/22` |
| `wlan0` | `10.0.4.26/22` |
| `tailscale0` | `100.91.161.111/32` |

Default route prefers `eth0` via `10.0.4.1`.

## CUPS / printers

CUPS status: **active**.

| Printer | Status |
|---|---|
| `EPSON_ET_5170` | idle / enabled |
| `xerox_c600` | idle / enabled / default destination |
| `Godex_G500` | disabled — unplugged or turned off |
| `Phomemo_PM249` | disabled — unplugged or turned off |

Legacy role mapping remains valid:

```json
{
  "ecommerce": ["Godex_G500", "Phomemo_PM249"],
  "secretarial": ["xerox_c600", "EPSON_ET_5170"]
}
```

## USB devices

Relevant attached devices:

- Logitech BRIO Ultra HD Webcam
- Godex G500 label printer
- PM249-BT thermal printer
- FTDI FT232 serial UART
- USB hubs

Serial path:

```text
/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_BG01PTRG-if00-port0 -> ../../ttyUSB0
```

## EDEN / hardware services running

Key ARCOS services active:

- `advansync-usb.service` — ADVANSYNC USB Bridge / SPLat telemetry
- `eden-arcos-api.service` — ARCOS Hardware API on port 6100
- `eden-forge-device-watcher.service`
- `eden-hal-discovery.service`
- `eden-node-pulse.service`
- `eden-print-queue.service`
- `eden-scan-intake.service`
- `go2rtc.service`
- `mosquitto.service`
- `nodered.service`
- `nginx.service`
- `tailscaled.service`
- `wayvnc.service`

ARCOS local API root returned HTTP 200 and identifies:

```text
node: AEGIS-ARCOS
role: Control Plane — Hardware HAL
ip: 10.0.4.26
cognition: AEGIS-ARK EDEN-CORE
```

## Failed services

| Service | Status |
|---|---|
| `configure-printer@usb-001-032.service` | failed |
| `syncthing@eden-sync.service` | failed |

## Hardware artifacts found

ARCOS contains active AdvanSync / LoRa / SPLat / voice / printer artifacts, including:

- `/home/urbanarkconsole/advansync_bridge.py`
- `/home/urbanarkconsole/advansync_listener.py`
- `/home/urbanarkconsole/advansync_telemetry.json`
- `/home/urbanarkconsole/eden/advansync_usb_bridge.py`
- `/home/urbanarkconsole/eden/arcos/commands/advansync_handler.py`
- `/home/urbanarkconsole/eden/arcos/hal/advansync_controller.py`
- `/home/urbanarkconsole/eden/arcos/routes/tts_api.py`
- `/home/urbanarkconsole/eden/integrations/printer.py`
- `/home/urbanarkconsole/heltec_advansync/heltec_advansync.ino`
- `/home/urbanarkconsole/lora_capture_20260123_193220.txt`

## S-1 closure impact

S-1 hardware discovery is now closed for read-only audit. Remaining hardware deliverables are operational actions, not access blockers:

1. Re-enable or power-check `Godex_G500` and `Phomemo_PM249` if label/thermal output is required.
2. Decide whether to repair `configure-printer@usb-001-032.service`.
3. Decide whether `syncthing@eden-sync.service` matters to S-1 document flow.
4. Next S-1 print test can target `xerox_c600` or `EPSON_ET_5170`; actual printing remains a physical side-effect gate.
