"""
Simple painting demo that draws on an Adafruit capacitive touch shield with
ILI9341 display and STMPE610 resistive touch driver
"""

import busio
import board
import digitalio
import adafruit_stmpe610
from adafruit_rgb_display import ili9341, color565

# Create library object using our Bus I2C & SPI port
i2c = busio.I2C(board.SCL, board.SDA)
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Adafruit Metro M0 + 2.8" Capacitive touch shield
cs_pin = digitalio.DigitalInOut(board.D9)
dc_pin = digitalio.DigitalInOut(board.D10)

# Initialize display
display = ili9341.ILI9341(spi, cs=cs_pin, dc=dc_pin)
# Fill with black!
display.fill(color565(0, 0, 0))

st_cs_pin = digitalio.DigitalInOut(board.D6)
st = adafruit_stmpe610.Adafruit_STMPE610_SPI(spi,st_cs_pin)

while True:
    if st.touched:
        ts = st.touches
        point = ts[0]   # the shield only supports one point!
        # perform transformation to get into display coordinate system!
        y = point['y']
        x = 4096 - point['x']
        x = 2 * x // 30
        y = 8 * y // 90
        display.fill_rectangle(x-2, y-2, 4, 4, color565(255, 255, 255))
