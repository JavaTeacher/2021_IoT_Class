import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)  # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN, GPIO.OUT)  # GPIO.OUT or GPIO.IN

for i in range(10):
    GPIO.output(LED_PIN, GPIO.HIGH)  # 1, True
    print("led on")
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)  # 0, False
    print("led off")
    time.sleep(1)

GPIO.cleanup()  # GPIO 핀 설정 초기화
