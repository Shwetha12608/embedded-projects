# IoT Monitoring & Control System (ESP32 + MQTT)

## Overview
This project implements a real-time IoT monitoring and control system using ESP32. Sensor data (temperature and light) is transmitted using MQTT protocol and monitored via a Python client. The system also supports remote device control (LED ON/OFF).

## Features
- Real-time sensor data monitoring
- MQTT-based publish–subscribe communication
- Bi-directional control (Python → ESP32)
- JSON-based data formatting
- WiFi-enabled communication

## Tech Stack
- ESP32 (Embedded C)
- Python (MQTT Client)
- MQTT (broker.hivemq.com)
- JSON

## Architecture
ESP32 → MQTT Broker → Python Client  
Python Client → MQTT Broker → ESP32 (Control)

## How to Run
1. Run Python MQTT client
2. Start ESP32 simulation in Wokwi
3. Send ON/OFF commands from Python terminal

## Results
- Latency: ~1–2 seconds
- Stable communication with 5–15 sec updates
