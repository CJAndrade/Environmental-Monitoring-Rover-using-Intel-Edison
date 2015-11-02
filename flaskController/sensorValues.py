#Create by @CarmelitoA  11 Oct 2015 -Reading Grove Sensors.
import mraa
import time
import math

def gasDensity():
	#Gas Sensor
	#https://github.com/Seeed-Studio/Grove_Gas_Sensor/blob/master/Gas_Sensor.ino
	gas = mraa.Aio(0) #Connected to A0
	gasSensorvalue= float (gas.read()) 
	vol = float(gasSensorvalue/1024)
	#print 'The gas density is '
	#print vol
	return vol

def temperature():
	#Temperature Sensor 
	#https://github.com/Seeed-Studio/Grove_Temperature_Sensor
	temp = mraa.Aio(1) #Connected to A1
	B=3975; #B value of the thermistor per the github repo above
	tempSensorvalue= float (temp.read()) 
	#get the resistance of the sensor
	resistance= float((1023-tempSensorvalue)*10000/tempSensorvalue)
	#convert to temperature via datasheet
	temperature=1/(math.log(resistance/10000)/B+1/298.15)-273.15	
	#print 'The current temperature is'
	#print temperature
	return temperature

def uvIndex():
	#UV sensor http://www.seeedstudio.com/wiki/Grove_-_UV_Sensor
	uv = mraa.Aio(2)
	sum =0
	for i in range(0,1024): 
		uvSensorvalue= float (uv.read()) 
		sum=long (uvSensorvalue+sum)
		time.sleep(0.002)
	sum = sum >> 10
	#print'The voltage value'
	#print sum*4980.0/1023.0
	#print 'mV'
	return sum*4980.0/1023.0



