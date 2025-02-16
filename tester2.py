import cv2
import os
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import paho.mqtt.enums
import paho.mqtt.client as mq
import re

# Parameters
width, height = 1280, 720
gestureThreshold = 300
folderPath = "Presentation"

# Camera Setup
# will probably import video via http here
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detectorHand = HandDetector(detectionCon=0.8, maxHands=1)

# Variables
imgList = []
delay = 30
buttonPressed = False
counter = 0
drawMode = False
imgNumber = 0
delayCounter = 0
annotations = [[]]
annotationNumber = -1
annotationStart = False
hs, ws = int(120 * 1), int(213 * 1)  # width and height of small image
rgb_value = (0, 0, 0)
outofboundstopic = "python/buzzer"

# MQTT Login info
URL = "82a6cf24592241609f0c78d6c926b55d.s1.eu.hivemq.cloud"
USER = "Python"
PASS = "Cooked234"

PORT = 8883
VERSION = paho.mqtt.enums.CallbackAPIVersion.VERSION2
TLS_VERSION = mq.ssl.PROTOCOL_TLS

client = mq.Client(VERSION)

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code", reason_code)

def parse_rgb_message(message):
    # Extract numbers using regex
    match = re.search(r'R:\s*(\d+),\s*G:\s*(\d+),\s*B:\s*(\d+)', message)
    if not match:
        return "Invalid message format"

    # Convert extracted values to integers
    red, green, blue = map(int, match.groups())

    # Convert binary (0/1) to 8-bit RGB (0 or 255)
    rgb_value = (red * 255, green * 255, blue * 255)

def on_msg(client, userdata, message:mq.MQTTMessage):
    topic = message.topic
    if topic == "arduino/glove/colour":
        msg = message.payload.decode("utf-8")
        msg = parse_rgb_message(msg)
        # change colour setting to true/false
        print("topic", topic, "message", msg)
        return (topic, msg)

def on_send(client, userdata, mid, reason_code, properties):
    print(mid, "published")

def on_sub(client, userdata, mid, granted_qos, _):
    print("granted qos", granted_qos)

# Get list of presentation images
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

while True:
    client.on_message = on_msg
    client.on_connect = on_connect
    client.on_subscribe = on_sub
    client.on_publish = on_send
    client.username_pw_set(USER, PASS)
    client.tls_set(tls_version=TLS_VERSION)
    client.connect(URL, PORT)

    client.subscribe("arduino/photo", qos=1)
    client.subscribe("arduino/glove/colour", qos=1)
    client.subscribe("arduino/bent", qos=1)
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    # Find the hand and its landmarks
    hands, img = detectorHand.findHands(img)  # with draw
    # Draw Gesture Threshold line
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (rgb_value), 10)

    if hands and buttonPressed is False:  # If hand is detected

        hand = hands[0]
        cx, cy = hand["center"]
        lmList = hand["lmList"]  # List of 21 Landmark points
        fingers = detectorHand.fingersUp(hand)  # List of which fingers are up

        # Constrain values for easier drawing
        xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))
        indexFinger = xVal, yVal

        if cy <= gestureThreshold:  # If hand is at the height of the face
            if fingers == [1, 0, 0, 0, 0]:
                print("Left")
                buttonPressed = True
                if imgNumber > 0:
                    imgNumber -= 1
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False
            if fingers == [0, 0, 0, 0, 1]:
                print("Right")
                buttonPressed = True
                if imgNumber < len(pathImages) - 1:
                    imgNumber += 1
                    annotations = [[]]
                    annotationNumber = -1
                    annotationStart = False

        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 12, (rgb_value), cv2.FILLED)

        if fingers == [0, 1, 0, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            print(annotationNumber)
            annotations[annotationNumber].append(indexFinger)
            cv2.circle(imgCurrent, indexFinger, 12, (rgb_value), cv2.FILLED)

        else:
            annotationStart = False

        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                annotations.pop(-1)
                annotationNumber -= 1
                buttonPressed = True

    else:
        annotationStart = False

    if buttonPressed:
        counter += 1
        if counter > delay:
            counter = 0
            buttonPressed = False

    for i, annotation in enumerate(annotations):
        for j in range(len(annotation)):
            if j != 0:
                cv2.line(imgCurrent, annotation[j - 1], annotation[j], (rgb_value), 12)

    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws: w] = imgSmall

    cv2.imshow("Slides", imgCurrent)
    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    # out of bounds condition
    # if hand is out of bounds:
    # client.publish(outofboundstopic, str(1), qos=1)
    # if hand is in bounds (to stop buzzing):
    # client.publish(outofboundstopic, str(0), qos=1)