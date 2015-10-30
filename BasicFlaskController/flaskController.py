#Create by @CarmelitoA  12 Oct 2015 -Basic Flask controller App.
#Using the Intel Edison Arduino Break out and 
#SparkFun Motor Driver https://www.sparkfun.com/products/9457
#Controller URL https://EdisonIPAddress:800
#Unless otherwise stated, this code is released under the CC BY 4.0
import mraa
import time
#importing flask 
from flask import Flask,request, redirect,render_template
#print (mraa.getVersion())
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
minSpeed = 0.3
maxSpeed = 0.9
speed = 0.3 #intal speed 


def moveFoward(speedBackMotor):
	STBY.write(1) #enable the standby of the motor driver
	BIN1.write(0) #change to 1 if motor runs opposite direction
	BIN2.write(1) #change to O if motor runs opposite direction
	PWMB.write(speedBackMotor)
	return;

def moveBackward(speedBackMotor):
	STBY.write(1) 
	BIN1.write(1) 
	BIN2.write(0) 
	PWMB.write(speedBackMotor)
	return;

def stopMoving():
	BIN1.write(0)#ReSeting the pins
	BIN2.write(0) 
	AIN1.write(0) 
	AIN2.write(0) 
	STBY.write(0) #disable the standby aka stop the motor driver
	return;

def turnFowardRight(speedBackMotor,speedFrontMotor):
	STBY.write(1) 
	BIN1.write(0)
	BIN2.write(1) 
	PWMB.write(speedBackMotor)
	AIN1.write(1) #Front motor of the truck
	AIN2.write(0) 
	PWMA.write(speedFrontMotor)
	return;


def turnFowardLeft(speedBackMotor,speedFrontMotor):
	STBY.write(1) 
	BIN1.write(0)
	BIN2.write(1) 
	PWMB.write(speedBackMotor)
	AIN1.write(0) 
	AIN2.write(1) 
	PWMA.write(speedFrontMotor)
	return;
def increaseSpeed():
	print("increase speed")
	global speed
	global maxSpeed
	global minSpeed
	if speed <= maxSpeed:
		speed = speed + 0.1 #increaseing speed by 10
		print 'speed +0.1'
	else:
		speed = maxSpeed
	return;

def decreaseSpeed():
	print("decrease speed")
	global speed
	global maxSpeed
	global minSpeed
	if speed <= minSpeed:
		speed = minSpeed
		print 'speed = minSpeed'
	else:
		speed = speed - 0.1
		print 'speed -0.1'
	return;

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/controlit', methods = ['POST'])
def signup():
    buttonHit = request.form['buttonPress']
    print("The button hit is '" + buttonHit + "'")
    if buttonHit == 'Fast':
        increaseSpeed()
    elif buttonHit == 'Slow':
        decreaseSpeed()
    elif buttonHit == 'Foward':
        moveFoward(speed)
        time.sleep(1);
        stopMoving()
	print ("Move Foward")
    elif buttonHit == 'Back':
        moveBackward(speed)
        time.sleep(1);
        stopMoving()
	print ("Move Back")
    elif buttonHit == 'Left':
        turnFowardLeft(speed,0.6)
        time.sleep(1);
        stopMoving()
	print ("Move Left")
    elif buttonHit == 'Right':
        turnFowardRight(speed,0.7)
        time.sleep(1);
        stopMoving()
	print ("Move Right")
    else :
        print("Do Nothing")
    
		
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=800 ,debug = True)



