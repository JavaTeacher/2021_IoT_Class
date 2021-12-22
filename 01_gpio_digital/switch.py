import RPi.GPIO as GPIO
import time

SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
