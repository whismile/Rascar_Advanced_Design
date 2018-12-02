# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
# import ALL method in the SEN040134 Tracking Module
# =======================================================================
from SEN040134 import SEN040134_Tracking as ts

# =======================================================================
# import ALL method in the SR02 Ultrasonic Module
# =======================================================================
from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor

# =======================================================================
# import ALL method in the rear/front Motor Module
# =======================================================================
import rear_wheels
import front_wheels

# =======================================================================
# import LineTracer's Status List
# ======================================================================
import line_status as lineStat

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)


class Car(object):

    def __init__(self):
        self.moduleInitialize()

    def drive_parking(self):
        # front wheels center alignment
        self.direction.turn_straight()

        # power down both wheels
        self.drive.stop()
        self.drive.power_down()

    def assignment_main(self):
        self.direction.turn_straight()

        while True:
            currentStat = ""
            for x in self.line.read_digital():
                currentStat += str(x)

            if currentStat == lineStat.leftDegree_35:
                self.drive.forward_with_speed(80)
                self.direction.turn_left()
            elif currentStat == lineStat.leftDegree_30:
                self.drive.forward_with_speed(80)
                self.direction.turn_left(5)
            elif currentStat == lineStat.leftDegree_10:
                self.drive.forward_with_speed(80)
                self.direction.turn_left(20)
            elif currentStat == lineStat.leftDegree_5:
                self.drive.forward_with_speed(80)
                self.direction.turn_left(30)

            elif currentStat == lineStat.rightDegree_35:
                self.drive.forward_with_speed(80)
                self.direction.turn_right()
            elif currentStat == lineStat.rightDegree_30:
                self.drive.forward_with_speed(80)
                self.direction.turn_right(-5)
            elif currentStat == lineStat.rightDegree_10:
                self.drive.forward_with_speed(80)
                self.direction.turn_right(-25)
            elif currentStat == lineStat.rightDegree_5:
                self.drive.forward_with_speed(80)
                self.direction.turn_right(-30)

            elif currentStat == lineStat.back:
                self.direction.turn_right(-5)
                self.drive.backward_with_speed(100)
            elif currentStat == lineStat.stop:
                self.drive.stop()
                break
            else:
                self.drive.forward_with_speed(80)

                self.direction.turn_straight()

                if self.distance.get_distance() < 30:
                    # Sensing And Action
                    pass

    def moduleInitialize(self):
        try:
            # ================================================================
            # ULTRASONIC MODULE DRIVER INITIALIZE
            # ================================================================
            self.distance = Ultrasonic_Sensor.Ultrasonic_Avoidance(35)

            # ================================================================
            # TRACKING MODULE DRIVER INITIALIZE
            # ================================================================
            self.line= ts.SEN040134_Tracking([16, 18, 22, 40, 32])

            # ================================================================
            # FRONT WHEEL DRIVER SETUP
            # ================================================================
            self.direction = front_wheels.Front_Wheels(db='config')
            self.direction.ready()

            # ================================================================
            # REAR WHEEL DRIVER SETUP
            # ================================================================
            self.drive = rear_wheels.Rear_Wheels(db='config')
            self.drive.ready()

            # ================================================================
            # SET LIMIT OF TURNING DEGREE
            # ===============================================================
            self.direction.turning_max = 35

            # ================================================================
            # SET FRONT WHEEL CENTOR ALLIGNMENT
            # ================================================================
            self.direction.turn_straight()

        except:
            print("MODULE INITIALIZE ERROR")
            print("CONTACT TO Kookmin Univ. Teaching Assistant")


if __name__ == "__main__":
    try:
        car = Car()
        car.assignment_main()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        car.drive_parking()
