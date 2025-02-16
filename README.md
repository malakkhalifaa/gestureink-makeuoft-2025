# Gesture Ink
## Overview
This project implements a hand gesture-controlled writing system using OpenCV, cvzone, and a webcam. This project is integrated with wearable technologies hardware (i.e. gloves and a camera headpiece powered by Arduino) and will translate hand gestures into a digital drawing. 

## 🚀 Features 
### 1. ✏️ Drawing/Writing Mode
- ✌️ Index & Middle Finger Up - Activate drawing mode
- ☝️ Index Finger Up - Continue drawing
- 🤟 Three Fingers Up - Undo last annotation

### 2. 🌈 Pen Colour Selection: 
- Dynamic color changes based on MQTT messages from an external device.
- LED + switch colour selection modes

### 🎯3. Boundary Notification
- Buzzer on hardware device will notify user when hand is no longer detected on screen 

### 3. 📡 MQTT Integration
- Receives RGB values to set the annotation color.
- Sends buzzer alerts when the user moves outside a defined gesture region.
- Subscribes to multiple topics to receive updates from an external glove-based system.

### 4. 📷 Webcam & Live Feed
- Real-time hand gesture detection using OpenCV and cvzone.
- Small preview window displaying the user's webcam feed.

## 📃 Requirements 
- Python 3.12
- OpenCV (cv2)
- NumPy (numpy)
- cvzone (cvzone)
- paho-mqtt(paho.mqtt)
- Arduino IDE (for programming hardware) 

## 👇Installation 

## 👩‍💻Usage 

## 🤔 Limitations/ Known Issues 
- Only one camera to track hand movement i.e. can only use at one stationary spot 
- Non-inclusive hand recognition (software is unable to read broad range of skin tones)
- Laggy strokes due to human factors (e.g. shaky hands) 

## ⏭️Future Improvements 
- Utilizing ML to optimize stroke/ pen flow
- Include colour sensors/threshold to tailor to user's skin tone colour
- Integration with external camera source (i.e. ESP32-CAM)








 
