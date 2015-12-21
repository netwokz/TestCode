__author__ = 'netwokz'

# Raspberry Pi Temperature Logger Stephen M Deane Jr 
# www.thepowerofpi.com 6/5/2015

import time 
import datetime 
import weather 
import Adafruit_CharLCD as LCD
import RPi.GPIO as io

# Raspberry Pi pin configuration:
lcd_rs        = 27  
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4 # Currently not used
doorSwitch    = 12
relayPin      = 16


# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# String Templates
mTemp = "Temperature: "
mHum  = "Humidity: "

# Button Setup
io.setmode(io.BCM)
io.setup(20, io.IN, pull_up_down=io.PUD_UP)
io.setup(21, io.IN, pull_up_down=io.PUD_UP)
io.setup(doorSwitch,io.IN,pull_up_down=io.PUD_UP)
io.setup(relayPin, io.OUT)
isGarageClosed = False
mLastView = 0 # 0 = temp, 1 = Garage


# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def temperature():
    temp = weather.return_weather()
    return temp 

def showTemp():
    outvalue = temperature()
    lcd.clear()
    lcd.message(mTemp + str(outvalue[0]) + "F \n" + mHum + str(outvalue[1]) + "% ")
    mLastView = 0

def showGarage():
    activateGarage()
    lcd.clear()
    mClosed = "Closed"
    mOpen = "Open"
    garage = ""
    if isGarageClosed == True:
        garage = "Garage is Closed"
    else:
        garage = "Garage is Open"
    lcd.message(garage)
    mLastView = 1

def showView():
    if mLastView == 0:
        showTemp()
    elif mLastView == 1:
        showGarage()

def activateGarage():
    io.output(relayPin, 0)
    time.sleep(1)
    io.output(relayPin, 1)

try:
    while True:   
    	temp = io.input(20)
    	garage = io.input(21)
        if temp == False:
            showTemp()
        elif garage == False:
            showGarage()
        if io.input(doorSwitch):
            isGarageClosed = False
        else:
            isGarageClosed = True
        #showView()
            
except KeyboardInterrupt:
    lcd.clear()
