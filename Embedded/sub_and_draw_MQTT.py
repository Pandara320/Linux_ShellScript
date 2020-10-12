import paho.mqtt.client as mqtt  # import the client1
import json
import matplotlib.pyplot as plt
import time
import math
from collections import deque , defaultdict

import matplotlib.animation as animation
from matplotlib import pyplot as plt
import threading
from random import randint
#import DataPlot and RealtimePlot from the file plot_data.py
from plot_data import DataPlot, RealtimePlot
from plot_data import DataPlot2, RealtimePlot2

countNum = 0

# 4 data in one graph in one figure
fig, axes = plt.subplots()
plt.title('Pixy RealTime Plot [ON/OFF, Sequence, Direction, Color] vs MsgID')
data = DataPlot();
dataPlotting = RealtimePlot(axes)

# 1 data in four graph in one figure
fig1 = plt.figure()
axes1 = fig1.add_subplot(2, 2, 1)
plt.title('Pixy Data [ON/OFF]')
data_onoff = DataPlot2()
dataPlotting_onoff = RealtimePlot2(axes1)

axes2 = fig1.add_subplot(2, 2, 2)
plt.title('Pixy Data [Sequence]')
data_seq = DataPlot2()
dataPlotting_seq = RealtimePlot2(axes2)

axes3 = fig1.add_subplot(2, 2, 3)
plt.title('Pixy Data [Direction]')
data_direct = DataPlot2()
dataPlotting_direct = RealtimePlot2(axes3)

axes4 = fig1.add_subplot(2, 2, 4)
plt.title('Pixy Data [Color]')
data_color = DataPlot2()
dataPlotting_color = RealtimePlot2(axes4)



# serverAddress = '192.168.127.1'
jakePubTopic = [("/Team11/Jake_pub",0)]

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        print("[Note] Connection: Success")
    else:
        print("[Error] Connection: Failure")

    client.subscribe(jakePubTopic)

def on_message(client, userdata, msg):
    jstat = msg.payload.decode()
    # print(jstat)
    msg_stat = json.loads(jstat)
    # print
    # get the json parsed data
    msgID = msg_stat['MSGID']
    OSDC_code = msg_stat['OSDC']
    OSDC_list = [int(x) for x in str(OSDC_code)]
    # split the OSDC code into list for 4 types data
    detection_code = OSDC_list[0]
    sequence_code = OSDC_list[1]
    direction_code = OSDC_list[2]
    color_code = OSDC_list[3]
    global countNum
    # osdc_type = type(OSDC_code)
    # print(osdc_type) OSDC_code is a int
    try:
            # data addition
            data.add(msgID, detection_code, sequence_code, direction_code, color_code)

            data_onoff.add2(msgID, detection_code)
            data_seq.add2(msgID, sequence_code)
            data_direct.add2(msgID, direction_code)
            data_color.add2(msgID, color_code)

            # data plot
            dataPlotting.plot(data)

            dataPlotting_onoff.plot2(data_onoff);
            dataPlotting_seq.plot2(data_seq);
            dataPlotting_direct.plot2(data_direct);
            dataPlotting_color.plot2(data_color);

            countNum += 1

            plt.pause(0.005)
    except KeyboardInterrupt:
        print('\n\nLimit Reached, close signal received. Exiting.')
        plt.close()
        ser.close()
        exit()

# Connect the clients to ip
# set paho.mqtt callback
ttn_client = mqtt.Client()
ttn_client.connect("192.168.127.1", 1883, 60)
ttn_client.on_connect = on_connect
ttn_client.on_message = on_message

# Start client loops
ttn_client.loop_forever()
