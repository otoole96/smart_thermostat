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
import time, sched
import main_globals
import threading
# Main function of the project
def main():
    # Initialization
    main_globals.init() # TODO: get the user set point through the UI
    probability_present()
    io.get_outside_t()
    flag_15 = 0
    flag_05 = 0
    print("Initialization complete. Entering main loop...")
    # Main Loop
    while True:
        current_minutes= time.localtime()[4]
        current_seconds = time.localtime()[5]
       

        if (current_seconds == 0 or current_seconds == 30) and flag_05 == 0:
                io.get_inside_temp()
                bang_bang.bang_bang()
                flag_05 = 1
                print(time.localtime())
        if current_seconds == 1 or current_seconds == 31:
                flag_05 = 0

        # Get the probability present, then setpoint in the next delta t (dt = 15m)
        if current_minutes % 15 == 0 and flag_15 == 0:
                io.get_outside_t()
                io.get_occ()
                probability_present()
                bounds.set_new()
                flag_15 = 1
        if current_minutes % 16 == 0:
                flag_15 = 0
                
        # UI Code (dt = 0)

#main()

print('Making threads.')

mainThread = threading.Thread(target=main)
mainThread.start()
mainThread.join()

print('Done')

