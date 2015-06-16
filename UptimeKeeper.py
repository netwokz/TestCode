__author__ = 'netwokz'

# Raspberry Pi Temperature Logger
# Stephen M Deane Jr
# www.thepowerofpi.com
# 6/5/2015

import time
import datetime
print("Uptime Logger\n")

initial = datetime.datetime.now().strftime("%Y/%m/%d %H:%M \n")
start = time.time()
init = 0
while True:
    # Open Log File
    f = open('/home/pi/Desktop/uptime.txt', 'a')
    now = time.time()
    delta = int(round(now - start))
    if init == 0:
        initalTime = "Inital Start: " + initial
        #outstring = initalTime + "Total: " + delta.strftime("%d day, %H hours, %M Minutes, %S Seconds \n")
        outstring = initalTime + "Total: " + str(datetime.timedelta(seconds=delta))
        init = 1
    else:
        outstring = "Total: " + str(datetime.timedelta(seconds=delta))
    print outstring
    f.write(outstring)
    f.close()

    # log temperature every 60 seconds
    time.sleep(1)
