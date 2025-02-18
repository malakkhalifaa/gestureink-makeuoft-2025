# ✨ Gesture Ink - Hand Gesture Writing & Drawing System  

Gesture Ink is a **real-time hand gesture-controlled writing system** powered by **computer vision, MQTT communication, and wearable technology**. It allows users to **write and draw using only hand movements**, with **dynamic color selection** and **buzzer alerts** for out-of-bounds gestures.  

This project integrates **gesture-based control** with **wearable sensors**, making it an innovative tool for **digital art, interactive presentations, assistive technology, and smart interfaces**.  

---

## 📸 Demo & Screenshots  

### 🎥 **[Check out the Demo](https://youtu.be/lAq6rWafrmU)**  

### 🖼️ **Hand Gesture Writing in Action**  
> **✌️ Index & Middle Fingers Up** → Start drawing  
![Gesture Drawing](https://github.com/user-attachments/assets/432637c5-4906-4aa1-b9c5-b3850cd591fe)

### 🎨 **Group Photo**  
> **🧤 During the presentation we showed the glove gensors dynamically adjusting RGB values**  
![Color Change](https://github.com/user-attachments/assets/93cde095-60f9-4f15-bd4d-9df8ed427bb9)  

---

## 🚀 Key Features  

### **1️⃣ ✏️ Gesture-Based Drawing & Writing**  
- **✌️ Index & Middle Finger Up** → Start drawing  
- **☝️ Index Finger Up** → Continue drawing  
- **🤟 Three Fingers Up** → Undo last annotation  
- **🛑 Closed Fist** → Stop drawing  

### **2️⃣ 🌈 Dynamic Pen Color Selection via MQTT**  
- **RGB values update dynamically** based on **glove-based sensor inputs**.  
- **LED-based glove controls** allow users to switch colors **without touching a screen**.  

### **3️⃣ 🎯 Boundary Notification System**  
- **Buzzer Alert 🔊** when the hand moves **out of the drawing area**.  
- **Real-time feedback** prevents accidental strokes outside the gesture region.  

### **4️⃣ 📡 MQTT Integration for Smart Interactions**  
- **Receives real-time RGB values** from an external **glove-based sensor system**.  
- **Publishes buzzer alerts** when the user moves outside a defined drawing region.  
- **Subscribes to multiple MQTT topics** to enable seamless data exchange.  

### **5️⃣ 📷 Real-Time Webcam Hand Tracking**  
- **Hand gesture recognition** using **OpenCV & cvzone**.  
- **Live preview window** for real-time interaction feedback.  

### **6️⃣ 🔄 Undo & Clear Options**  
- **Undo previous strokes** with **hand gestures**.  
- **Clear the screen** with a **custom reset action**.  

---

## 🛠️ Technologies Used  

### **1️⃣ Computer Vision & Gesture Recognition**  
- **[OpenCV](https://opencv.org/)** → Real-time hand tracking & gesture detection  
- **[cvzone](https://github.com/cvzone/cvzone)** → Simplified hand detection using MediaPipe  
- **[NumPy](https://numpy.org/)** → Image processing and mathematical operations  

### **2️⃣ IoT & MQTT-Based Communication**  
- **[paho-mqtt](https://www.eclipse.org/paho/)** → MQTT protocol for real-time data exchange  
- **[ESP32/ESP8266](https://www.espressif.com/)** → Wi-Fi-enabled microcontroller for sending RGB color updates  
- **[Arduino IDE](https://www.arduino.cc/en/software)** → Microcontroller programming for glove sensors  

### **3️⃣ Hardware Components**  
- **Webcam** → Captures hand movements for gesture recognition  
- **Arduino-compatible glove sensors** → Detects hand gestures & color changes  
- **Buzzer module** → Notifies users when they move out of bounds  
- **Wi-Fi enabled microcontroller (ESP32/ESP8266)** → Sends gesture data over MQTT  

### **4️⃣ Programming Languages**  
- **Python** → Main backend logic & real-time processing  
- **C++ (Arduino Sketches)** → Microcontroller firmware for gloves  
- **MQTT Protocol** → Wireless data exchange for sensor integration  

---

## 📃 Installation & Setup  

### **🖥️ Software Requirements**  
Ensure you have **Python 3.12+** installed. Then, install the required dependencies:  

```bash
pip install opencv-python numpy cvzone paho-mqtt
```

🔌 Hardware Setup
🛠️ Step 1: Connect the ESP32/ESP8266
Plug the ESP32/ESP8266 into your computer and upload the glove firmware using Arduino IDE.

✋ Step 2: Attach Flex Sensors
Mount flex sensors onto the glove to detect finger positions.

🔊 Step 3: Connect the Buzzer
Attach a buzzer to the microcontroller for out-of-bounds alerts.

🌐 Step 4: Configure MQTT Broker
Set up an MQTT broker and update the broker address in the Python script.

🔥 Future Improvements
✍️ 1️⃣ AI-Based Handwriting Recognition
🧠 Convert air-written text into actual editable text using machine learning models.
🔗 Potential integration with Google Handwriting Recognition API.
✏️ 2️⃣ Customizable Drawing Thickness & Pressure Sensitivity
🎚️ Allow users to adjust brush size based on finger pressure using sensor data.
📈 Dynamic brush thickness scaling with movement speed.
🎨 3️⃣ Integration with VR/AR Systems
🕶️ Create a virtual whiteboard for writing & drawing in 3D space.
🎮 Support for Leap Motion or Meta Quest hand tracking.
☁️ 4️⃣ Cloud Sync & Multi-Device Support
💾 Store gesture-based notes in the cloud for cross-device access.
🔗 Integrate Firebase or Google Drive API for storing & retrieving handwritten data.
