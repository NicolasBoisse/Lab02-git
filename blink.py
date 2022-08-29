#!/usr/bin/env python3
########################################################################
# Filename    : blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2022-02-02
########################################################################

import RPi.GPIO as GPIO         # import RPi.GPIO module 
import time                     # import time module 

def setup():
    GPIO.setmode(GPIO.BCM)       # choose BCM or BOARD
    GPIO.setup(10, GPIO.OUT)  	 # set a port/pin as an output
    GPIO.output(10, GPIO.LOW)    # set port/pin value to 0/GPIO.LOW/False 

def loop():
    while True:
        GPIO.output(10, GPIO.HIGH) 
        print ('led turned on >>>')     # print information on terminal
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(10, GPIO.LOW)  
        print ('led turned off <<<')
        time.sleep(1)                  

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

