#Create by @CarmelitoA  11 Oct 2015 -Reading Grove Sensors.
#Reading Gas sensor,converted from Arduino equivallent code from
#https://github.com/Seeed-Studio/Grove_Gas_Sensor/blob/master/Gas_Sensor.ino
import mraa
import time

gas = mraa.Aio(0) #Connected to A1

while 1:
	gasSensorvalue= float (gas.read()) 
	vol = float(gasSensorvalue/1024)
	print 'The gas density is '
	print vol
	time.sleep(1)

