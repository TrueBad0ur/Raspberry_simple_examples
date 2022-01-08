import RPi.GPIO as GPIO
from time import sleep
from random import randint

def setColor(r, g, b):
        pwmR.ChangeDutyCycle(r)
        pwmG.ChangeDutyCycle(g)
        pwmB.ChangeDutyCycle(b)

def setup():
        global pwmR, pwmG, pwmB
        #GPIO.setup(i, GPIO.LOW)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(14, GPIO.OUT)

        pwmR = GPIO.PWM(14, 2000)
        pwmG = GPIO.PWM(18, 2000)
        pwmB = GPIO.PWM(15, 2000)

        pwmR.start(100)
        pwmG.start(100)
        pwmB.start(1)

        #for i in range(100):
        #       pwmR.ChangeDutyCycle(101-randint(1, 100))
        #       pwmG.ChangeDutyCycle(101-randint(1, 100))
        #       pwmB.ChangeDutyCycle(101-randint(1, 100))
        #       sleep(0.5)
        for n in range(10):
                for r in range(1, 101):
                        pwmR.ChangeDutyCycle(101-r)
                        pwmG.ChangeDutyCycle(100)
                        pwmB.ChangeDutyCycle(8)
                        sleep(0.05)
                #print('1')
                for r in range(100, 0, -1):
                        pwmR.ChangeDutyCycle(101-r)
                        pwmG.ChangeDutyCycle(100)
                        pwmB.ChangeDutyCycle(8)
                        sleep(0.05)

        sleep(10)

try:
        setup()
except KeyboardInterrupt:
        GPIO.cleanup()
