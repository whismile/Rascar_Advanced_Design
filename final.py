from car import Car
from batting_servo import Batting_Servo
import time

class myCar(object):
    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    def car_startup(self):
        pass

if __name__ == "__main__":
    try:
        myCar = myCar("KingOfBaseball")
        myCar.car_startup()

    except KeyboardInterrupt:
        myCar.drive_parking()
