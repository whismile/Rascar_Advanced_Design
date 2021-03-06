#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):
    """ Initialize speed value"""
    #SPEED
    SLOWEST = 20
    SLOWER = 25
    SLOW = 35
    NORMAL = 45
    FAST = 65
    FASTER = 80
    FASTEST = 100
    
    # ANGLE
    LEFT_EDGE = 55
    LEFT = 75
    CENTER = 90
    RIGHT = 105
    RIGHT_EDGE = 125
    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        distance, before_distance = 0, 0
        self.car.accelerator.go_forward(myCar.NORMAL)
        line = self.car.line_detector.read_digital()
        count = 0
        
        while line != [1, 1, 1, 1, 1] or count < 2:
            #check obstacle & avoid obstacle
            distance = self.car.distance_detector.get_distance()
            line = self.car.line_detector.read_digital()
            print(line)
            
            if 0 <= distance < 30:
                if before_distance - distance > 10 or distance == -1:
                    continue
                
                else:
                    count += 1
                    #left diagonal handling
                    self.car.steering.turn(65)
                    self.car.accelerator.go_forward(myCar.NORMAL)
                    time.sleep(0.15)
                    
                    while self.car.line_detector.read_digital()[0] != 1:
                        continue
                    
                    # right diagonal handling
                    self.car.steering.turn(140)
                    self.car.accelerator.go_forward(myCar.SLOW)
                    time.sleep(0.15)
                    while self.car.line_detector.read_digital()[4] != 1:
                        continue
                    
                    # finish event
                    
            else:
                if line == [0, 0, 0, 0, 0]:
                    self.car.steering.turn(130)
                    self.car.accelerator.go_backward(myCar.FAST)
                    while self.car.line_detector.read_digital()[1] != 0:
                        continue
                    time.sleep(0.33)
                    
                elif line == [0, 0, 1, 0, 0]:
                    self.car.steering.turn(90)
                    
                elif line == [0, 1, 1, 0, 0]:
                    self.car.steering.turn(80)
                    
                elif line == [0, 1, 0, 0, 0]:
                    self.car.steering.turn(65)
                    
                elif line == [0, 0, 1, 1, 0]:
                    self.car.steering.turn(100)
                    
                elif line == [0, 0, 0, 1, 0]:
                    self.car.steering.turn(105)
                    
                elif line == [1, 1, 0, 0, 0]:
                    self.car.steering.turn(70)
                    
                elif line == [1, 0, 0, 0, 0]:
                    self.car.steering.turn(60)
                    
                elif line == [0, 0, 0, 1, 1]:
                    self.car.steering.turn(110)
                    
                elif line == [0, 0, 0, 0, 1]:
                    self.car.steering.turn(120)
                
                self.car.accelerator.go_forward(myCar.FAST)
            before_distance = distance
        self.car.accelerator.stop()
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
