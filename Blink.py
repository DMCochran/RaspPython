#!/usr/bin/python

import RPi.GPIO as GPIO
import BMP085 as BMP
import time

pinNumber = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinNumber,GPIO.OUT)
GPIO.output(pinNumber,False)

sensor = BMP085.BMP085()

print('Temp = {0:0.2f} *C'.format(sensor.read_temperature())) # Temperature in Celcius
print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())) # The local pressure
print('Altitude = {0:0.2f} m'.format(sensor.read_altitude())) # The current altitude
print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())) # The sea-level pressure

for i in range(50):
    GPIO.output(pinNumber,True)
    time.sleep(1)
    GPIO.output(pinNumber,False)
    time.sleep(1)

GPIO.cleanup()
    