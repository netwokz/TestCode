#!/usr/bin/env python

#import modules used in script
import random, time
import RPi.GPIO as GPIO

# Set GPIO to Broadcom system and set RGB Pins
GPIO.setmode(GPIO.BCM)
red = 5
green = 6
blue = 13
doorSwitch = 18

door=0

RGB = [red,green,blue]
for pin in RGB:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

GPIO.setup(doorSwitch,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def turnRedOn():
    GPIO.output(red,1)
    return
    
def turnRedOff():
    GPIO.output(red,0)
    
def turnGreenOn():
    GPIO.output(green,1)
    
def turnGreenOff():
    GPIO.output(green,0)
    
def turnBlueOn():
    GPIO.output(blue,1)
    
def turnBlueOff():
    GPIO.output(blue,0)
try:
    while True:
        if GPIO.input(doorSwitch):
            door=0
            turnGreenOff()
            turnRedOn()
            time.sleep(1)
        if (GPIO.input(doorSwitch)==False and door!=1):
            door=1
            turnRedOff()
            turnGreenOn()
except KeyboardInterrupt:
    GPIO.cleanup()
    
            

