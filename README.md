# Smart Thermostat README
Create a smart thermostat using a Raspberry Pi 3.

### Before you run
To run, python 3 must be installed on your pi. Then, you have to change the permissions on the setup file using:
```
chmod u+x setup
```
This file contains the dependencies for the application. 

  
Then, do
```
sudo ./setup
```
to install the dependencies.


### Running the program
Its very simple. Either change the main2.py file to an executable and run that, or simply run the following command:
```
sudo python3 main2.py
```
Note, you must be running on a raspberry pi with the correct pinout. Errors will arise if you try to run without an input temperature sensor, lack internet connection (for querying the weather API), or do not have the correct dependencies.
