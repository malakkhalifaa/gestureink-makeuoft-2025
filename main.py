import cv2
import os
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import paho.mqtt.enums
import paho.mqtt.client as mq
import re

# Parameters
width, height = 1280, 720
gesture_threshold = 300
folder_path = "Presentation"


# Camera Setup
capture = cv2.VideoCapture(0)
capture.set(3, width)
capture.set(4, height)


# Hand Detector
hand_detector = HandDetector(detectionCon=0.8, maxHands=1)


# Variables
image_list = []
delay_time = 30
button_is_pressed = False
frame_counter = 0
is_draw_mode = False
current_image_index = 0
delay_counter = 0
annotations = [[]]
annotation_index = -1
annotation_started = False
small_img_height, small_img_width = int(120 * 1), int(213 * 1)  # width and height of the small image
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
    rgb_value = (red*255, green * 255, blue * 255)
    return rgb_value

def on_msg(client, userdata, message:mq.MQTTMessage):
    topic = message.topic
    if topic == "arduino/glove/colour":
        msg = message.payload.decode("utf-8")
        msg = parse_rgb_message(msg)
        rgb_value = msg
        # change colour setting to true/false
        print("topic", topic, "message", msg)
        return (topic, msg)

def on_send(client, userdata, mid, reason_code, properties):
    print(mid, "published")

def on_sub(client, userdata, mid, granted_qos, _):
    print("granted qos", granted_qos)

# Get list of presentation images
image_paths = sorted(os.listdir(folder_path), key=len)
print(image_paths)

# Place the MQTT client setup outside the loop
client.on_message = on_msg
client.on_connect = on_connect
client.on_subscribe = on_sub
client.on_publish = on_send
client.username_pw_set(USER, PASS)
client.tls_set(tls_version=TLS_VERSION)
#client.tls_insecure_set(False)
client.connect(URL, PORT)

client.subscribe("arduino/photo", qos=1)
client.subscribe("arduino/glove/colour", qos=1)
client.subscribe("arduino/bent", qos=1)

while True:
    # Capture frame
    success, frame = capture.read()
    frame = cv2.flip(frame, 1)
    current_image_path = os.path.join(folder_path, image_paths[current_image_index])
    current_image = cv2.imread(current_image_path)


    # Detect hand and landmarks
    hands, frame = hand_detector.findHands(frame)  # with draw
    # Draw Gesture Threshold line
    cv2.line(frame, (0, gesture_threshold), (width, gesture_threshold), (rgb_value), 10)


    if hands and not button_is_pressed:  # If hand is detected


        hand = hands[0]
        center_x, center_y = hand["center"]
        landmark_list = hand["lmList"]  # List of 21 Landmark points
        fingers_up = hand_detector.fingersUp(hand)  # List of which fingers are up


        # Constrain values for easier drawing
        x_value = int(np.interp(landmark_list[8][0], [width // 2, width], [0, width]))
        y_value = int(np.interp(landmark_list[8][1], [150, height - 150], [0, height]))
        index_finger_position = (x_value, y_value)


        if center_y <= gesture_threshold:  # If hand is at the height of the face
            client.publish("python/buzzer", "0", qos=1)
            if fingers_up == [1, 0, 0, 0, 0]:
                print("Left")
                button_is_pressed = True
                if current_image_index > 0:
                    current_image_index -= 1
                    annotations = [[]]
                    annotation_index = -1
                    annotation_started = False
            if fingers_up == [0, 0, 0, 0, 1]:
                print("Right")
                button_is_pressed = True
                if current_image_index < len(image_paths) - 1:
                    current_image_index += 1
                    annotations = [[]]
                    annotation_index = -1
                    annotation_started = False
        else:
            client.publish("python/buzzer", "1", qos=1)


        if fingers_up == [0, 1, 1, 0, 0]:
            cv2.circle(current_image, index_finger_position, 12, (rgb_value), cv2.FILLED)


        if fingers_up == [0, 1, 0, 0, 0]:
            if not annotation_started:
                annotation_started = True
                annotation_index += 1
                annotations.append([])
            print(annotation_index)
            annotations[annotation_index].append(index_finger_position)
            cv2.circle(current_image, index_finger_position, 12, (rgb_value), cv2.FILLED)


        else:
            annotation_started = False


        if fingers_up == [0, 1, 1, 1, 0]:
            if annotations:
                annotations.pop(-1)
                annotation_index -= 1
                button_is_pressed = True


    else:
        annotation_started = False


    if button_is_pressed:
        frame_counter += 1
        if frame_counter > delay_time:
            frame_counter = 0
            button_is_pressed = False


    for i, annotation in enumerate(annotations):
        for j in range(len(annotation)):
            if j != 0:
                cv2.line(current_image, annotation[j - 1], annotation[j], ((rgb_value)), 12)


    small_img = cv2.resize(frame, (small_img_width, small_img_height))
    img_height, img_width, _ = current_image.shape
    current_image[0:small_img_height, img_width - small_img_width: img_width] = small_img


    cv2.imshow("Slides", current_image)
    cv2.imshow("Image", frame)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    client.loop_forever



