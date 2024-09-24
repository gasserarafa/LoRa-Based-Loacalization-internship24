import paho.mqtt.client as paho
import json
import time

thingsboardHost = "mqtt.thingsboard.cloud"
thingsboardPort = #add thingsboard port number
token = "" #device token

thingsboardClient = paho.Client(paho.CallbackAPIVersion.VERSION1,"control1")
thingsboardClient.username_pw_set(token)
thingsboardClient.connect(thingsboardHost,thingsboardPort,keepalive=60)
while not thingsboardClient.is_connected():
    thingsboardClient.loop()

fs_vals = [[-2945.2719581489378,1], [-2966.1064224075217,2], [2954.306942011762,3], [-2961.019229521074,4], [2961.831148813683,5], [-2963.227602362018,6], [2955.378992690453,7], [-2969.3388586311225,8], [-2976.3516452939184,9], [-2975.7273732475182,10], [-2973.761155299321,11], [-2982.7385219334224,12], [-2980.1613192750315,13], [-2976.6882949938913,14], [-2982.1447483360694,15], [-2990.7004176885753,16], [-2995.305914543957,17], [-3003.00631447524,18], [-3004.261629425904,19], [-3008.5002649271146,20]]
map_vals=[[31.4414218,29.9866381,22],[31.131302,29.976480,24]]
tmp_vals=[100,120,190,100,30,10,10,12,19,100,30,10]
for tmp in tmp_vals:
          
                payload = json.dumps({"Temperature": tmp})
                thingsboardClient.publish("v1/devices/me/telemetry", payload)
                print(f"Sent value {tmp}.")
                time.sleep(2)
for fs in fs_vals:
    payload = json.dumps({"frequency":fs[0],"packet number":fs[1]})
    thingsboardClient.publish("v1/devices/me/telemetry",payload)
    print(f"Sent value {fs}.")
    time.sleep(2)
for map in map_vals:
    payload = json.dumps({"longitude":map[0],"latitude":map[1],"altitude":map[2]})
    thingsboardClient.publish("v1/devices/me/telemetry",payload)
    print(f"Sent value {map}.")
    time.sleep(2)
    

thingsboardClient.disconnect()
