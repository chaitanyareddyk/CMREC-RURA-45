import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = [18,17,15,14] 

GPIO.setup(pins, GPIO.OUT)




GPIO.cleanup()
print "Shutdown All relays"
