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

#determine the mode of the thermostat. 
def outside_comp():
    if main_globals.outside_t > main_globals.setpoint:
        main_globals.mode = 0 #hot outside/AC in use
    else:
        main_globals.mode = 1 #cold outside/Heat in use
        
#Increment or decrement the count of occupancy samples within the last two hours that user was home
def update_sum():
    if main_globals.occ == 1 and main_globals.occ_sum < 8:
        main_globals.occ_sum = main_globals.occ_sum + 1

    elif main_globals.occ == 0 and main_globals.occ_sum > 0:
        main_globals.occ_sum = main_globals.occ_sum - 1
    
    print(main_globals.occ_sum)

#Calculate the bound shift and apply it to the back-end setpoint    
def set_new():
    a = 0.5         #Recent occupancy weight
    b = 0.5         #Machine learning weight 
    outside_comp()
    update_sum()
    boundshift = ((4-0.5*main_globals.occ_sum)*a)+((4 - 4*main_globals.prob_present)*b) #cant go above 5
    main_globals.setpoint = main_globals.user_setpoint + boundshift*(-1)**main_globals.mode #-1^mode determines which direction the bound shift moves
    print("Setpoint = " + str(main_globals.setpoint))
