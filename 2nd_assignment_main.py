#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        lineDetector = self.car.line_detector
        steering = self.car.steering
        accelerator = self.car.accelerator
        
        accelerator.go_forward(self.car.FASTEST)
        
        while lineDetector.is_in_line():
            status = lineDetector.read_digital()
            #if lineDetector.read_digital()[1] == 1:
            if status[2] == 1:
                steering.turn(90)
            
            elif status[1] == 1:
                steering.turn(80)
                
            #if lineDetector.read_digital()[3] == 1:
            elif status[3] == 1:
                steering.turn(100)
                
            #elif lineDetector.read_digital()[0] == 1:
            elif status[0] == 1:
                steering.turn(70)
        
            #elif lineDetector.read_digital()[4] == 1:
            elif status[4] == 1:
                steering.turn(110)
    
        accelerator.go_backward(30)
        time.sleep(0.3)
        accelerator.stop()
        
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()