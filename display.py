#!/usr/bin/env python
from time import *
import I2C_LCD_driver
from sys import argv

str_pad = " " * 16
my_long_string = str_pad + argv[1]

def message(firstLine, secondLine):
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_display_string(secondLine, 2)
    while True:
        for i in range (0, len(firstLine)):
            lcd_text = firstLine[i:(i+16)]
            mylcd.lcd_display_string(lcd_text,1)
            sleep(0.10)
            mylcd.lcd_display_string(str_pad,1)

message(my_long_string, argv[2])
