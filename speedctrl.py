import time
import RPi.GPIO as GPIO

leftStepPinForwardEnable=11
leftStepPinForward=16

rightStepPinForwardEnable=31
rightStepPinForward=35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftStepPinForwardEnable, GPIO.OUT)
GPIO.setup(leftStepPinForward, GPIO.OUT)
GPIO.setup(rightStepPinForwardEnable, GPIO.OUT)
GPIO.setup(rightStepPinForward, GPIO.OUT)
pwm = GPIO.PWM(leftStepPinForwardEnable, 100)
pwm.start(30)

GPIO.output(rightStepPinForward, GPIO.HIGH)
GPIO.output(leftStepPinForward, GPIO.LOW)
GPIO.output(rightStepPinForwardEnable, GPIO.HIGH)
time.sleep(2)
GPIO.output(leftStepPinForward, GPIO.HIGH)
GPIO.output(rightStepPinForward, GPIO.LOW)
GPIO.output(leftStepPinForwardEnable, GPIO.HIGH)
time.sleep(2)

pwm.stop()

GPIO.cleanup()
