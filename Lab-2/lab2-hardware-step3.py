#!/usr/bin/python
import sys
import Adafruit_DHT

#Tutorial from https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
#The temperature sensor was tested by checking the temperature from a thermometer installed in my house and humidity/temperature was confirmed to work by boiling water and seeing if humidity rises to close to 100% and if the temperature increased as well

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
