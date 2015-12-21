import os
import sys
if os.name != 'posix':
    sys.exit('platform not supported')
import psutil

from datetime import datetime
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageDraw, ImageFont

def temperature():
    t = 76
    return "Temperature: %.1f F" \
           % (t)

def humidity():
    h = 33
    return "Humidity: %.0f %%" \
           % (h)

def garage():
    g = "open"
    return "Garage: %s " \
           % (g)

def stats(oled):
    font = ImageFont.truetype('font.ttf', 12)
    with canvas(oled) as draw:
        draw.text((0, 12), temperature(), font=font, fill=255)
        draw.text((0, 26), humidity(), font=font, fill=255)
        draw.text((0, 40), garage(), font=font, fill=255)

def main():
    oled = sh1106(port=1, address=0x3C)
    stats(oled)

if __name__ == "__main__":
    main()
