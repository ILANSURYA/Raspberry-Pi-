import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(3,GPIO.OUT) 
GPIO.setup(2,GPIO.IN) 
while True: 
 GPIO.output(3,GPIO.HIGH) 
 time.sleep(1) 
 GPIO.output(3,GPIO.LOW) 
 time.sleep(1) 
 if GPIO.input(2)==GPIO.HIGH: 
 print("pin 3 is on") 
 else: 
 print("pin 3 is off")
