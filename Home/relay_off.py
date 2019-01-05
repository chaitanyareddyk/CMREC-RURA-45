import RPi.GPIO as GPIO
import time,sys

def f(x):
	return {
	'1':18,
	'2':17,
	'3':15,
	'4':14,
}[x]

pinNum = f(sys.argv[1]) 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinNum,GPIO.OUT)
GPIO.output(pinNum,1)
print not GPIO.input(pinNum)