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

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)     #heat
GPIO.setup(25,GPIO.OUT)     #ac
GPIO.setup(26,GPIO.OUT)     #fan


h = 0.5                     #hysteresis vale in f
heat = 0
ac = 0
fan = 0

def control(setpoint,inside_t,outside_t):
    # Heat mode
    if outside_t =< inside_t:
        if inside_t<(setpoint-h):
            heat = 1
            ac = 0
            fan = 0
        elif inside_t>(setpoint+h):
            heat = 0
            ac = 0
            fan = 0
    # AC mode
    elif outside_t > inside_t:
        if inside_t > (setpoint + h):
            heat = 0
            ac = 1
            fan = 1
        elif inside_t <(setpoint - h):
            heat = 0
            ac = 0
            fan = 0


def set_pins():
    if heat == 1:
        GPIO.output(24,GPIO.HIGH)
    else:
        GPIO.output(24,GPIO.LOW)

    if ac == 1:
        GPIO.output(25,GPIO.HIGH)
    else:
        GPIO.output(25,GPIO.LOW)

    if fan == 1:
        GPIO.output(26,GPIO.HIGH)
    else:
        GPIO.output(26,GPIO.LOW)



def bang_bang(setpoint,inside_t,outside_t):
    control(setpoint,inside_t,outside_t)
    set_pins()

