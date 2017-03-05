import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# PIN 19 will sense for button pushing
button = 19
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# The LED
led = 21
GPIO.setup(led, GPIO.OUT)

while True:
    input_state = GPIO.input(button) # Sense the button
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
        # Switch on LED
        GPIO.output(led,True)
    else:
        # Switch off LED
        GPIO.output(led,False)
GRIO.cleanup()
