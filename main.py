#-------------------------------------------------------------------------
#Program Name: main.py
#Author: Thomas Krenelka, Zach O'Toole
#------------------------------------------------------------------------
#Description:
#   This the main routine that calls all other subroutines.
#   Main entry point for the application.

#-----------------------------------------------------------------------

import bang_bang.py as bang_bang
import bounds.py as bounds
import thermostat_io.py as io
import learning as smart


# Main function of the project
def main():
    inside_t, humidity, user_setpoint, occ, outside_t = io.get_inputs()

    occ_hist = smart.load_history()

    prob_present = smart.probability_present(occ_hist)

    setpoint = bounds.determine_setpoint(occ, prob_present, user_setpoint)

    pid.set_relays(setpoint, inside_t)
    
    while True:
        bang_bang.bang_bang(setpoint,inside_t,outside_t)

    
if __name__ == "__main__ ":
    main()


