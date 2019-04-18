#-------------------------------------------------------------------------
#Program Name: bang_bang.py
#Author: Thomas Krenelka, Zach O'Toole, Lam
#------------------------------------------------------------------------
#Description:
#   This the main routine that calls all other subroutines.
#   Main entry point for the application.

#-----------------------------------------------------------------------
import RPi.GPIO as GPIO 
import main_globals

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)     #heat
GPIO.setup(3, GPIO.OUT)     #ac
GPIO.setup(14, GPIO.OUT)     #fan


h = 0.5                     #hysteresis vale in f

def control():

    # Heat mode
    if main_globals.outside_t <= main_globals.setpoint:
        if main_globals.inside_t< (main_globals.setpoint - h):
            main_globals.heat = 1
            main_globals.ac = 0
            main_globals.fan = 1
        elif main_globals.inside_t>(main_globals.setpoint + h):
            main_globals.heat = 0
            main_globals.ac = 0
            main_globals.fan = 0

    # AC mode
    elif main_globals.outside_t > main_globals.setpoint:
        if main_globals.inside_t > (main_globals.setpoint + h):
            main_globals.heat = 0
            main_globals.ac = 1
            main_globals.fan = 1
        elif main_globals.inside_t < (main_globals.setpoint - h):
            main_globals.heat = 0
            main_globals.ac = 0
            main_globals.fan = 0

def set_pins():
    print("Setting pins...")

    if main_globals.heat == 1:
        GPIO.output(2,GPIO.HIGH)
        print("Setting heat..")
    else:
        GPIO.output(2,GPIO.LOW)
        print("Resetting heat")

    if main_globals.ac == 1:
        GPIO.output(3,GPIO.HIGH)
        print("Setting AC")
    else:
        GPIO.output(3,GPIO.LOW)
        print("Resetting AC")

    if main_globals.fan == 1:
        GPIO.output(14,GPIO.HIGH)
        print("Setting fan")
    else:
        GPIO.output(14,GPIO.LOW)
        print("Resetting fan")


def bang_bang():
    control()
    set_pins()

