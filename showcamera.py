
import numpy as np
import cv2
import paho.mqtt.client as mqtt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# initialize the broker
broker = "mqtt.eclipse.org"
#broker="172.18.0.2"
topic="hw3"

def on_publish(client, message, result):
    print("message was published")

# initialize client
client = mqtt.Client("admin")
client.on_publish = on_publish
client.connect(broker,1883,60)
print ("client connected")

cap = cv2.VideoCapture(0)
print (cap)
cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)

#set a counter 
i = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print ("face detected")
    for (x,y,w,h) in faces:
       cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 0), 2)
       roi = gray[y:y+h, x:x+w]
       print (roi)       print (roi)
    # Display the resulting frame
       #cv2.imshow('frame',roi)
       _, img = cv2.imencode('.png', roi)
       msg = img.tobytes()

       # publish the message
       print ("before publishing...")
       client.publish(topic, msg, 0)
       print ("message published")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if i > 10:
        break
    i += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

    
                                                                                                                            1,1           Top
