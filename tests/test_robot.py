import unittest
from models import Robot
from helper import get_map, get_2x2_map, get_3x3_map, get_5x5_map_up_down_right_left, get_5x5_map_up_down_right

class TestRobot(unittest.TestCase):

    def test_min_path_2x2_naive_implementation(self):
        expected_route = ['R', 'D']
        robot = Robot(get_2x2_map(), (0,0), (1,1), "Naive")
        answer = robot.get_min_path()
        self.assertEqual(answer, expected_route)

    def test_min_path_2x2_optimal_implementation(self):
        expected_route = ['R', 'D']
        robot = Robot(get_2x2_map(), (0,0), (1,1))
        answer = robot.get_min_path()
        self.assertEqual(answer, expected_route)

    def test_min_path_3x3_naive_implementation(self):
        expected_route = ['R', 'D', 'D', 'R']
        robot = Robot(get_3x3_map(), (0,0), (2,2), "Naive")
        answer = robot.get_min_path()
        self.assertEqual(answer, expected_route)

    def test_min_path_3x3_optimal_implementation(self):
        expected_route = ['R', 'D', 'D', 'R']
        robot = Robot(get_3x3_map(), (0,0), (2,2))
        answer = robot.get_min_path()
        self.assertEqual(answer, expected_route)

    def test_mint_path_example_naive_implementation(self):
        expected_route = ['R', 'R', 'D', 'D', 'R', 'D', 'D', 'R', 'R', 'D']
        robot = Robot(get_map(), (0,0), (5,5), "Naive")
        answer = robot.get_min_path()
        self.assertEqual(answer, expected_route)

    def test_min_path_example_optimal_implementation(self):
        expected_route = ['R', 'R', 'D', 'D', 'R', 'D', 'D', 'R', 'R', 'D']
        robot = Robot(get_map(), (0,0), (4,4))
        answer = robot.get_min_path()
        self.assertEqual(answer, expected_route)

    def test_min_cost_path_up_down_right_left_optimal_implementation(self):
        expected_route = ['D', 'R', 'R', 'U', 'R', 'R', 'D', 'D', 'L', 'D', 'D', 'R']
        robot = Robot(get_5x5_map_up_down_right_left(), (0,0), (4,4))
        answer = robot.get_min_path()
        self.assertEqual(answer, expected_route)

    def test_min_path_up_down_right_optimal_implementation(self):
        expected_route = ['D', 'D', 'R', 'R', 'U', 'U', 'R', 'R', 'D', 'D', 'D', 'D']
        robot = Robot(get_5x5_map_up_down_right(), (0,0), (4,4))
        answer = robot.get_min_path()
        self.assertEqual(answer, expected_route)

if __name__ == "__main__":
    unittest.main()
