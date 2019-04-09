#--------------------------------------------------------------------------
#Program Name: bounds.py
#Author: Thomas Krenelka, Zach O'Toole, The Notorious L.A.M.
#--------------------------------------------------------------------------
#Description:
#   Establish a backend setpoint
#--------------------------------------------------------------------------
#Global Var Names:
#   inside_t
#   outside_t
#   occ
#   occ_hist
#   prob_present

import main_globals

def outside_comp(main_globals.outside_t,main_globals.inside_t):
    if main_globals.outside_t > main_globals.inside_t:
        main_globals.mode = 0 #hot outside/AC in use
    else:
        main_globals.mode = 1 #cold outside/Heat in use

def update_sum():
    if main_globals.occ == 1 and main_globals.occ_sum < 8:
        main_globals.occ_sum = main_globals.occ_sum - 1

    elif main_globals.occ == 0 and main_globals.occ_sum > 0:
        main_globals.occ_sum = main_globals.occ_sum - 1

def set_new():
    a = 0.5
    b = 0.5
    outside_comp()
    update_sum()
    boundshift = ((4-0.5*main_globals.occ_sum)*a)+((4 - 4*main_globals.prob_present)*b) #cant go above 5
    setpoint = main_globals.user_setpoint + boundshift*(-1)^mode

