# Thermostat IO
# Purpose: to get the inputs from the thermostat sensors and output stuff.
#
#
#

import os
import glob
import time

from urllib.request import urlopen
import json



os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
size = 0
count = 0
10minute = 610
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        
        return  temp_c, temp_f

	
while True:
        
        temp_c = []
        temp_f = []
        size = size + 1
        temp_c_, temp_f_ = read_temp()
        temp_c.append(temp_c_)
        temp_f.append(temp_f_)
        count = count +1
	print(str(temp_c))	
	print(str(temp_f))	
	time.sleep(1)
	
if (count > 602) :
    count = 0
else if ( count > 599 ) :
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

