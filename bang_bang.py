#-------------------------------------------------------------------------
#Program Name: bang_bang.py
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
import main_globals

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)     #heat
GPIO.setup(25,GPIO.OUT)     #ac
GPIO.setup(26,GPIO.OUT)     #fan


h = 0.5                     #hysteresis vale in f

def control()
    # Heat mode
    if main_globals.outside_t <= main_globals.inside_t:
        if main_globals.inside_t<(main_globals.setpoint-h):
            main_globals.heat = 1
            main_globals.ac = 0
            main_globals.fan = 1
        elif main_globals.inside_t>(main_globals.setpoint+h):
            main_globals.heat = 0
            main_globals.ac = 0
            main_globals.fan = 0
    # AC mode
    elif main_globals.outside_t > main_globals.inside_t:
        if main_globals.inside_t > (main_globals.setpoint + h):
            main_globals.heat = 0
            main_globals.ac = 1
            main_globals.fan = 1
        elif main_globals.inside_t <(main_globals.setpoint - h):
            main_globals.heat = 0
            main_globals.ac = 0
            main_globals.fan = 0

def set_pins()
    if main_globals.heat == 1:
        GPIO.output(24,GPIO.HIGH)
    else:
        GPIO.output(24,GPIO.LOW)

    if main_globals.ac == 1:
        GPIO.output(25,GPIO.HIGH)
    else:
        GPIO.output(25,GPIO.LOW)

    if main_globals.fan == 1:
        GPIO.output(26,GPIO.HIGH)
    else:
        GPIO.output(26,GPIO.LOW)



def bang_bang()
    control()
    set_pins()

