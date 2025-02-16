#include <Arduino.h>
#include <WiFiNINA.h>
#include <Wire.h>
#include <ArduinoMqttClient.h>
// #include <login.h>

const char *ssid = "UofT";
const char *username = "";
const char *password = "";
const char* mqtt_server = "";
int port = 443;
const char *mqtt_username = "";
const char *mqtt_password = "";

unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE (500)
char msg[MSG_BUFFER_SIZE];
WiFiSSLClient client;
MqttClient mqttClient(client);
const char twoTopic[] = "arduino/glove/colour";
const char oneTopic[] = "arduino/glove/bent_strip";
const char threeTopic[] = "python/buzzer";

const long interval = 80000;
unsigned long previousMillis = 0;
int rLED = 13;
int gLED = 12;
int bLED = 11;
int buzzerPin = 8;

void mqttSend(String topic, String payload){
  mqttClient.beginMessage(topic);
  mqttClient.print(payload);
  mqttClient.endMessage();
  Serial.println("message sent");
}

void mqtt_parseSend(String topic, String JSONText){
  int total = 0;
  while(total < JSONText.length()){
    String parsed_text = "";
    for (int i=0; i < 128; i++){
      parsed_text += JSONText[total+i];
    }
    total += 128;
    Serial.println(parsed_text);
    mqttSend(topic, parsed_text);
  }
}

void callback(unsigned int length) {
  Serial.println("callback fired");

  // read topic
  String topic = mqttClient.messageTopic();

  // read payload
  String payload_mqtt = "";
  while (mqttClient.available()){
    payload_mqtt += String((char)mqttClient.read());
  }

  int receivedValue = payload_mqtt.toInt();

  // trace
  Serial.println(topic);
  Serial.println(payload_mqtt);

  if (topic == "python/buzzer") {
    if(receivedValue == 0){
      digitalWrite(buzzerPin, LOW);
    }
    if(receivedValue == 1){
      digitalWrite(buzzerPin, HIGH);
    }
  }
}

void reconnect() {
  // Loop until we’re reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection…");

    mqttClient.setUsernamePassword(mqtt_username, mqtt_password);
    mqttClient.onMessage(callback);

    if (!mqttClient.connect(mqtt_server, 8883)){

      Serial.print("MQTT connection failed! Error code = ");
      Serial.println(mqttClient.connectError());
      delay(5000);
    } else {
        mqttClient.subscribe("python/buzzer");
    }
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(rLED, INPUT);
  pinMode(gLED, INPUT);
  pinMode(bLED, INPUT);
  pinMode(buzzerPin, OUTPUT);

  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  //while(WiFi.begin(ssid, password) != WL_CONNECTED){
  while(WiFi.beginEnterprise(ssid, username, password) != WL_CONNECTED){
    delay(5000);
    Serial.print(".");
    }
  Serial.println("You're connected to the network");
  mqttClient.setUsernamePassword(mqtt_username, mqtt_password);
  mqttClient.onMessage(callback);

  if (!mqttClient.connect(mqtt_server, 8883)){
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  mqttClient.subscribe("python/buzzer");
}

void loop() {
  mqttClient.poll();

  int red = digitalRead(rLED);
  int green = digitalRead(gLED);
  int blue = digitalRead(bLED);
  Serial.println(blue);
  char message[50];  // Buffer to hold formatted string
  snprintf(message, sizeof(message), "R: %d, G: %d, B: %d", red, green, blue);
  //snprintf(message, sizeof(message), "R: 1, G: 0, B: 1");
  mqttSend("arduino/glove/colour", message);
  delay(3000);

  reconnect();
  
}
