#! /usr/bin/python3

from gpiozero import CPUTemperature
from time import sleep
from fanshim import FanShim
from math import floor

cpu = CPUTemperature()
fanshim = FanShim()


def temp_to_rgb(value):
    
    output = 0
    if value > 35:
        output = floor((value-35)*(17/3))
    if value > 80:
        output = 255
        
    return output


def main():
    while True:
        temp = cpu.temperature
        TEMP_TO_RGB = temp_to_rgb(temp)
        fanshim.set_light(TEMP_TO_RGB, 0, 255-TEMP_TO_RGB)
        sleep(1)
        

if __name__ == '__main__':
    try:
        fanshim.set_fan(True)
        main()
    except KeyboardInterrupt:
        fanshim.set_light(0, 0, 255)

