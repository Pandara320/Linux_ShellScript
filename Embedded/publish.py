import paho.mqtt.client as mqtt
import time
import json
import random

client=mqtt.Client()
#client.connect("localhost",1883,60)
client.connect("192.168.127.1", 1883,60)

count=0
drop=0
while(1):

	count=count+1
	msg="Arm Signal Test[Teamxx], this is a test for PixyCam: count " + str(count)
	dict={"Publish_Board_ID":"Jake", "Message_ID":str(count) , "Message_Content": msg}
	j=json.dumps(dict)
	print(j)
	client.publish("/Teamxx/Jake_pub",j);
	print(" "+time.asctime(time.localtime(time.time() ) ) )
	time.sleep(0.5)
	#client.disconnect();
