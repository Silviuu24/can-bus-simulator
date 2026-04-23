# CAN Bus Simulator

A virtual CAN Bus simulator implemented in Python, replicating
real automotive ECU communication over a virtual interface.

## Overview
Simulates communication between multiple ECU nodes over a virtual CAN Bus without requiring physical hardware. Demonstrates the CAN 2.0A protocol used in automotive systems.

## Architecture
```text
can-bus-simulator/
├── src/
│   ├── can_message.py   # CAN frame abstraction
│   ├── can_bus.py       # Virtual bus interface (send/receive)
│   ├── ecu_engine.py    # Engine ECU - transmits RPM and temperature
│   ├── ecu_dashboard.py # Dashboard ECU - receives and displays
│   └── config.py        # CAN IDs, DLC and limits
├── main.py              # Entry point, thread orchestration
└── README.md
```
## Installation
```bash
git clone https://github.com/Silviuu24/can-bus-simulator.git
cd can-bus-simulator
pip install python-can
python main.py
```

## How it works
- **ECU Engine** transmits RPM every 10ms and temperature every 100ms
- **ECU Dashboard** continuously listens and decodes incoming frames
- Each ECU runs on a separate thread simulating real-life behavior
- Values are encoded into bytes using bit shifting and offset encoding for negative values (temperature)
  
## Technologies
* **Language:** Python 3.x
* **Libraries:** `python-can` , `threading`

## Status
🚧 Work in progress
