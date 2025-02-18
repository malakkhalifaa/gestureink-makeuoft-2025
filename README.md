# ✨ Gesture Ink - Hand Gesture Writing & Drawing System  

Gesture Ink is a **real-time hand gesture-controlled writing system** using **OpenCV, cvzone, and MQTT integration**. It allows users to **write and draw using only hand movements**, with **dynamic color selection** and **buzzer alerts** for out-of-bounds gestures.  

This project integrates with **wearable technology** (glove sensors + MQTT communication) for **gesture-based control**, making it a **powerful assistive tool** for digital art, presentations, and interactive applications.  

---

## 📸 Demo & Screenshots  

### 🖼️ Demo Video URL
https://youtu.be/lAq6rWafrmU

### 🎨 **Hand Gesture Writing in Action**  
> *Index & Middle Fingers Up - Start Drawing*  
Gesture Drawing![Screenshot (264)](https://github.com/user-attachments/assets/432637c5-4906-4aa1-b9c5-b3850cd591fe)



### 🎨 **Changing Colors via MQTT**  
> *RGB values dynamically update from glove-based sensor inputs.*  
![Color Change]![PHOTO-2025-02-17-08-41-46](https://github.com/user-attachments/assets/93cde095-60f9-4f15-bd4d-9df8ed427bb9) 


---

## 🚀 Features  

### **1️⃣ ✏️ Gesture-Based Drawing/Writing**  
- ✌️ **Index & Middle Finger Up** → Start drawing  
- ☝️ **Index Finger Up** → Continue drawing  
- 🤟 **Three Fingers Up** → Undo last annotation  

### **2️⃣ 🌈 Dynamic Pen Color Selection via MQTT**  
- RGB colors update **in real-time** based on MQTT messages.  
- LED-based **glove control** allows users to **change color modes dynamically**.  

### **3️⃣ 🎯 Boundary Notification System**  
- **Buzzer Alert 🔊** when the hand moves **out of the drawing area**.  
- Prevents accidental strokes outside the intended gesture region.  

### **4️⃣ 📡 MQTT Integration for Smart Interactions**  
- **Receives RGB values** from a glove-based external system.  
- **Publishes buzzer alerts** when the user moves outside a defined gesture region.  
- **Subscribes to multiple MQTT topics** to receive real-time updates from an external glove system.  

### **5️⃣ 📷 Webcam & Live Preview**  
- **Hand gesture detection** using **OpenCV & cvzone**.  
- **Small live preview window** of the user's webcam for real-time feedback.  

---

## 📃 Requirements  

### **🖥️ Software Requirements**
- **Python 3.12**  
- **OpenCV (cv2)** → `pip install opencv-python`  
- **NumPy (numpy)** → `pip install numpy`  
- **cvzone (cvzone)** → `pip install cvzone`  
- **paho-mqtt (paho-mqtt)** → `pip install paho-mqtt`  
- **Arduino IDE** → For hardware integration with the glove system  

### **🔌 Hardware Requirements**
- **Webcam** (built-in or external) for hand tracking  
- **Arduino-compatible glove sensors** for color switching  
- **Buzzer module** for boundary notifications  
- **Wi-Fi enabled microcontroller** (ESP32/ESP8266) for MQTT messaging  

---


