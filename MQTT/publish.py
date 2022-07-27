import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

# 每间隔 1 秒钟向 xxx/topic 发送一个消息，连续发送 5 次
i=0
while 1>0:
    # 四个参数分别为：主题，发送内容，QoS, 是否保留消息
    client.publish('helium/382cd7de-74ea-4141-81c6-fda086f4bb08/rx', payload=i, qos=0, retain=False)
    print(f"send {i} to helium/topic")
    i=i+1
    time.sleep(1)

client.loop_forever()
