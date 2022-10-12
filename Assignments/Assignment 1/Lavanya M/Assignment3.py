#TRAFFIC LIGHT
import RPi.GPIO as GPIO
import time

GP.setmode(GP.BOARD)

GP1O.setup(7,GP1O.OUT)
GP1O.setup(11,GP1O.OUT)
GP1O.setup(13,GP1O.OUT)


while True:
    GPIO.output(7,True)
    sleep(2)
    GPIO.output(7,False)
    
    GPIO.output(11,True)
    sleep(1)
    GPIO.output(11,False)

    GPIO.output(13,True)
    sleep(3)
    GPIO.output(13,False)

GPIO.cleanup()
print("traffic light sequence done")


#BLINKING AN LED

Import RPi.GPIO as GPIO 
From time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

While True: 
 GPIO.output(5, GPIO.HIGH) 
 Sleep(2) 
 GPIO.output(5, GPIO.LOW) 
 Sleep(1)
 GPIO.output(5, GPIO.HIGH) 
 Sleep(2) 
 GPIO.output(5, GPIO.LOW) 
 Sleep(2)
