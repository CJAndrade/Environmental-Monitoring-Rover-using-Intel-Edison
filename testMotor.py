#Create by @CarmelitoA  11 Oct 2015 - to test Motors on Mostor truck using the Intel Edison Arduino breakout and Sparkfun Motor Driver.
import mraa
import time

print (mraa.getVersion())
STBY = mraa.Gpio(10)
STBY.dir(mraa.DIR_OUT)

#Back motor ie motor A
PWMA = mraa.Pwm(3) # to control speed via PWM
PWMA.period_us(700)
PWMA.enable(True)
AIN1 = mraa.Gpio(9)
AIN1.dir(mraa.DIR_OUT)
AIN2 = mraa.Gpio(8)
AIN2.dir(mraa.DIR_OUT)

#front Motor ie motor B
PWMB = mraa.Pwm(5) # to control speed via PWM
PWMB.period_us(200)
PWMB.enable(True)
BIN1 = mraa.Gpio(11)
BIN1.dir(mraa.DIR_OUT)
BIN2 = mraa.Gpio(12)
BIN2.dir(mraa.DIR_OUT)

while True:
	STBY.write(1) #enable the standby of the motor driver
	time.sleep(0.5);
	print'motor Foward'
	#running the foward
	AIN1.write(1); 
	AIN2.write(0); 
	PWMA.write(0.5)
	time.sleep(1);
	#running the front motor - Left
	print'motor Left'
	BIN1.write(1); 
	BIN2.write(0); 
	PWMB.write(0.5)
	time.sleep(1);	
	#running the backward
	print'motor back'
	AIN1.write(0); 
	AIN2.write(1); 
	PWMA.write(0.5)
	time.sleep(1);
	print 'motor Right'
	#running the front motor - Right
	BIN1.write(0); 
	BIN2.write(1); 
	PWMB.write(0.5)
	time.sleep(1);	
	

