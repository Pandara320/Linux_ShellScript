import logging
import socket
import sys
from time import sleep
from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import time
from zeroconf import ServiceInfo, Zeroconf
SUCCESS=201
CREATED=202
BAD_REQUEST=400
NOT_FOUND=404

app = Flask(__name__)
global ip_add
global ip_port
def blue(brightness):#18
    p = GPIO.PWM(12, brightness)
    p.start(1)
    sleep(5)
    #hi = input('stop')
    p.stop()
    GPIO.cleanup()
    return

def red(brightness):#26
    p = GPIO.PWM(37, brightness)
    p.start(1)
    sleep(5)
    p.stop()
    GPIO.cleanup()
    return
	
def green(brightness):#21
    p = GPIO.PWM(40, brightness)
    p.start(1)
    sleep(5)
    p.stop()
    GPIO.cleanup()
	
def white(brightness):
    p = GPIO.PWM(12, brightness)
    s = GPIO.PWM(37, brightness)
    z = GPIO.PWM(40, brightness)
    p.start(1)
    z.start(1)
    s.start(1)
    sleep(5)
    p.stop()
    z.stop()
    s.stop()
    GPIO.cleanup()

def magenta(brightness):
    p = GPIO.PWM(12, brightness)
    s = GPIO.PWM(37, brightness)
    p.start(1)
    s.start(1)
    sleep(5)
    p.stop()
    s.stop()
    GPIO.cleanup()

def cyan(brightness):
    p = GPIO.PWM(12, brightness)
    s = GPIO.PWM(40, brightness)
    p.start(1)
    s.start(1)
    sleep(5)
    p.stop()
    s.stop()
    GPIO.cleanup()

def yellow(brightness):
    p = GPIO.PWM(40, brightness)
    s = GPIO.PWM(37, brightness)
    p.start(1)
    s.start(1)
    sleep(5)
    p.stop()
    s.stop()
    GPIO.cleanup()
    
def buildError(status=NOT_FOUND,error=None):
    if error is None:
        error = {'status': status, 'error': 'Not Found: ' + request.url}
	#jsonify returns a flask.Response object
    resp = jsonify(error)
    resp.status_code = status
    return resp
@app.route('/LED')
def led():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(40, GPIO.OUT)
    color = request.args.get('color', '')
    status = request.args.get('status', '')
    brightness = int(request.args.get('intensity', ''))
    if color == "red":
        red(brightness)
    elif color == "green":
        green(brightness)
    elif color == "blue":
        blue(brightness)
    elif color == "white":
        white(brightness)
    elif color == "magenta":
        magenta(brightness)
    elif color == "cyan":
        cyan(brightness)
    elif color == "yellow":
        yellow(brightness)
    else:
        print("Wrong color", color)
        returnVal = { 'status': BAD_REQUEST, 'Error':"Invalid color"}
        return buildError(returnVal["status"], returnVal)
    #print(ip_add)
    #print(ip_port)
    returnVal = { 'IP Address':ip_add,'port number':ip_port,
    'supported color':'red, blue, green, magent, cyan, yellow, white',
    'request status': 200,'current color':color}
    return jsonify(returnVal)

if __name__ == '__main__':
    desc = {'path': '/~flaskwebserver1/'}
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",5000))
    
    ip = s.getsockname()[0]
    #print(ip)
    ip_add = str(ip)
    ip_port = str(s.getsockname()[1])
    s.close()
    info = ServiceInfo("_http._tcp.local.",
                       "Team18._http._tcp.local.",
                       socket.inet_aton(ip), 5000, 0, 0, desc, "flaskwebserver1.local.")

    zeroconf = Zeroconf()
    print("Registration of Team18's LED service")
    zeroconf.register_service(info)
    try:
        app.run(host='0.0.0.0', debug = True)
    except KeyboardInterrupt:
        pass
    finally:
        zeroconf.close()
