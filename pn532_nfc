# Example of detecting and reading a block from a MiFare NFC card.
# Author: Tony DiCola
# Copyright (c) 2015 Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import binascii
import Adafruit_PN532 as PN532
import time

# Configuration for a Raspberry Pi:
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

current_id = None
last_id = []
pn532 = None

mSavedCards = []

def check_uid(uid):
    if uid in mSavedCards:
        print 'Access Granted'
        return True
    else:
        print "Access Denied"
        return False

def setup_reader():
    global pn532
    global mSavedCards
    mSavedCards.append('00ad0b11')
    # Create an instance of the PN532 class.
    pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
    # Call begin to initialize communication with the PN532.
    pn532.begin()
    # Configure PN532 to communicate with MiFare cards.
    pn532.SAM_configuration()

def get_uid():
    while True:
        # Check if a card is available to read.
        uid = pn532.read_passive_target()
        # Try again if no card is available.
        if uid is None:
            continue
        print 'Found card with UID: ', binascii.hexlify(uid)
        _id = str(binascii.hexlify(uid))
        return _id


def get_firmware_version():
    # Get the firmware version from the chip and print it out.
    ic, ver, rev, support = pn532.get_firmware_version()
    print 'Found PN532 with firmware version: {0}.{1}'.format(ver, rev)

# Main loop to detect cards
print 'Waiting for MiFare card...'
setup_reader()
while True:
    global card_id
    card_id = get_uid()
    check_uid(card_id)
    time.sleep(3)
    
    
