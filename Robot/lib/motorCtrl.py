# This is where we keep all the controls for the motors. 
# We have a different function for each of the controls. 
# When Firebase datapoint is changed the corrisponding 
# function will be called for the robot to complete. 

import RPi.GPIO as GPIO
from time import sleep

class MotorControl:
    def __init__(self):             
        GPIO.setmode(GPIO.BOARD)

        self.Motor1A = 16
        self.Motor1B = 18
        self.Motor1E = 22

        self.Motor2A = 19
        self.Motor2B = 21
        self.Motor2E = 23
        
        GPIO.setup(self.Motor1A,GPIO.OUT)
        GPIO.setup(self.Motor1B,GPIO.OUT)
        GPIO.setup(self.Motor1E,GPIO.OUT)
    
        GPIO.setup(self.Motor2A,GPIO.OUT)
        GPIO.setup(self.Motor2B,GPIO.OUT)
        GPIO.setup(self.Motor2E,GPIO.OUT)

    #This is the function that tells the robot to move forward
    def Forward(self, driveFor):                
        print("Moving forward")
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        GPIO.output(self.Motor2A,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.HIGH)
        sleep(driveFor)
        self.Reset1()
        self.Reset2()
        
    #This is the function that tells the robot to move backward
    def Backward(self, driveFor):
        print("Moving Back")
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.HIGH)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        GPIO.output(self.Motor2A,GPIO.LOW)
        GPIO.output(self.Motor2B,GPIO.HIGH)
        GPIO.output(self.Motor2E,GPIO.HIGH)
        sleep(driveFor)
        self.Reset1()
        self.Reset2()

    #This is the function stops the right motors from moving
    def Reset1(self):
        print("Reset self.Motor 1")
        GPIO.output(self.Motor1E,GPIO.OUT)
    #This is the function stops the left motors from moving    
    def Reset2(self):
        print("Reset self.Motor 2")
        GPIO.output(self.Motor2E,GPIO.OUT)
    
    #This is the function that tells the robot to turn right
    def Right(self, driveFor):
        print("Moving right")
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.HIGH)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        GPIO.output(self.Motor2A,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.HIGH)
        sleep(driveFor)
        self.Reset1()
        self.Reset2()

    #This is the function that tells the robot to turn left
    def Left(self, driveFor):
        print("Moving left")
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        GPIO.output(self.Motor2A,GPIO.LOW)
        GPIO.output(self.Motor2B,GPIO.HIGH)
        GPIO.output(self.Motor2E,GPIO.HIGH)
        sleep(driveFor)
        self.Reset1()
        self.Reset2()


    def MotorCleanUp(self):
        GPIO.output(self.Motor1E,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.LOW)
        GPIO.cleanup()
