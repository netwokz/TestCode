__author__ = 'netwokz'

# Raspberry Pi Temperature Logger
# Stephen M Deane Jr
# www.thepowerofpi.com
# 6/5/2015

import datetime
print("Uptime Logger\n")

start = time.time()

while True:
    timestamp.strftime("%Y/%m/%d %H:%M")
    # Open Log File
    f = open('uptime.txt', 'a')
    now = time.time()
    delta = now - start
    
    
    outstring = "Total: " + delta.strftime("%d day, %H hours, %M Minutes, %S Seconds \n")
    print outstring
    f.write(outstring)
    f.close()

    # log temperature every 60 seconds
    time.sleep(60)
