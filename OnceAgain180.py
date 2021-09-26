#!/usr/bin/python

import Adafruit_BMP.BMP085 as BMP085 # Imports the BMP library

# Create an 'object' containing the BMP180 data
sensor = BMP085.BMP085()

sensor.sealevel = 101000

def convertC(temp):
    return temp*(9/5)+32

print('Temp = {0:0.0f} *F'.format(convertC(sensor.read_temperature()))) # Temperature in Celcius
print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())) # The local pressure
print('Altitude = {0:0.2f} m'.format(sensor.read_altitude())) # The current altitude
print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())) # The sea-level pressure