import gaugette.ssd1306
import time
import sys
import RPi.GPIO as gpio
import logging

# Setting some variables for our reset pin etc.
RESET_PIN = 15
DC_PIN    = 16

CSx = 23
CSy = 24


def OLEDimage(dev,image,clear=True):
    from PIL import Image
    
    gpio.setmode(gpio.BCM)
    gpio.setup(CSx,gpio.OUT)
    gpio.setup(CSy,gpio.OUT)
    
    width = 72
    height = 32
    
    if dev == 0: #LEFT OLED
        gpio.output(CSx,gpio.LOW)
        gpio.output(CSy,gpio.HIGH)
    elif dev == 1: #MIDDLE OLED
        gpio.output(CSx,gpio.HIGH)
        gpio.output(CSy,gpio.LOW)
    elif dev ==2: #RIGHT OLED
        gpio.output(CSx,gpio.HIGH)
        gpio.output(CSy,gpio.HIGH)
        
    time.sleep(.05)
    
    oled = gaugette.ssd1306.SSD1306(device=1,reset_pin=RESET_PIN, dc_pin=DC_PIN)
    oled.begin()
    if clear:
        oled.clear_display()
    
    im = Image.open(image)
    im_r = im.resize((width,height), Image.BICUBIC)
    im_bw = im_r.convert("1")

    for x in range(width):
            for y in range(height):
                    oled.draw_pixel(x+33,y+4,bool(int(im_bw.getpixel((x,y)))))
                    
    oled.display()
    gpio.cleanup()

def OLEDtext(dev,text,size,clear=True):
    gpio.setmode(gpio.BCM)
    gpio.setup(CSx,gpio.OUT)
    gpio.setup(CSy,gpio.OUT)

    if dev == 0: #LEFT OLED
        gpio.output(CSx,gpio.LOW)
        gpio.output(CSy,gpio.HIGH)
    elif dev == 1: #MIDDLE OLED
        gpio.output(CSx,gpio.HIGH)
        gpio.output(CSy,gpio.LOW)
    elif dev ==2: #RIGHT OLED
        gpio.output(CSx,gpio.HIGH)
        gpio.output(CSy,gpio.HIGH)
        
    time.sleep(.05)
    
    oled = gaugette.ssd1306.SSD1306(device=1,reset_pin=RESET_PIN, dc_pin=DC_PIN)
    oled.begin()
    
    if clear:
        oled.clear_display()
        
    oled.draw_text2(33,15,text,size)
    oled.display()
    gpio.cleanup()

def OLEDanimate(dev, image1, image2, clear=True):
   ### animates two frames only ### 
    from PIL import Image
    
    gpio.setmode(gpio.BCM)
    gpio.setup(CSx,gpio.OUT)
    gpio.setup(CSy,gpio.OUT)
    
    width = 72
    height = 32
    
    if dev == 0: #LEFT OLED
        gpio.output(CSx,gpio.LOW)
        gpio.output(CSy,gpio.HIGH)
    elif dev == 1: #MIDDLE OLED
        gpio.output(CSx,gpio.HIGH)
        gpio.output(CSy,gpio.LOW)
    elif dev ==2: #RIGHT OLED
        gpio.output(CSx,gpio.HIGH)
        gpio.output(CSy,gpio.HIGH)
        
    time.sleep(.05)
    
    oled = gaugette.ssd1306.SSD1306(device=1,reset_pin=RESET_PIN, dc_pin=DC_PIN)
    oled.begin()
    if clear:
        oled.clear_display()
    
    im1 = Image.open(image1)
    im_r1 = im1.resize((width,height), Image.BICUBIC)
    im_bw1 = im_r1.convert("1")
    
    im2 = Image.open(image2)
    im_r2 = im2.resize((width,height), Image.BICUBIC)
    im_bw2 = im_r2.convert("1")

    for i in range (0,6):
        for x in range(width):
                for y in range(height):
                        oled.draw_pixel(x+15,y+4,bool(int(im_bw1.getpixel((x,y)))))
        oled.display()
        for x in range(width):
                for y in range(height):
                        oled.draw_pixel(x+15,y+4,bool(int(im_bw2.getpixel((x,y)))))
        oled.display()
        i += 1
                        
    gpio.cleanup()
    
def OLEDanimate2(dev,path,loops,clear=True):
   # ex path: /home/pi/fan/
   # files must be saved as n.xxx
      # where n is the frame number
      # example: fan_1.png, smile_4.bmp
   from PIL import Image
   import os
   
   gpio.setmode(gpio.BCM)
   gpio.setup(CSx,gpio.OUT)
   gpio.setup(CSy,gpio.OUT)
   
   width = 100
   height = 32
   
   if dev == 0: #LEFT OLED
       gpio.output(CSx,gpio.LOW)
       gpio.output(CSy,gpio.HIGH)
   elif dev == 1: #MIDDLE OLED
       gpio.output(CSx,gpio.HIGH)
       gpio.output(CSy,gpio.LOW)
   elif dev ==2: #RIGHT OLED
       gpio.output(CSx,gpio.HIGH)
       gpio.output(CSy,gpio.HIGH)
       
   time.sleep(.05)
   
   oled = gaugette.ssd1306.SSD1306(device=1,reset_pin=RESET_PIN, dc_pin=DC_PIN)
   oled.begin()
   
   if clear:
       oled.clear_display()
   
   files = os.listdir(path)
   files.sort()
   
   for j in range(0,loops):
      for i in range(0,len(files)):
         im = Image.open(path + files[i])
         im_r = im.resize((width,height), Image.BICUBIC)
         im_bw = im_r.convert("1")
         for x in range(width):
               for y in range(height):
                       oled.draw_pixel(x+15,y+4,bool(int(im_bw.getpixel((x,y)))))
         oled.display()
         time.sleep(.1)
          
   gpio.cleanup()
   
    
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    try:
        for dev in range(0,3):
            text = sys.argv[1]
            OLEDtext(dev,text,2,clear=True)
            time.sleep(2)
            print(dev)
            
    except ValueError:
        print("test requires text input")
            

