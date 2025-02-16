import paho.mqtt.enums
import paho.mqtt.client as mq
import re

# MQTT Login info
URL = ""
USER = "n"
PASS = ""

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


client.on_message = on_msg
client.on_connect = on_connect
client.on_subscribe = on_sub
client.on_publish = on_send
client.username_pw_set(USER, PASS)
client.tls_set(tls_version=TLS_VERSION)
client.connect(URL, PORT)

#client.publish("python/buzzer", str(0), qos=1)
client.publish("python/buzzer", "1", qos=1)

client.subscribe("arduino/photo", qos=1)
client.subscribe("arduino/glove/colour", qos=1)
client.subscribe("arduino/bent", qos=1)

client.loop_forever()
