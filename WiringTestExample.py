# This is a program to learn how the GPIO pins of the Raspberry Pi works
# Wade Whitten

import RPi.GPIO as GPIO
import time

# Sets the reference pins as the physical pins, odd on left, even on right
GPIO.setmode(GPIO.BOARD)

# Enable the pin to be an out pin
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

for i in range(100):

    # Turn the pin on
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    GPIO.output(36, False)

    # Wait some time
    time.sleep(1)

    # Turn the pin off
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    GPIO.output(36, True)

    time.sleep(1)

# Maintenance work to prevent bugs later
GPIO.cleanup()
