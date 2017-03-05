#import the GPIO and time package
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

red = 21
yellow = 16
green = 12


GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)


print "Starting"
# loop through 50 times, on/of for 1 second
for i in range(5):
    
    GPIO.output(red,True)
    time.sleep(1)
    GPIO.output(yellow,True)
    print "Red and Yellow on"
    time.sleep(1)

    GPIO.output(red,False)
    GPIO.output(yellow,False)
    print "Red and Yellow off -> Switch to green"
    GPIO.output(green,True)
    time.sleep(1)
    GPIO.output(green,False)
    GPIO.output(yellow,True)
    time.sleep(1)
    GPIO.output(yellow,False)
GPIO.cleanup()

