#-------------------------------------------------------------------------
#Program Name: main.py
#Author: Thomas Krenelka, Zach O'Toole, Qian Hao lam
#------------------------------------------------------------------------
#Description:
#   This the main routine that calls all other subroutines.
#   Main entry point for the application.
#-----------------------------------------------------------------------

import bang_bang as bang_bang
import bounds as bounds
import thermostat_inputs as io
from learning import probability_present
import time
import main_globals
import threading
import disp

def backend():
    print("Backend running")
    probability_present()
    io.get_outside_t()
    bounds.set_new()
    flag_15 = 0
    flag_05 = 0
    print("Initialization complete. Entering main backend loop on backend thread.")

    # Main Loop
    while True:

        current_minutes = time.localtime()[4]
        current_seconds = time.localtime()[5]
       
        if (current_seconds == 0 or current_seconds == 30) and flag_05 == 0:
                io.get_inside_temp()
                bounds.set_new()
                bang_bang.bang_bang()
                flag_05 = 1
                print('INSIDE T, OUTSIDE T, USER SETPOINT, CALC SETPOINT' + str(main_globals.inside_t) + ',' +  str(main_globals.outside_t) + ',' + str(main_globals.user_setpoint) + ',' +  str(main_globals.setpoint) )
                #print(time.localtime())
        if current_seconds == 1 or current_seconds == 31:
                flag_05 = 0
                
        # Get the probability present, then setpoint in the next delta t (dt = 15m)
        if current_minutes % 15 == 0 and flag_15 == 0:
                io.get_outside_t()
                io.get_occ()
                #probability_present()
                bounds.set_new()
                flag_15 = 1
        if current_minutes % 16 == 0:
                flag_15 = 0

# UI Code (dt = 0)
def ui():
    print("Display running")
    disp.ui_main()

# Main function of the project
def main():
    # Initialization
    main_globals.init()

    print('Making threads.')
    mainThread = threading.Thread(target=backend) 
    UIThread = threading.Thread(target=ui)

    print('Starting threads.')
    mainThread.start()
    UIThread.start()

    mainThread.join()
    UIThread.join()

main()
