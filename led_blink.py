#import the GPIO and time package
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 21

GPIO.setup(21, GPIO.OUT)
print "Starting"
# loop through 50 times, on/of for 1 second
for i in range(5):
    GPIO.output(led,True)
    print "LED on"
    time.sleep(1)
    GPIO.output(led,False)
    time.sleep(1)
GPIO.cleanup()

