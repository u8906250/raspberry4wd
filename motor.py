import time
import RPi.GPIO as GPIO

#mode=GPIO.getmode()
#print " mode ="+str(mode)
GPIO.cleanup()

leftStepPinForwardEnable=11
leftStepPinBackEnable=15
leftStepPinForward=16
leftStepPinBackward=18

rightStepPinForwardEnable=31
rightStepPinBackEnable=33
rightStepPinForward=35
rightStepPinBackward=37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftStepPinForwardEnable, GPIO.OUT)
GPIO.setup(leftStepPinBackEnable, GPIO.OUT)
GPIO.setup(leftStepPinForward, GPIO.OUT)
GPIO.setup(leftStepPinBackward, GPIO.OUT)
GPIO.output(leftStepPinForwardEnable, True)
GPIO.output(leftStepPinBackEnable, True)

GPIO.setup(rightStepPinForwardEnable, GPIO.OUT)
GPIO.setup(rightStepPinBackEnable, GPIO.OUT)
GPIO.setup(rightStepPinForward, GPIO.OUT)
GPIO.setup(rightStepPinBackward, GPIO.OUT)
GPIO.output(rightStepPinForwardEnable, True)
GPIO.output(rightStepPinBackEnable, True)

def right(x):
    GPIO.output(leftStepPinForward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(leftStepPinForward, GPIO.LOW)

def left(x):
    GPIO.output(rightStepPinForward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(rightStepPinForward, GPIO.LOW)

def forward(x):
    GPIO.output(leftStepPinForward, GPIO.HIGH)
    GPIO.output(rightStepPinForward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(leftStepPinForward, GPIO.LOW)
    GPIO.output(rightStepPinForward, GPIO.LOW)

def reverse(x):
    GPIO.output(leftStepPinBackward, GPIO.HIGH)
    GPIO.output(rightStepPinBackward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(leftStepPinBackward, GPIO.LOW)
    GPIO.output(rightStepPinBackward, GPIO.LOW)


def demo():
    forward(1)
    reverse(1)
    left(1)
    right(1)

demo()

GPIO.cleanup()
