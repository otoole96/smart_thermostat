#---------------------------------------------------------------------------------------
#Program Name: learning.py
#Author: Zach O'Toole
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
# Parses the time (string format) to an integer of minutes
# Input(s)  : string time
# Output(s) : int total_minutes
#---------------------------------------------------------------------------------------
def time_str_to_int(time):
    hours = 0
    # If-else handles the case where hours.length = 1, ex: time=' 1:11' 
    if time[0] == ' ':
        hours = int(time[1])
    else:
        hours = int(time[:2])

    minutes = int(time[-2:])
    return 60*hours + minutes

#---------------------------------------------------------------------------------------
# Determines the next time slot for the prediction algorithm
# Input(s)  : NONE
# Output(s) : the next time slot for prediction
#---------------------------------------------------------------------------------------
def get_next_time_index():
    t_struct = localtime()
    hours = t_struct[3]
    minutes = t_struct[4]
    total_minutes = hours * 60 + minutes
    return int(total_minutes + 15)
    
#---------------------------------------------------------------------------------------
# Loads and parses the occupancy history file to train the model.
# Stores the resulting features and targets into lists: time and taget.
# Input(s)  : NONE
# Output(s) : NONE
#---------------------------------------------------------------------------------------
def load_history():
    print("Loading history...")
    filename = "occupancy_history.csv"
    df = pd.read_csv(filename, index_col=0)
    present = np.array(df['Present'])
    
    # Gets the time, converts it into int value
    dates = df.index
    for date_time in dates:
        x = date_time[-5:]
        t = time_str_to_int(x)
        time.append(t)

    # Get the occ for each time, converting from boolean to 1/0 binary
    for val in present:
        if val:
            target.append(1)
        else:
            target.append(0)

    print("Done.")

def init():
    load_history()

#---------------------------------------------------------------------------------------
# Creates the SVM model to predict occupancy of the next time slot.
# Input(s)  : NONE
# Output(s) : NONE
#---------------------------------------------------------------------------------------
def get_probability_model():
    # convery lists to arrays
    t = np.array(time)
    y = np.array(target)
    
    # Creates the SVM model using the training data from the occ file
    support_vector_machine = svm.SVC(probability=True, kernel="rbf", verbose=1)
    
    t = t.reshape(-1, 1)
    
    # Train the SVM
    h = support_vector_machine.fit(t, y)

    # Find the next time t_current + 15
    t_test = np.array([get_next_time_index()])
    t_test = t_test.reshape(1, -1)

    # yhat = 1/0 hard classifier, yprob = Pr{Present} soft classifier 
    yhat = support_vector_machine.predict(t_test)
    yprob = support_vector_machine.predict_proba(t_test)
    
    return yprob

#---------------------------------------------------------------------------------------
# Adds an occupany data for the user for the current time slot.
# Input(s)  : NONE
# Output(s) : NONE
#---------------------------------------------------------------------------------------
def add_entry():
    m = localtime()[4]
    h = localtime()[3]

    m_str = str(m)
    h_str = str(h)
    # Open and append the occupant data
    with open("occupancy_history.csv", "a") as occ_file:
        # Makes sure to store time as a string of length 5, ie 01:01, instead of 1:1
        if len(str(m)) == 1:
            m_str = "0" + str(m)
        if len(str(h)) == 1:
            h_str = "0" + str(h)

        # Actually writes to the file
        if main_globals.occ == 1:
            occ_file.write("\n" + h_str + ":" + m_str + ",,,,TRUE")
        else:
            occ_file.write("\n" + h_str + ":" + m_str + ",,,,FALSE")            
    
#---------------------------------------------------------------------------------------
# Main entry point for the learning program.
# Calls the necessary functions for prediction and adding entries.
# Changes: file occupancy_data, global float yprob
#---------------------------------------------------------------------------------------
def probability_present():
    init()
    yprob = get_probability_model()[:,1]
    print(yprob)
    add_entry()
    main_globals.yprob = yprob
    
