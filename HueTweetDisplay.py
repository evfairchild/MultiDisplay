import time
import sys
import logging
from Adafruit_9x9 import NineByNine
import EAL_OLEDs
import Matrix16x8
from fonts import custom_font

M = Matrix16x8.Matrix16x8()  #address: 0x71 set in HT16K33.py
grid = NineByNine(address=0x70)
import neopix_hex

M.set_brightness(4)

def HueTweetDisplay(Tweet,color,tweet=False):
    if tweet==False:
        grid.setPixel(8,0)
        time.sleep(1)
        grid.clear()
        time.sleep(1)
    else:
        grid.setPixel(0,8)
        time.sleep(.1)
        grid.setPixel(0,1)
        time.sleep(.1)
        grid.setPixel(2,1)
        time.sleep(.1)
        grid.setPixel(3,1)
        time.sleep(.1)
        grid.setPixel(1,2)
        time.sleep(.1)
        grid.setPixel(1,3)
        time.sleep(.1)
        grid.setPixel(1,4)
        time.sleep(.1)
        
        EAL_OLEDs.OLEDanimate(0,"twitter_128x64.png","twitterflap_128x64.png")
        time.sleep(.2)
    
        grid.setPixel(2,5)
        time.sleep(.1)
        grid.setPixel(3,5)
        time.sleep(.1)
        grid.setPixel(3,4)
        time.sleep(.1)
        grid.setPixel(3,3)
        time.sleep(.1)
        
        M.scroll_message(Tweet,custom_font.textFont2)
    
        grid.setPixel(5,3)
        time.sleep(.1)
        grid.setPixel(5,4)
        time.sleep(.1)
        grid.setPixel(5,5)
        time.sleep(.1)
        grid.setPixel(6,5)
        time.sleep(.1)
                
        EAL_OLEDs.OLEDanimate(2,"Bulb_128x64.png","BulbOn_128x64.png")

        time.sleep(2)
        neopix_hex.colorChange(color)
        grid.clear()
        
        EAL_OLEDs.OLEDimage(1,"Zymbit.png")
        

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    try:
        logger = logging.getLogger(__name__)
        logger.info('Evans Light Show Subscribed!')
        if len(sys.argv) == 3:
            self.HueTweetDisplay(sys.argv[1],(sys.argv[2]))
        elif len(sys.argv) == 4:
            self.HueTweetDisplay(sys.argv[1],(sys.argv[2]),tweet=sys.argv[3])
        time.sleep(5)
        
    except ValueError:
        print("requires 2 or 3 args")  
        
    except Exception, exc:
        
        logger = logging.getLogger(__name__)
        logger.exception(exc)
        time.sleep(10)
    
    # while sys.argv[1] = False:
    #     grid.setPixel(8,0)
    #     time.sleep(1)
    #     grid.clear()
    #     time.sleep(1)
        
