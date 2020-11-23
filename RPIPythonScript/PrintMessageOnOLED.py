# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import fcntl
import struct
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)
TEXT = ''

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
#i2c = board.I2C()
#oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d, reset=RESET_PIN)
# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# Create the SSD1306 OLED class.
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new('1', (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
font2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)

# Draw the text
intro = 'Hello!'
ip = 'PI is starting...'
draw.text((0, 0), intro, font=font, fill=255)
draw.text((0, 30), ip, font=font2, fill=255)

# Display image
oled.image(image)
oled.show()
