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
    
    
