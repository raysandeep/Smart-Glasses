'''
 - > sudo raspi-config
 - > sudo apt install -y python3-dev
 - > sudo apt install -y python-imaging python-smbus i2c-tools
 - > sudo apt install -y python3-pil
 - > sudo apt install -y python3-pip
 - > sudo apt install -y python3-setuptools
 - > sudo apt install -y python3-rpi.gpio
 - > i2cdetect -y 1
 - > sudo apt install -y git
 - > git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
 - > cd Adafruit_Python_SSD1306
 - > sudo python3 setup.py install 

Refer - > https://www.instructables.com/id/Temperature-and-Humidity-Chart-With-OLED-Display/


Sample ECG Data : 


436,285
389,285
391,285
432,285
436,285
400,285
405,285
443,285
458,285
420,285
403,285
442,285
457,285
409,285
392,285
434,285
464,285






'''


# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)




import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()

# Clear display.
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

##Defining constants
padding = -2
top = padding
bottom = height-padding
x = 0


# Load default font.
font = ImageFont.load_default()

#ECG Graph
disp.fillScreen (BLACK)

disp.drawFastVLine (POS_X_GRAPHIC, POS_Y_GRAPHIC, GRAPHIC_HEIGHT, WHITE)
disp.drawFastHLine (POS_X_GRAPHIC, HEIGHT_GRAPHIC + 1, GRAPHIC_LENGTH, WHITE)

disp.drawPixel (4.2, WHITE)
disp.drawPixel (6.2, WHITE)

disp.drawPixel (POS_X_GRAPHIC + GRAPHIC-LENGTH-2, POS_Y_GRAPHIC + GRAPHIC-HEIGHT-1, WHITE)
disp.drawPixel (POS_X_GRAPHIC + GRAPHIC-LENGTH-2, POS_Y_GRAPHIC + GRAPHIC HEIGHT + 1, WHITE)

display.setTextSize (1)
display.setTextColor (WHITE)
 display.setCursor (POS_X_DATA, POS_Y_DATA)
display.print ("T:")
display.setCursor (POS_X_DATA + 35, POS_Y_DATA)
display.print ("U:")


Pulse = "v"
Name = "Akshat Gupta"
Mess = "Pass Knife"

draw.text((x, top),       "PULSE: " + str(Pulse),  font=font, fill=255)
draw.text((x, top+16),    "NAME: " + str(Name),  font=font, fill=255)
draw.text((x, top+25),    "MESSAGE: " + str(Mess),  font=font, fill=255)

# Display image.
disp.image(image)
disp.display()
time.sleep(.1)