#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math

DO = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    ADC.setup(0x48)
    GPIO.setup(DO, GPIO.IN)


def getTemp():
    analogVal = ADC.read(0)
    Vr = (float(analogVal)/(255*3.3))
    temp = 1/(((math.log((10000 * Vr/(3.3 - Vr)) / 10000)) / 3950) + (1 / (273.15+25)))
    temp = temp - 273.15
    temp = temp - 100
##    if temp > 33:
##        tmp = 0
##    elif temp < 31:
##        tmp = 1
##
##    if tmp != status:
##        print(tmp)
##        status = tmp
    return temp

  
