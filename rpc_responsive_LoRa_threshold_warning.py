import paho.mqtt.client as paho
import json
import time
import threading
import serial  # For serial communication with Arduino

# ThingsBoard MQTT configurations
thingsboardHost = "mqtt.thingsboard.cloud"
thingsboardPort =  #Add ThingsBoard port number
token = ""#device token

# Initialize serial communication with Arduino
arduino = serial.Serial('', 9600)  # Update with correct port

# Initialize the MQTT client for ThingsBoard
thingsboardClient = paho.Client(paho.CallbackAPIVersion.VERSION1, "control1")
thingsboardClient.username_pw_set(token)
thingsboardClient.connect(thingsboardHost, thingsboardPort, keepalive=60)
# Global variable to control the sending of temperature data
send_data = True

# Callback function for when a message is received (for RPC)
def on_message(client, userdata, message):
    print("Received RPC message: ", str(message.payload.decode("utf-8")))
    try:
        # Parse the received JSON message
        data = json.loads(message.payload.decode("utf-8"))
        
        # Send RPC command to Arduino via serial
        if 'params' in data:
            rpc_command = data['params']
            print(f"Sending RPC command to Arduino: {rpc_command}")
            arduino.write(rpc_command.encode())  # Send the command to Arduino
    except Exception as e:
        print(f"Error processing RPC message: {e}")

# Thread function to wait for RPC commands
def rpc_listener():
    thingsboardClient.subscribe("v1/devices/me/rpc/request/+")
    thingsboardClient.on_message = on_message
    while True:
        thingsboardClient.loop()
def send_temperature_data():
    global send_data
    tmp_vals = [100, 100, 100, 100, 300, 100, 100, 102, 109, 100, 30, 910,200,108, 120, 189, 100, 30, 109, 108, 100, 120, 109, 100, 30, 100, 100, 102, 109, 100, 30, 910,200,108, 120, 189, 100, 30, 109, 108,100, 170, 83, 180]
    for tmp in tmp_vals:
        if not send_data:
            print("Data transmission stopped.")
            break
        
        payload = json.dumps({"Temperature": tmp})
        thingsboardClient.publish("v1/devices/me/telemetry", payload)
        print(f"Sent value {tmp}.")
        time.sleep(3)

# Start RPC listener thread
rpc_thread = threading.Thread(target=rpc_listener)
rpc_thread.start()

# Wait for the connection to be established
while not thingsboardClient.is_connected():
    thingsboardClient.loop()

# Start sending temperature data
send_temperature_data()

# Disconnect from ThingsBoard
thingsboardClient.disconnect()

# Keep the script running
while True:
    time.sleep(1)
