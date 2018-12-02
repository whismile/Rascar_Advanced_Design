from TCS34725 import TCS34725_RGB
from time import sleep


class Colour_Detector(object):
    def __init__(self):
        # Inheritance from Library
        self.colour_detector = TCS34725_RGB.TCS34725()

        self.red_range = [[100, 255], [0, 155], [0, 155]]   # Range of Colours
        self.green_range = [[0, 155], [100, 255], [0, 155]]
        self.blue_range = [[0, 155], [0, 155], [100, 255]]
        self.yellow_range = [[100, 255], [100, 255], [0, 155]]

    # Comparing Conditions and Return Boolean
    def is_red(self):
        return self.get_red() > self.get_green() + 50 and self.get_red() > self.get_blue() + 50 \
               and self.red_range[0][0] <= self.get_red() <= self.red_range[0][1] \
               and self.red_range[1][0] <= self.get_green() <= self.red_range[1][1] \
               and self.red_range[2][0] <= self.get_blue() <= self.red_range[2][1]

    def is_yellow(self):
        return self.get_red() > self.get_blue() + 50 and self.get_green() > self.get_blue() + 50 \
               and self.yellow_range[0][0] <= self.get_red() <= self.yellow_range[0][1] \
               and self.yellow_range[1][0] <= self.get_green() <= self.yellow_range[1][1] \
               and self.yellow_range[2][0] <= self.get_blue() <= self.yellow_range[2][1]

    def is_green(self):
        return self.get_green() > self.get_blue() + 50 and self.get_green() > self.get_blue() + 50 \
               and self.green_range[0][0] <= self.get_red() <= self.green_range[0][1] \
               and self.green_range[1][0] <= self.get_green() <= self.green_range[1][1] \
               and self.green_range[2][0] <= self.get_blue() <= self.green_range[2][1]

    def is_blue(self):
        return self.get_blue() > self.get_red() + 50 and self.get_blue() > self.get_green() + 50 \
               and self.blue_range[0][0] <= self.get_red() <= self.blue_range[0][1] \
               and self.blue_range[1][0] <= self.get_green() <= self.blue_range[1][1] \
               and self.blue_range[2][0] <= self.get_blue() <= self.blue_range[2][1]

    # Mapping Sensing Values whit Range of (0, 1024) to (0, 254) And Return Integer value
    def get_red(self):
        return int((255 / 1024) * self.colour_detector.get_raw_data()[0])

    def get_green(self):
        return int((255 / 1024) * self.colour_detector.get_raw_data()[1])

    def get_blue(self):
        return int((255 / 1024) * self.colour_detector.get_raw_data()[2])

    def get_clear(self):
        return int((255 / 1024) * self.colour_detector.get_raw_data()[3])


if __name__ == "__main__":
    cd = Colour_Detector()

    try:
        while True:
            print("[", cd.get_red(), cd.get_green(), cd.get_blue(), "]")
            
            if cd.is_red():
                print('red')
            elif cd.is_blue():
                print('blue')
            elif cd.is_green():
                print('green')
            elif cd.is_yellow():
                print("yellow")
            else:
                print('None')

            sleep(1)
    except KeyboardInterrupt:
        exit()
