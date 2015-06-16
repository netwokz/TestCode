#! /usr/bin/env python
#
# Fade an LED (or one color of an RGB LED) using GPIO's PWM capabilities.
#
#
# @author Stephen M Deane Jr, 2015

import time
import RPi.GPIO as GPIO

# LED pin mapping.
red_pin = 13
green_pin = 6
blue_pin = 5

# GPIO setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Set up colors using PWM so we can control individual brightness.
RED = GPIO.PWM(red_pin, 100)
GREEN = GPIO.PWM(green_pin, 100)
BLUE = GPIO.PWM(blue_pin, 100)
RED.start(0)
GREEN.start(0)
BLUE.start(0)

def setup_pins(R,G,B):
    global red, blue, green
    red = R
    green = G
    blue = B


# Set a color by giving R, G, and B values of 0-255.
def setColor(r,g,b):
    rgb = [r,g,b]
    # Convert 0-255 range to 0-100.
    rgb = [(x / 255.0) * 100 for x in rgb]
    RED.ChangeDutyCycle(rgb[0])
    GREEN.ChangeDutyCycle(rgb[1])
    BLUE.ChangeDutyCycle(rgb[2])

#setColor(args.rgb)
#time.sleep(10)

#GPIO.cleanup()
