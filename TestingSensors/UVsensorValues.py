#Create by @CarmelitoA  11 Oct 2015 -Reading Grove Sensors.
#Reading UV sensor, converted from Arduino equivallent code from
#http://www.seeedstudio.com/wiki/Grove_-_UV_Sensor
import mraa
import time

uv = mraa.Aio(2)
while 1:
	sum =0
	for i in range(0,1024): 
		uvSensorvalue= float (uv.read()) 
		sum=long (uvSensorvalue+sum)
		time.sleep(0.002)
	sum = sum >> 10
	print'The voltage value'
	print sum*4980.0/1023.0
	print 'mV'
	time.sleep(1)	

