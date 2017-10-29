from math import sqrt

class Map:

    MAX_COST = float('inf')

    def __init__(self, str_map):

        if not str_map or not isinstance(str_map, str):
            raise ValueError("A valid str map should be provided")

        paths = str_map.split()
        size_matrix = sqrt(len(paths)) 
        
        #assuming a square grid
        if round(size_matrix) != size_matrix:
            raise ValueError("Invalid map generation")

        self.grid = []
        line = []
        
        for index, path in enumerate(paths):
            if index != 0 and index % size_matrix == 0:
                self.grid.append(line)
                line = []
            line.append(int(path, 16))
        self.grid.append(line)
        self.start_x, self.start_y = 0, 0
        self.end_x, self.end_y = len(self.grid) - 1, len(self.grid) - 1

    def _split_line(line):
    
        line = []
        for val in line:
            line.append(int(val, 16))
        return line

    def get_position_value(self, position_x, position_y):

        if not self.is_inside_grid(position_x, position_y):
            return self.MAX_COST
        return self.grid[position_x][position_y]


    def is_inside_grid(self, position_x, position_y):

        if position_x < self.start_x or position_x > self.end_x:
            return False
        if position_y < self.start_y or position_y > self.end_y:
            return False
        return True