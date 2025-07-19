# Gesture Ink – Hand Gesture Writing & Drawing System

**Gesture Ink** is a real-time, no-touch writing and drawing system powered by **computer vision**, **MQTT**, and **wearable technology**.  
It lets users write or draw mid-air using hand gestures alone — perfect for **digital art**, **assistive tools**, and **smart presentations**.

Developed at **MakeUofT 2025 (Canada’s Largest Makeathon)**, this project was awarded recognition for its innovation in **gesture-based interfaces** and **IoT integration**.

---

## Demo & Live Preview

 **[Watch the Full Demo on YouTube](https://youtu.be/lAq6rWafrmU)**

---

##  Highlights from Gesture Ink

### Gesture-Based Drawing  
> Two fingers up → Draw mode  
![Gesture Drawing](https://github.com/user-attachments/assets/432637c5-4906-4aa1-b9c5-b3850cd591fe)

###  Dynamic Color Switching via Glove Sensors  
>  Real-time RGB control during our MakeUofT demo  
![Color Change](https://github.com/user-attachments/assets/93cde095-60f9-4f15-bd4d-9df8ed427bb9)

![Team Presentation](https://github.com/user-attachments/assets/cd8db60f-47e6-4059-8a00-c65dbf8d277c)

---

##  Core Features

###  Gesture-Based Drawing & Writing  
- ✌️ Two fingers up → Start drawing  
- ☝️ One finger up → Continue drawing  
- 🤟 Three fingers up → Undo  
- ✊ Fist → Stop drawing  

### Dynamic Color Selection (MQTT-Driven)  
- Live RGB changes from glove sensors  
- Color switching without touching the screen  

###  Boundary Detection + Buzzer Alerts  
- Sends out-of-bounds alert via MQTT  
- Glove buzzer provides tactile feedback  

### Real-Time MQTT Communication  
- Subscribes to live glove sensor values  
- Publishes buzzer triggers and actions  

###  Computer Vision + Hand Tracking  
- Uses OpenCV and cvzone for gesture detection  
- Real-time visual feedback and accuracy  

### Undo + Reset Capabilities  
- Gesture-based undo action  
- Clear screen with a reset motion  

---

## Tech Stack & Tools

### Software  
- **Python 3.12+**  
- **OpenCV** for video capture and processing  
- **cvzone + MediaPipe** for hand tracking  
- **NumPy** for image manipulation  
- **paho-mqtt** for communication

### Hardware  
- **Arduino glove sensors** (flex sensors + RGB)  
- **Buzzer module**  
- **ESP32 / ESP8266** for MQTT connectivity  
- **Webcam** for hand tracking  

### Languages & Protocols  
- **Python** → main logic  
- **C++ (Arduino IDE)** → glove firmware  
- **MQTT** → real-time, wireless communication  

---

### Hardware Setup

Connect the **ESP32** and upload the glove firmware via **Arduino IDE**.  
Attach **flex sensors** to detect finger gestures.  
Connect a **buzzer** for out-of-bound alerts.  
Set up an **MQTT broker** (e.g., Mosquitto) and configure IPs in the Python script.

---

###  Future Enhancements

#### AI-Based Handwriting Recognition  
- Translate air-written strokes into editable text  
- Potential use of Google’s handwriting API or ML model

#### Pressure-Based Brush Control  
- Use sensor data to vary stroke thickness  
- Speed-sensitive brush dynamics

#### VR/AR Compatibility  
- Create a virtual whiteboard in 3D  
- Support Leap Motion / Meta Quest tracking

#### Cloud Sync & Multi-Device Support  
- Store notes/drawings via Firebase or Google Drive  
- Access from any device
## Installation Guide

### Install Dependencies  
Make sure you have Python installed, then run:

```bash
pip install opencv-python numpy cvzone paho-mqtt
```

## Final Thoughts

**Gesture Ink** pushes the boundaries of how we interact with technology — no screens, no touch, just natural movement.  
From **assistive tech** to **immersive presentations**, this system showcases how **computer vision** and **IoT** can come together to create intuitive, hands-free interfaces.

Whether you’re an **artist**, **educator**, **developer**, or just curious — we invite you to **explore, expand**, and **enhance** the future of gesture-based interaction.

> Built with passion at **MakeUofT 2025** — and just getting started.
