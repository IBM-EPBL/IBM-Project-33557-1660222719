#Enter Python code here and hit the Run button.
Import RPi.GPIO as GPIO 
From time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

While True: 
 GPIO.output(8, GPIO.HIGH) 
 Sleep(1) 
 GPIO.output(8, GPIO.LOW) 
 Sleep(2)
GPIO.output(8, GPIO.HIGH) 
 Sleep(1) 
GPIO.output(8, GPIO.LOW) 
Sleep(1)