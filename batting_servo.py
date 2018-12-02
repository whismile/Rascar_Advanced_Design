from PCA9685 import Servo
from time import sleep

class Bat(object):
    channel = 1

    def __init__(self, bus_number=1):
        self.wheel = Servo.Servo(self.channel, bus_number=bus_number, offset=-12)
        self.wheel.setup()

    def batting(self, angle=150):
        self.wheel.write(angle)


if __name__ == "__main__":
    bat = Bat()
    bat.batting(180)
    sleep(1)
    bat.batting(-150)
    sleep(1)
