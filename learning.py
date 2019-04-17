#---------------------------------------------------------------------------------------
#Program Name: learning.py
#Author: Zach O'Toole, Qian Hao Lam, Thomas Krenelka
#---------------------------------------------------------------------------------------
#Description:
#   This file is responsible for handling all of the machine learning 
#   duties. This includes the following:
#   - loading data from a csv file
#   - creating a ML model from that data
#   - using that data to determine if the occupant will be present for
#     the next time interval
#---------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------
# Imports go here
#---------------------------------------------------------------------------------------
import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import svm
from time import localtime
import main_globals

time = []
target = []

#---------------------------------------------------------------------------------------
# Helper function for loading history
#---------------------------------------------------------------------------------------
def time_str_to_int(time):
    hours = 0
    if time[0] == ' ':
        hours = int(time[1])
    else:
        hours = int(time[:2])

    minutes = int(time[-2:])
    return 60*hours + minutes

#---------------------------------------------------------------------------------------
# Determines the next time slot for the prediction
#---------------------------------------------------------------------------------------
def get_next_time_index():
    t_struct = localtime()
    hours = t_struct[3]
    minutes = t_struct[4]
    total_minutes = hours * 60 + minutes
    return int(math.floor(total_minutes/15) + 1)
    
#---------------------------------------------------------------------------------------
# Load history takes in a file (.csv) and creates a data frame for each day
#---------------------------------------------------------------------------------------
def load_history():
    print("Loading history...")
    #filename = "occupancy_history.csv"
    filename = "occupancy_history.csv"
    df = pd.read_csv(filename, index_col=0)
    present = np.array(df['Present'])
    
    # Gets the time, converts it into int value
    dates = df.index
    for date_time in dates:
        x = date_time[-5:]
        t = time_str_to_int(x)
        time.append(t)

    # Get the occ for each time
    for val in present:
        if val:
            target.append(1)
        else:
            target.append(0)

    print("Done.")

def init():
    load_history()

#---------------------------------------------------------------------------------------
# Creates the SVM and returns the vecto holding the probability data for the different
# time slots
#---------------------------------------------------------------------------------------
def get_probability_model():
    t = np.array(time)
    y = np.array(target)
    
    support_vector_machine = svm.SVC(probability=True, kernel="rbf", verbose=1)
    
    #    t_train = t[:-96]
    #    y_train = y[:-96]

    #    t_train = t_train.reshape(-1, 1)

    t = t.reshape(-1, 1)

    h = support_vector_machine.fit(t, y)

    t_test = np.array([get_next_time_index()])
    t_test = t_test.reshape(1, -1)

    yhat = support_vector_machine.predict(t_test)
    yprob = support_vector_machine.predict_proba(t_test)
    
    return yprob

def add_entry():
    m = localtime()[4]
    h = localtime()[3]

    with open("occupancy_history.csv", "a") as occ_file:
        if main_globals.occ == 1:
            occ_file.write("\n" + str(h) + ":" + str(m) + ",,,,TRUE")
        else:
            occ_file.write("\n" + str(h) + ":" + str(m) + ",,,,FALSE")            
    
#---------------------------------------------------------------------------------------
# Main entry point for the learning program.
# TODO: 
#       - Test addiing entries
#       - Run prediction on a single time (get_next_time_ind) 
#       - Train the model on all samples  
#---------------------------------------------------------------------------------------
def probability_present():
    init()
    yprob = get_probability_model()[:,1]
    print(yprob)
    add_entry()
    main_globals.yprob = yprob
    
