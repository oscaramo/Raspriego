import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)

n=0

while n<10:
    n=n+1
    time.sleep(5)
    GPIO.output(3,True)
    time.sleep(5)
    GPIO.output(3,False)
    
