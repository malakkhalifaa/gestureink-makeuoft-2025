# Gesture Ink
## Overview
This project implements a hand gesture-controlled writing system using OpenCV, cvzone, and a webcam. This project is integrated with wearable technologies hardware (i.e. gloves and a camera headpiece powered by Arduino) and will translate hand gestures into a digital drawing. 

## Features 
### 1. Hand Gestures: 
- Draw function with index finer
- Lift pen with two fingers
- Tap with three fingers to undo line
### 2. Pen Colour Selection: 
- Pen Colour Selection using LED light switches
### 2. Pen Colour Selection: 
- Buzzer to indicate hand is not within camera frame
### 3. Live camera feed 
- Displays a small overlay of the user's hand movements
- Includes whiteboard backdrop and displays registered drawings

## Requirements 
### Python 
- Python 3.12
- cvzone
- OpenCV
- Numpy
### Arduino 
- Buzzer
- LED lights
- Switches
- Arduino UNO Wifi
- Arduino IDE

## Installation 

## Usage 

## Limitations/ Known Issues 
- Only one camera to track hand movement i.e. can only use at one stationary spot 
- Non-inclusive hand recognition (software is unable to read broad range of skin tones)
- Laggy strokes due to human factors (e.g. shaky hands) 

## Future Improvements 
- Utilizing ML to optimize stroke/ pen flow
- Include colour sensors/threshold to tailor to user's skin tone colour
- Integration with external camera source (i.e. ESP32-CAM)








 
