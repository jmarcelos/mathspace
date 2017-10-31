from models import Robot, Map
import sys

class MathSpaceRunner:

    def __init__(self, filename=None):

        available_grid = "46B E59 EA C1F 45E 63 899 FFF 926 7AD C4E FFF E2E 323 6D2 976 83F C96 9E9 A8B 9C1 461 F74 D05 EDD E94 5F4 D1D D03 DE3 89 925 CF9 CA0 F18 4D2"
        if filename:
            available_grid = self._read_file(filename)
        else:
            print("Supporting default grid: 46B E59 EA C1F 45E 63 899 FFF 926 7AD C4E FFF E2E 323 6D2 976 83F C96 9E9 A8B 9C1 461 F74 D05 EDD E94 5F4 D1D D03 DE3 89 925 CF9 CA0 F18 4D2")
        self.map = Map(available_grid)

    def execute(self):
        
        self.show_path_naive()
        self.show_path_optimal()
        self.show_path_up_righ_down_left()

    def show_path_naive(self):
               
        start = (0,0)
        end = (5,5)
        robot = Robot(self.map, start, end, "Naive")
        print(robot.maps)
        print("Naive (right down) path from file {}".format(robot.get_min_path()))

    def show_path_optimal(self):
               
        start = (0,0)
        end = (5,5)
        robot = Robot(self.map, start, end, "Optimal")
        print(robot.maps)
        print("Optimal path from file {}".format(robot.get_min_path()))


    def show_path_up_righ_down_left(self):
               
        maps = Map("1 20 1 1 1 1 1 1 20 1 20 20 20 1 1 20 20 20 1 20 20 20 20 1 1")
        start = (0,0)
        end = (4,4)
        robot = Robot(maps, start, end, "Optimal")
        print("Map with up down right left")
        print(robot.maps)
        print("Optimal path from file {}".format(robot.get_min_path()))

    def _read_file(self, filename):

        with open(filename, "r") as content:
            grid = content.read()
        return grid



if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        available_grid = sys.argv[1]
        print("Implementing map from file {0}".format(available_grid))
        default_runner = MathSpaceRunner(available_grid)
    else:
        default_runner = MathSpaceRunner()

    default_runner.execute()
