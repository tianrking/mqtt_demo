# subscriber.py
import paho.mqtt.client as mqtt
# from flask import Flask, request, jsonify,render_template
import json
import base64
import pandas as pd
import datetime as dt
import time

def on_connect(client, userdata, flags, rc):
    client.subscribe("helium/8730a475-49b5-440d-9b21-d4f9c1f1a4ae/rx")
    
# Callback function, which is triggered when a message is received
def on_message(client, userdata, msg):
    #print(f"{msg.topic} {msg.payload}")
    #print(msg.payload.decode('utf-8'))
    uplink_data = msg.payload.decode('utf-8')
    uplink_data = json.loads(uplink_data)
    #decode_data = base64.b64decode(uplink_data['payload'])
    print(uplink_data) 
    try:
        flag = uplink_data['decoded']['payload']
        print(flag)
        temperature = flag["temp"]
        humidity = flag["humi"]
    
        try:
            df = pd.read_excel("test.xlsx",sheet_name="Sheet1",header=0)
            df = df.append({'Time':dt.datetime.now(),'Temperature':temperature,'Humidity':humidity},ignore_index=True)
            df = df.set_index('Time')
            df.to_excel("data.xlsx")
        except:
            df = pd.DataFrame({'Time':[],'Temperature':[],'Humidity':[]})
            df = df.set_index('Time')
            df.to_excel('data.xlsx')
    

        print(df.shape)
    
    except:
        print("Network Error")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Set up a will message to send a will message to other clients when the Raspberry Pi loses power, or when there is an abnormal network outage

client.will_set('helium/8730a475-49b5-440d-9b21-d4f9c1f1a4ae/rx',  b'{"status": "Off"}')

# Create a connection with three parameters: broker address, broker port number, and keep-alive time
client.connect("broker.emqx.io", 1883, 60)

# Set the network loop to block and not actively end the program until disconnect() is called or the program crashes
client.loop_forever()

