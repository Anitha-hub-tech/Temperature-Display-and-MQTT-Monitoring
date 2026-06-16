# IoT Temperature Monitoring System (Arduino + Python + MQTT + Web Dashboard)

## Overview

This project is an IoT-based temperature monitoring system that collects temperature data from an Arduino sensor, processes it using a Python script, and publishes it to an MQTT broker. The data is then displayed in real time on a web-based dashboard using MQTT over WebSockets.

The system demonstrates a full IoT workflow including embedded systems, serial communication, message brokering, and web-based visualization.

---

## System Architecture

Arduino Sensor
    ↓ (USB Serial Communication)
Python Publisher (pyserial + paho-mqtt)
    ↓ (MQTT Protocol)
MQTT Broker (broker.benax.rw)
    ↓ (WebSockets)
Web Dashboard (HTML + JavaScript)
    ↓
Real-time Temperature Display

---

## Technologies Used

- Arduino Uno (temperature sensor input)
- Python 3.12
  - pyserial
  - paho-mqtt
- MQTT Broker (broker.benax.rw)
- HTML5
- JavaScript
- MQTT.js (WebSocket client)

---

## MQTT Configuration

Broker: broker.benax.rw  
MQTT Port: 1883  
WebSocket Port: 9001  
Topic: anitha/temperature  

---

## Project Structure

IRAKOZE GIKUNDIRO Anitha EXAM Year2c/

├── publisher.py        (Python script: Arduino → MQTT)
├── dashboard.html      (Web dashboard subscriber)
├── Arduino_code.ino    (Arduino program)
└── README.md           (Project documentation)

---

## How to Run the Project

### 1. Upload Arduino Code
- Open Arduino IDE
- Upload the Arduino sketch to the board
- Ensure correct COM port is selected

---

### 2. Install Python Dependencies

pip install pyserial paho-mqtt

---

### 3. Run Python Publisher

cd "C:\Users\user\OneDrive\Pictures\Documents\Arduino\IRAKOZE GIKUNDIRO Anitha EXAM Year2c"

.venv\Scripts\activate

python publisher.py

---

### 4. Open Web Dashboard

Open dashboard.html in a browser  
OR  
Use Live Server in VS Code

---

## MQTT Topic Structure

anitha/temperature

This topic is used to publish all temperature values from Python to the MQTT broker.

---

## Important Notes

- Ensure Arduino Serial Monitor is closed before running Python.
- Verify correct COM port in publisher.py.
- Ensure MQTT broker supports WebSockets for dashboard functionality.
- Check that ports 1883 and 9001 are accessible.

---

## Learning Outcomes

This project demonstrates:

- Embedded systems programming (Arduino)
- Serial communication (UART over USB)
- MQTT communication protocol
- Real-time data streaming
- Web-based IoT dashboards
- End-to-end IoT system integration

---

## Future Improvements

- Add multiple sensors (humidity, gas, etc.)
- Store data in a database (MySQL or Firebase)
- Add real-time graphs using Chart.js
- Deploy system on a VPS server
- Add authentication and secure MQTT (TLS)

---
##connections
LCD
SDA:A4
SCL:A5
DHT
Data:D13
## Author

IRAKOZE  Gikunidiro Anitha 

find my work on http://157.173.101.159:8081/
