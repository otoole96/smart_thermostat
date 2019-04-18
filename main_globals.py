#---------------------------------------------------------------------------------------
#Program Name: main_globals.py
#Author: Zach O'Toole
#---------------------------------------------------------------------------------------
#Description:
#   Holds the globals variables shared by all of the modules.
#---------------------------------------------------------------------------------------


def init():
    # used by bounds and probability calc.
    global yprob
    yprob = []

    # used by bounds and controller
    global inside_t
    inside_t = 0

    # used by controller
    global outside_t
    outside_t = 30

    # used by the bounds and probability
    global occ
    occ = 0

    # used by the bounds
    global prob_present
    prob_present = 0.0

    # this is the calculated setpoint from the bounds file
    global setpoint
    setpoint = 70.0

    # used by the controller
    global heat
    heat = 0

    # used by the controller
    global fan
    fan = 0

    # used by the controller
    global ac
    ac = 0

    # used by the bounds
    global occ_sum
    occ_sum = 0

    # used by the bounds
    global mode
    mode = 0

    # setpoint from the user
    global user_setpoint
    user_setpoint = 70.0
