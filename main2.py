#!/usr/bin/python3
#-------------------------------------------------------------------------
#Program Name: main.py
#Author: Thomas Krenelka, Zach O'Toole, Qian Hao lam
#------------------------------------------------------------------------
#Description:
#   This the main routine that calls all other subroutines.
#   Main entry point for the application. This is the file to run upon 
#   starting the overall program.
#-----------------------------------------------------------------------

# Import user files and some necessary libraries
import bang_bang as bang_bang
import bounds as bounds
import thermostat_inputs as io
from learning import probability_present
import time
import main_globals
import threading
import disp

# This function used used by a thread to run the backend of the program
def backend():
    print("Backend running")
    probability_present()       # Init Probability
    io.get_outside_t()          # Init outside temperature
    bounds.set_new()            # Init the bounds around the setpoint
    # init flags used for timing control
    flag_15 = 0
    flag_05 = 0
    print("Initialization complete. Entering main backend loop on backend thread.")

    # Main Loop for the backend
    while True:
        # Get the current time for control
        current_minutes = time.localtime()[4]
        current_seconds = time.localtime()[5]
        # If statement executes every 30sec, flag used to make sure no repeats in a second
        if (current_seconds == 0 or current_seconds == 30) and flag_05 == 0:
                # Get the inside temp, set new bounds, control the relays
                io.get_inside_temp()
                bounds.set_new()
                bang_bang.bang_bang()
                flag_05 = 1
                print('INSIDE T, OUTSIDE T, USER SETPOINT, CALC SETPOINT' + str(main_globals.inside_t) + ',' +  str(main_globals.outside_t) + ',' + str(main_globals.user_setpoint) + ',' +  str(main_globals.setpoint) )
                #print(time.localtime())
        # Reset the flag the second after the previous executes
        if current_seconds == 1 or current_seconds == 31:
                flag_05 = 0
                
        # Get the probability present, then setpoint in the next delta t (dt = 15m)
        if current_minutes % 15 == 0 and flag_15 == 0:
                # Get the outside temp, occupancy and calculate the probability
                io.get_outside_t()
                io.get_occ()
                probability_present()
                bounds.set_new()
                flag_15 = 1
        # Reset the flag the minute after the previous executes
        if current_minutes % 16 == 0:
                flag_15 = 0

# UI Thread, continuously executes
def ui():
    print("Display running")
    disp.ui_main()

# Main function of the project
def main():
    # Initialization of global variables
    main_globals.init()

    print('Making threads.')
    mainThread = threading.Thread(target=backend)       # Make the thread to handle backend
    UIThread = threading.Thread(target=ui)              # Make the thread to handle the UI

    print('Starting threads.')
    mainThread.start()                    # Start the execution of the main thread
    UIThread.start()                      # Start the execution of the UI

    mainThread.join()
    UIThread.join()

main()
