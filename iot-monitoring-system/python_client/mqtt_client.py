import paho.mqtt.client as mqtt
import threading
import time

BROKER = "broker.hivemq.com"
DATA_TOPIC = "shwetha/iot/data"
CONTROL_TOPIC = "shwetha/iot/control"

# Global flag to track connection status
is_connected = False

# -------- MQTT Callbacks (Updated to API v2) --------
def on_connect(client, userdata, flags, rc, properties=None):
    global is_connected
    if rc == 0:
        is_connected = True
        print("Connected to MQTT Broker!")
        client.subscribe(DATA_TOPIC)
        print("Subscribed to data topic\n")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    # Move to a new line so the message doesn't mess up the input prompt
    print(f"\n[Incoming Data]: {msg.payload.decode()}")
    print("Enter command (ON/OFF): ", end="", flush=True)

# -------- MQTT Client Setup --------
# Using CallbackAPIVersion.VERSION2 to fix the DeprecationWarning
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Connecting to broker...")
client.connect(BROKER, 1883, 60)

# Run MQTT in background thread
client.loop_start()

# --- WAIT UNTIL CONNECTED ---
while not is_connected:
    time.sleep(0.1)

# -------- Input Loop --------
print("Type ON or OFF to control LED")

while True:
    cmd = input("Enter command (ON/OFF): ").strip().upper()

    if cmd in ["ON", "OFF"]:
        client.publish(CONTROL_TOPIC, cmd)
        print(f"Command sent: {cmd}")
    else:
        print("Invalid command. Use ON/OFF")
