#-------------------------------------------------------------------------
#Program Name: On and Off Controller
#Author: Thomas Krenelka, Zach O'Toole, Lam
#------------------------------------------------------------------------
#Description:
#   This the main routine that calls all other subroutines.
#   Main entry point for the application.

#-----------------------------------------------------------------------
import bounds.py as bound
import thermostat.io. as io
import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

if temp_c < (setpoint - 0.1) :
    GPIO.output(26,GPIO.HIGH) # Hot
    time.sleep(10)
else if temp_c < (setpoint +0.1) :
    GPIO.output(26,GPIO.LOW) # Hot off
    time.sleep(10)
else :
    GPIO.output(26,GPIO.LOW)
    time.sleep(10)
