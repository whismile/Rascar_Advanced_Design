import line_status as lineStat
from SEN040134 import SEN040134_Tracking as ts
import rear_wheels
import front_wheels


class Tracking(object):

    def __init__(self):
        # Set LineTracker =======================================
        self.line = ts.SEN040134_Tracking([16, 18, 22, 40, 32])
        # =======================================================

        # Set FrontWheel ========================================
        self.direction = front_wheels.Front_Wheels(db='config')
        self.direction.ready()
        # =======================================================

        # Set RearWheel =========================================
        self.drive = rear_wheels.Rear_Wheels(db='config')
        self.drive.ready()
        # =======================================================

        self.direction.turning_max = 35

        self.direction.turn_straight()

    def tracking(self):
        self.direction.turn_straight()

        currentStat = ""
        while True:
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
