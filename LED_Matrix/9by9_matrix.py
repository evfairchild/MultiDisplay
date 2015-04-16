#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = EightByEight(address=0x70)
grid2 = EightByEight(address=0x71)

print "Press CTRL+Z to exit"
	
# Continually update the 8x8 display one pixel at a time
while(True):
  for x in range(0,9):
    for y in range(0,9):
      grid.setPixel(x, y)
      time.sleep(0.05)
  time.sleep(5)
  grid.clear()
