__author__ = 'youngsoul'

from Matrix16x8 import Matrix16x8
import time
from fonts import custom_font

m = Matrix16x8()

hours_colon = custom_font.hours
hours_no_colon = custom_font.hours_no_colon
font = custom_font.shapes


colon_on = True

while True:
    the_hour = time.strftime("%I", time.localtime()) #convert to PST
    the_min = time.strftime("%M")
    if the_hour.startswith("0"):
        the_hour = the_hour[1:]

    if colon_on:
        colon_on = False
        the_hour_data = hours_colon[the_hour]
    else:
        colon_on = True
        the_hour_data = hours_no_colon[the_hour]

#    the_min_data =  digits[the_min[0]]+digits[the_min[1]]
    #buffer = m.get_message_buffer("zymbit",font)
    m.display_16x8_buffer(font['half_off'] + font['Zymbit'] + font['half_off'])
    time.sleep(.5)
#    m.display_16x8_buffer(font['all_off']+font['all_off'])
    time.sleep(.5)



