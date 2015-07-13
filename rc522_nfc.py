import MFRC522
import signal
import time
import rgb_pwm as led
import RPi.GPIO as GPIO

mTagCard = [0,173,11,17,183]
mTagKey = [68,67,183,150,38]
mLastTag = []
mCount = 0
mDelta = 3

RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]

run = True
DEBUG = False
#savedUID = [mTagCard, mTagKey]
savedUID = [mTagCard]

def end_read(signal,frame):
    global run
    print "\nEnding read."
    run = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

print "Starting"

def check_uid(uid):
    if uid in savedUID:
        check_last_uid(uid)
        return True
    else:
        print "Tag Not added yet"
        check_last_uid(uid)
        return False

def add_uid(uid):
    global savedUID
    savedUID.append(uid)

def check_last_uid(uid):
    global mCount, mLastTag
    if uid == mLastTag:
        mCount += 1
        if DEBUG:
            print mCount
        if mCount == mDelta:
            add_uid(uid)
            mCount = 1
        else:
            mLastTag = uid
    else:
        if DEBUG:
            print mCount
            
        mLastTag = uid
        mCount = 1
        if DEBUG:
            print mCount

while run:
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]) + "," + str(uid[4])

        if check_uid(uid):
            print "Already saved"
            led.setColor(GREEN)
            time.sleep(2)
            led.turnOff()
        else:
            led.setColor(RED)
            time.sleep(2)
            led.turnOff()
            #add_uid(uid)
        if DEBUG:
            for id in savedUID :
                print id
                
