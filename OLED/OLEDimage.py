
# OLEDimage.py

# Meant for use with the Raspberry Pi and an Adafruit monochrome OLED display!

# This program takes any image (recommended: landscape) and converts it into a black and white image which is then 
# displayed on one of Adafruit's monochrome OLED displays. 

# To run the code simply change directory to where it is saved and then type: sudo python OLEDimage.py <image name>
# For example: sudo python OLEDimage.py penguins900x600.jpg 
# The image penguins900x600.jpg is included in this repo as an example! Download any image that you want and simply change the
# image name!

# This program was created by The Raspberry Pi Guy

# Imports the necessary software - including PIL, an image processing library
import gaugette.ssd1306
import time
import sys
from PIL import Image

# Sets up our pins and creates variables for the size of the display. If using other size display you can easily change them.
def OLEDimage:
    RESET_PIN = 15
    DC_PIN    = 16
    width = 95
    height = 48

    led = gaugette.ssd1306.SSD1306(device=int(sys.argv[2]),reset_pin=RESET_PIN, dc_pin=DC_PIN)
    led.begin()
    led.clear_display()

    # This bit converts our image into black and white and resizes it for the display

    image = Image.open(sys.argv[1])
    image_rot = image.rotate(90)
    image_r = image_rot.resize((width,height), Image.BICUBIC)
    image_bw = image_r.convert("1")

    # Finally this bit maps each pixel (depending on whether it is black or white) to the display.
    # Note here we are not using the text command like in previous programs. We use led.draw_pixel:
    # That way we can individually address each pixel and tell it to be either on or off (on = white, off = black)

    for x in range(width):
            for y in range(height):
                    led.draw_pixel(x,y,bool(int(image_bw.getpixel((x,y)))))

    led.display()

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    OLEDimage(sys.argv[1],sys.argv[2])
