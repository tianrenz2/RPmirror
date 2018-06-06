import RPi.GPIO as GPIO
import time
 

def light():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.IN)
##    for i in range(0,5):
##        print(str(GPIO.input(4)))
##        time.sleep(5)
    if GPIO.input(4) == 0:
        return 1
    else:
        return 0
