import RPi.GPIO as GPIO
import time
import json

pins = [18,17,15,14]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

arr = []
for x in range(0,4) : 
	GPIO.setup(pins[x],GPIO.OUT)
	arr.append(not GPIO.input(pins[x]))

print json.dumps({0:arr[0],1:arr[1],2:arr[2],3:arr[3]})

