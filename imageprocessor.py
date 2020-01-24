
from datetime import datetime

import numpy as np
import paho.mqtt.client as mqtt


# name the bucket
bucket_name = 'hw3'


# Store IP address for broker -- this is the ip of the jetson
broker_ip = "10.0.0.191"

# topic for subscription
topic = "hw3"

#mounted my object storage to my VS
output_dir = "/mnt/mybucket" 

# choosing QoS 0 because not critical to lose data for this project!
qos_level = 0

# callback when connection occurs
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        client.subscribe(topic)
    print("connected: ", not bool(rc))


# callback for when message is received
def on_message(client, userdata, message):
    print("message received ")
    print("topic: ", message.topic)
    print("qos: ", message.qos)

    # generate unique timestamp so image naming is unique
    file_name = 'face_{}.png'.format(
        str(datetime.timestamp(datetime.now())).split('.')[0])
        
    # write image in Object Storage
    cv.imwrite(output_dir+"/"+file_name, img)


# Initialize a client
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

# Connect to broker
client.connect(broker_ip)

# loop forever to grab all messages
client.loop_forever()
