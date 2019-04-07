#--------------------------------------------------------------------------
#Program Name: pid_control.py
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


a = 0.5         #a + b must equal 1
b = 0.5
occ_sum = 0
bound_shift = 0  #do not make this more than 5 degrees ever

def outside_comp(outside_t,inside_t):
    if outside_t > inside_t:
        case = 0 #hot
    else:
        case = 1 #cold

def update_sum(occ):
    if occ == 1 and occ_sum < 8:
        occ_sum = occ_sum+1
    elif occ == 0 and occ_sum > 0:
        occ_sum = occ_sum - 1

def set_new(outside_t,inside_t,occ)
    outside_comp(outside_t,inside_t)
    update_sum(occ)
    boundshift = ((4-0.5*occ_sum)*a)+((4 - prob_present)*b)
    setpoint = user_setpoint + boundshift*(-1)^case



