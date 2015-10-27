#Create by @CarmelitoA  11 Oct 2015 -Reading Grove Sensors.
#Temperature sensor,converted from Arduino equivallent code from
#https://github.com/Seeed-Studio/Grove_Temperature_Sensor
import mraa
import math
import time

temp = mraa.Aio(1) #Connected to A1
B=3975; #B value of the thermistor per the github repo above
while 1:
	tempSensorvalue= float (temp.read()) 
	#get the resistance of the sensor
	resistance= float((1023-tempSensorvalue)*10000/tempSensorvalue)
	#convert to temperature via datasheet
	temperature=1/(math.log(resistance/10000)/B+1/298.15)-273.15
	time.sleep(2)	
	print 'The current temperature is'
	print temperature

