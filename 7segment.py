#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import weather
 
SDI   = 11
RCLK  = 12
SRCLK = 13
SDI2   = 15
RCLK2  = 16
SRCLK2 = 18
weatherPin = 29
buttonPin = 7

# Number of seconds allowed between refreshes
delta = 5
lastRefresh = 0

repeat = False

# 0x3f = 0
# 0x06 = 1
# 0x5b = 2
# 0x4f = 3
# 0x66 = 4
# 0x6d = 5
# 0x7d = 6
# 0x07 = 7
# 0x7f = 8
# 0x6f = 9

# 0x77 = A
# 0x7c = B
# 0x39 = C
# 0x5e = D
# 0x79 = E
# 0x71 = F

# 0x76 = H

# 0x80 = .
 
segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]
numCode = {"0":'0x3f',"1":'0x06',"2":'0x5b',"3":'0x4f',"4":'0x66',"5":'0x6d',"6":'0x7d',"7":'0x07',"8":'0x7f',"9":'0x6f'}
numCode2 = {"0":0x3f,"1":0x06,"2":0x5b,"3":0x4f,"4":0x66,"5":0x6d,"6":0x7d,"7":0x07,"8":0x7f,"9":0x6f}
letCode = {"A":0x77,"B":0x7c,"C":0x39,"D":0x5e,"E":0x79,"F":0x71}
 
def print_msg():
    print 'Please press Ctrl+C to end the program...'

def button_callback(channel):
    global lastRefresh
    global repeat
    print "button Pressed!"
    print int(time.time() - lastRefresh)
    if (int(time.time() - lastRefresh) > delta):
        repeat = False
        repeat = True
        lastRefresh = time.time()
        getTemp()
        #time.sleep(0.2)
        
 
def setup():
    GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location
    GPIO.setwarnings(False)

    # Shift Register 1 for LED 1
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)

    # Shift Register 2 for LED 2
    GPIO.setup(SDI2, GPIO.OUT)
    GPIO.setup(RCLK2, GPIO.OUT)
    GPIO.setup(SRCLK2, GPIO.OUT)
    GPIO.output(SDI2, GPIO.LOW)
    GPIO.output(RCLK2, GPIO.LOW)
    GPIO.output(SRCLK2, GPIO.LOW)

    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=button_callback, bouncetime=200)
 
def led_1(dat):
    for bit in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def led_2(dat):
    for bit in range(0, 8):
        GPIO.output(SDI2, 0x80 & (dat << bit))
        GPIO.output(SRCLK2, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK2, GPIO.LOW)
    GPIO.output(RCLK2, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK2, GPIO.LOW)

def printTemp(temperature,humidity):
    temp = int(temperature)
    temp = str(temp).zfill(2)

    hum = int(humidity)
    hum = str(hum).zfill(2)

    while repeat is True:
        if (repeat is False):
            break
        led_1(segCode[int(temp[0])])
        led_2(segCode[int(temp[1])])
        time.sleep(2)
        led_1(int(0x00))
        led_2(int(0x00))
        led_1(segCode[int(hum[0])])
        led_2(segCode[int(hum[1])])
        time.sleep(2)
        led_1(int(0x00))
        led_2(int(0x00))
    

def getTemp():
    temp, hum = weather.get_weather()
    printTemp(temp,hum)
 
def destroy():   #When program ending, the function is executed.
    led_1(int(0x00))
    led_2(int(0x00))
    GPIO.cleanup()
 
if __name__ == '__main__': #Program starting from here
    print_msg()
    setup()

    try:
        GPIO.wait_for_edge(buttonPin,GPIO.FALLING)
        print "\nFalling Edge Detected"
    except KeyboardInterrupt:
        GPIO.cleanup()

    repeat = True
    lastRefresh = time.time()
    getTemp()
    
    #try:
    #    while True:
    #        time.sleep(1)            
    #    
    #except KeyboardInterrupt: 
    #    destroy()
