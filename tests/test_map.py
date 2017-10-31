import unittest
from models.map import Map
from test_helper import get_str_map, get_map, get_2x2_map

class TestMap(unittest.TestCase):
    
    def test_create_invalid_map(self):
        with self.assertRaises(ValueError) as context:
            maps = Map(1321321)
        
        self.assertTrue(context, "A valid str map should be provided")

    def test_create_string_map(self):
        with self.assertRaises(ValueError) as context:
            maps = Map("1312 1231 312312")
        
        self.assertTrue(context, "Invalid map generation")

    def test_create_valid_map(self):
        maps_size_x, maps_size_y = 6,6
        maps = Map(get_str_map())
        self.assertTrue(len(maps.grid), maps_size_x)
        self.assertTrue(len(maps.grid[0]), maps_size_y)

    def test_values_created_map(self):
        maps = Map("46B E59 EA C1F")
        expected_human_grid = [[1131, 3673], [234, 3103]]
        human_grid = maps.grid
        for expected_results, results in zip(expected_human_grid, human_grid):
            for result, expected_result in (results, expected_results):
                self.assertTrue(result, expected_result)

    def test_is_inside_grid(self):
        maps = get_map()
        self.assertTrue(maps.is_inside_grid(2,2))

    def test_is_not_inside_grid(self):
        maps = get_map()
        self.assertFalse(maps.is_inside_grid(2,-1))

    def test_valid_positio_valuen_in_map(self):
        maps = get_2x2_map()
        expected_result = 64 
        self.assertEqual(maps.get_position_value(1,1), expected_result)

    def test_invalid_positio_valuen_in_map(self):
        maps = get_2x2_map()
        expected_result = maps.MAX_COST
        self.assertEqual(maps.get_position_value(2,2), expected_result)

if __name__ == "__main__":
    unittest.main()
