def pump_on():
import RPi.GPIO as GPIO  
from time import sleep
GPIO.setmode(GPIO.BCM)
pump_pin=26
watersensor_pin=18
GPIO.setup(watersensor_pin, GPIO.IN)
GPIO.setup(pump_pin, GPIO.OUT)   
 
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(18):
            print("no water detected")
            GPIO.output(pump_pin, GPIO.HIGH)
            sleep(5)
            GPIO.output(pump_pin, GPIO.LOW)
        else:
            print("water detected")
            # set port/pin value to 0/LOW/False  
        sleep(0.3)         # wait 0.1 seconds  
           
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
    
        

