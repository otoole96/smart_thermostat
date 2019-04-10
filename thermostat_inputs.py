#---------------------------------------------------------------------------------------------------
# Thermostat IO
# Authors: Zach O'Toole, Qian Hao Lam
# Purpose: to get the inputs from the thermostat sensors and output stuff.
#---------------------------------------------------------------------------------------------------

import os
import glob
import time
import datetime
import main_globals
import subprocess
   
from urllib.request import urlopen
import json

#---------------------------------------------------------------------------------------------------
# Inside Temp.
#---------------------------------------------------------------------------------------------------

# Helper function for reading the temperature
def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

# Reads the temp from the sensor
def read_temp(device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0        
        return  temp_c, temp_f

# Main entry point for getting the inside temperature
def get_inside_temp():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    temp_c, temp_f = read_temp(device_file)
    print("Inside temp is " + str(temp_f))	
    main_globals.inside_t = temp_f

#---------------------------------------------------------------------------------------------------
# Outside Temp.
#---------------------------------------------------------------------------------------------------

# Queries the open weather api for the weather
def query_outside_temp ():
    apikey="ac918d16f3698465e610f6e08518cced"
    url="http://api.openweathermap.org/data/2.5/weather?zip=43201,us&appid=ac918d16f3698465e610f6e08518cced"
    meteo=urlopen(url).read()
    meteo = meteo.decode('utf-8')
    weather = json.loads(meteo)
    outsidetemp = 0
    for key, value in weather['main'].items():
        if key == "temp":
            outsidetemp = value        
    print(outsidetemp)
    return outsidetemp

# Main entry point for getting the outside temp
def get_outside_t ():
    outside_t = query_outside_temp()
    main_globals.outside_t = 9.0/5.0 * outside_t - 449.67
    print("Outside temp is = " + str(main_globals.outside_t))

#---------------------------------------------------------------------------------------------------
# Occupancy
#---------------------------------------------------------------------------------------------------

# Helper function for the occupancy
def ping_the_user():
    os.system("sudo arp-scan -l > scan.txt")
    mac_addr = "ac:37:43:4e:d3:78"
    if mac_addr in open('scan.txt').read():
        return 1
    else :
        return 0

# Main entry point for obtaining the occupancy
def get_occ():
    occ = ping_the_user()
    print("Occupancy is " + str(occ))
    main_globals.occ = occ
