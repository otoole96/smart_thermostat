#-------------------------------------------------------------------------
#Program Name: main.py
#Author: Thomas Krenelka, Zach O'Toole
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

# Main function of the project
def main():
    # Initialization
    main_globals.init() # TODO: get the user set point through the UI
    s = sched.scheduler(time.time, time.sleep)

    # Main Loop
    while True:
        # Get inputs (dt = 60sec)
        s.enter(60, 10, io.get_inside_t)
        s.enter(60, 9, io.get_outside_t)
        s.enter(60*15, 8, io.get_occ)

        # Get the probability present, then setpoint in the next delta t (dt = 15m)
        s.enter(60*15, 3, probability_present)
        s.enter(60*15, 2, bounds.determine_setpoint)

        # Set the HVAC (dt = 1m)
        s.enter(60, 1, bang_bang.bang_bang)

        s.run()
        # UI Code (dt = 0)

if __name__ == "__main__ ":
    main()
