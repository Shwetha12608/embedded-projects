import paho.mqtt.client as mqtt
import threading

BROKER = "broker.hivemq.com"

DATA_TOPIC = "shwetha/iot/data"
CONTROL_TOPIC = "shwetha/iot/control"

# -------- MQTT Callbacks --------
def on_connect(client, userdata, flags, rc):
    print("\nConnected to MQTT Broker!")
    client.subscribe(DATA_TOPIC)
    print("Subscribed to data topic\n")

def on_message(client, userdata, msg):
    print("\nReceived:", msg.payload.decode())
    print("Enter command (ON/OFF): ", end="", flush=True)

# -------- MQTT Client --------
client = mqtt.Client(protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)

# Run MQTT in background thread
client.loop_start()

print("Type ON or OFF to control LED\n")

# -------- Input Loop --------
while True:
    cmd = input("Enter command (ON/OFF): ").strip().upper()

    if cmd in ["ON", "OFF"]:
        client.publish(CONTROL_TOPIC, cmd)
        print("Command sent:", cmd)
    else:
        print("Invalid command. Use ON/OFF")
