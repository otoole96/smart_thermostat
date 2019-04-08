#-------------------------------------------------------------------------
#Program Name: learning.py
#Author: Zach O'Toole
#------------------------------------------------------------------------
#Description:
#   This file is responsible for handling all of the machine learning 
#   duties. This includes the following:
#   - loading data from a csv file
#   - creating a ML model from that data
#   - using that data to determine if the occupant will be present for
#     the next time interval
#-----------------------------------------------------------------------

#
## Imports go here
#
import math
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, preprocessing

time = []
target = []

def time_str_to_int(time):
    hours = 0
    if time[0] == ' ':
        hours = int(time[1])
    else:
        hours = int(time[:2])

    minutes = int(time[-2:])
    return 60*hours + minutes


# Load history takes in a file (.csv) and creates a data frame for each day
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

    # Get the occ for each time
    for val in present:
        if val:
            target.append(1)
        else:
            target.append(0)

    print("Done.")

def init():
    load_history()


def probability_present():
    t = np.array(time)
    y = np.array(target)
    
    logreg = linear_model.LogisticRegression(C=1e5, class_weight='balanced')

    t_train = t[:-96]
    y_train = y[:-96]

    t_train = t_train.reshape(-1, 1)

    logreg.fit(t_train, y_train)
#    logreg.fit(t.reshape(-1,1), y)

    t_test = t[-96:]
    y_test = y[-96:]
    
    t_test = t_test.reshape(-1,1)
    
    yhat = logreg.predict(t_test)
    yprob = logreg.predict_proba(t_test)
    print(yprob)
#    yhat = logreg.predict(t.reshape(-1,1))
    print(yhat)
    acc = np.mean(yhat == y_test)
#    acc = np.mean(yhat == y)
    print("Accuracy on training data = %f" % acc)

    plt.scatter(t_test,yprob[:,1])
    plt.xlim(0,1500)
    plt.ylim(-0.1,1.1)
    plt.grid()
    plt.show()
