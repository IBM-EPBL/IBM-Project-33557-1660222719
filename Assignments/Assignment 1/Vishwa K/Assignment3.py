import RPi .GPIO as GP
import time
red = 8
yellow = 7
green = 13
GPIO.setmode(GP.BOARD)
GPIO.setup(red,GP.OUT)
GPIO.setup(yellow,GP.OUT)
GPIO.setup(green,GP.OUT)
while True:
 GP.output(red,true)
sleep(2)
GP.output(red,false)
    
GP.output(yellow,true)
sleep(2)
GP.output(yellow,false)

GP.output(green,true)
sleep(2)
GP.output(green,false)

GP.cleanup()
