#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ArduinoJson.h>

// -------- WiFi --------
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// -------- MQTT --------
const char* mqtt_server = "broker.hivemq.com";
WiFiClient espClient;
PubSubClient client(espClient);

// -------- Topics --------
const char* pub_topic = "shwetha/iot/data";
const char* sub_topic = "shwetha/iot/control";

// -------- LED --------
#define LED_PIN 2

// -------- Sensor --------
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// -------- WiFi --------
void connectWiFi() {
  WiFi.begin(ssid, password);
  Serial.print("Connecting WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected!");
}

// -------- MQTT Callback --------
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message received: ");

  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.println(message);

  // Control LED
  if (message == "ON") {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("LED ON");
  } else if (message == "OFF") {
    digitalWrite(LED_PIN, LOW);
    Serial.println("LED OFF");
  }
}

// -------- MQTT Connect --------
void connectMQTT() {
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  while (!client.connected()) {
    Serial.print("Connecting MQTT...");
    if (client.connect("ESP32Client_Shwe")) {
      Serial.println("Connected!");
      client.subscribe(sub_topic);  // subscribe for control
    } else {
      Serial.print("Failed, rc=");
      Serial.println(client.state());
      delay(2000);
    }
  }
}

// -------- Send Data --------
void sendMQTT(float temp, int light) {
  StaticJsonDocument<200> doc;
  doc["temperature"] = temp;
  doc["light"] = light;

  String payload;
  serializeJson(doc, payload);

  client.publish(pub_topic, payload.c_str());

  Serial.println("Data Sent:");
  Serial.println(payload);
}

// -------- Setup --------
void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  dht.begin();

  connectWiFi();
  connectMQTT();
}

// -------- Loop --------
void loop() {
  if (!client.connected()) {
    connectMQTT();
  }
  client.loop();

  float temp = dht.readTemperature();
  int light = analogRead(34);

  if (!isnan(temp)) {
    sendMQTT(temp, light);
  }

  delay(5000);
}
