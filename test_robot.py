import unittest
from robot import Robot
from test_helper import get_map, get_2x2_map, get_3x3_map

class TestRobot(unittest.TestCase):

    def test_get_least_cost_step(self):
        cost_right = (10, "R")
        cost_left = (5, "L")
        cost_up = (float("inf"), "U")
        cost_down = (8, "D")
        expected_cost = 5, "L"
        robot = Robot(get_map(), (0,0), (6,6))
        least_cost = robot.get_least_cost_step(cost_right, cost_left, cost_up, cost_down)
        self.assertEqual(least_cost, expected_cost)


    def test_min_cost_path_1_step(self):
        expected_cost = 113
        expected_route = ["D", "R"]
        robot = Robot(get_2x2_map(), (0,0), (1,1))
        answer = robot.get_min_cost_path()
        self.assertEqual(answer, (expected_cost, expected_route))

    def test_min_cost_path_2_step(self):
        expected_cost = 0
        expected_route = ["R", "D", "D", "R"]
        robot = Robot(get_3x3_map(), (0,0), (2,2))
        answer = robot.get_min_cost_path()
        self.assertEqual(answer, (expected_cost, expected_route))

    #def test_min_cost_path_entrega(self):
    #    expected_cost = 6
    #    expected_route = ["U", "U", "U", "U"]
    #    robot = Robot(get_map(), (0,0), (5,5))
    #    answer = robot.get_min_cost_path()
    #    self.assertEqual(answer, (expected_cost, expected_route))

if __name__ == "__main__":
    unittest.main()
