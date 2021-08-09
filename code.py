# Triple Slider Color Mixer
import time
import board
import neopixel
import busio
from analogio import AnalogIn

# set up three sliding pots + the turn pot
red_value = AnalogIn(board.A1)
green_value = AnalogIn(board.A2)
blue_value = AnalogIn(board.A3)
potentiometer = AnalogIn(board.A0)

# needed for display
import adafruit_displayio_ssd1306
import displayio
import terminalio
import adafruit_mpr121
from adafruit_display_text import label

# set up displays:
# For display through I2C (STEMMA QT)
displayio.release_displays()
#oled_reset = board.D9
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
# Create I2C bus <- don't need this and don't need the extra verbose definition. Created board.I2C above.
#i2c = busio.I2C(board.SCL, board.SDA)
WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 0
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
# Set text, font, and color
text = " "
font = terminalio.FONT
color = 0xFFFFFF
# Create the text label
text_area = label.Label(font, text=text, color=color)
# Set the location
text_area.x = 0
text_area.y = 3
# Show it
display.show(text_area)
# to update text area after this with new text, just use a statement like this:
# text_area.text = "This is my new statement to display\nAnd this second line is amazing!"

def scale(value):
    """Scale an value from 0-65535 (AnalogIn range) to 0-255 (RGB range)"""
    return int(value / 65535 * 255)

def get_and_print_values():
    r = scale(red_value.value)
    g = scale(green_value.value)
    b = scale(blue_value.value)

    color = (r, g, b)
    # print(color)
    return color

BRIGHTNESS_SETTING = 0.1
PIXELS_IN_RING = 12
RING_PIN = board.D9
ring = neopixel.NeoPixel(RING_PIN, PIXELS_IN_RING, brightness=BRIGHTNESS_SETTING)

top_strip_pin = board.D5
top_strip_pixel_count = 6
top_strip = neopixel.NeoPixel(top_strip_pin, top_strip_pixel_count, brightness=BRIGHTNESS_SETTING)

bottom_strip_pin = board.D6
bottom_strip_pixel_count = 6
bottom_strip = neopixel.NeoPixel(bottom_strip_pin, bottom_strip_pixel_count, brightness=BRIGHTNESS_SETTING)

while True:
    color = get_and_print_values()
    top_strip.fill(color)
    bottom_strip[0] = color[0], 0, 0
    bottom_strip[1] = color[0], 0, 0
    bottom_strip[2] = 0, color[1], 0
    bottom_strip[3] = 0, color[1], 0
    bottom_strip[4] = 0, 0, color[2]
    bottom_strip[5] = 0, 0, color[2]
    #print("Potentiometer reads:",  potentiometer.value)
    #print((potentiometer.value,))
    print((color[0], color[1], color[2]))

    # max value of potentiometer is 65535

    pixels_to_light = PIXELS_IN_RING -1 - int(potentiometer.value / (65535/PIXELS_IN_RING))
    print(pixels_to_light)
    for i in range(0, PIXELS_IN_RING):
        if i <= pixels_to_light:
            ring[i] = color
        else:
            ring[i] = (0, 0, 0)

    print_string = "R:" + str(color[0]) + ", G:" + str(color[1]) + ", B:" + str(color[2]) + "\n"
    print_string = print_string + "Pot:" + str(potentiometer.value) + ", Lights:" + str(pixels_to_light)

    text_area.text = print_string
    #time.sleep(0.25)

