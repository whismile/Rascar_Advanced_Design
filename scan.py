import time
import RPi.GPIO as GPIO
from SR02 import SR02_Supersonic as Supersonic_Sensor

buzzer_pin = 8
scale = [261.6, 293.6, 329.6, 349.2, 391.9, 440.0, 493.8, 523.2]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin, GPIO.OUT)

distanceDetector = Supersonic_Sensor.Supersonic_Sensor(35)
interval = 9

while distanceDetector.get_distance() <= interval:
    p = GPIO.PWM(buzzer_pin, 100)
    p.start(5)

try:
    p = GPIO.PWM(buzzer_pin, 100)
    p.start(5)

    for i in range(8):
        print(i + 1)
        p.ChangeFrequency(scale[i])
        time.sleep(0.5)

    p.stop()

finally:
    GPIO.cleanup()
