from collections import deque
from copy import deepcopy
from models.map import Map

class OptimalImplementation:

    def __init__(self, maps, end_x, end_y):
        self.maps = maps
        self.end_x = end_x
        self.end_y = end_y
        self.total_cost = self._initialize_total_cost() 

    def _initialize_total_cost(self):
        total_cost = [[(float("inf"), []) for x in range(len(self.maps.grid))] for y in range(len(self.maps.grid))] 
        return total_cost

    def get_min_cost_path(self, start_x, start_y):

        value = self.find_least_cost_path(start_x, start_y)
        return (value[0], (value[1]))
        

    def find_least_cost_path(self, start_x, start_y):

        grid = self.maps.grid
        size = len(grid)
        
        queue = deque([(start_x,start_y)])

        self.total_cost[start_x][start_y] = (self.maps.get_position_value(start_x, start_y), [])

        while queue:

            actual_item = queue.popleft()
            actual_x, actual_y = actual_item 
            is_set = False
            for next_item in self.maps.get_neighbours(actual_x, actual_y):

                next_x, next_y = next_item[0] 
                direction = next_item[1] 
                new_total = self.total_cost[actual_x][actual_y][0] + self.maps.get_position_value(next_x, next_y)
                if self.total_cost[next_x][next_y][0] > new_total:
                    
                    path = self.total_cost[actual_x][actual_y][1]
                    if path and is_set:
                        path = path[:-1]
                    is_set = True
                    path.append(direction)
                    self.total_cost[next_x][next_y] = (new_total, path) 
                    queue.append((next_x, next_y))

        return self.total_cost[size-1][size-1] 

class NaiveImplementation:

    def __init__(self, maps, end_x, end_y):
        self.maps = maps
        self.end_x = end_x
        self.end_y = end_y
        
    def get_min_cost_path(self, start_x, start_y):

        path = []
        visited = []
        value = self.find_least_cost_path(start_x, start_y, visited)
        return (value[0], list(reversed((value[1]))))

    def find_least_cost_path(self, position_x, position_y, visited):

        if (position_x, position_y) in visited:
            return self.maps.MAX_COST, []

        if not self.maps.is_inside_grid(position_x, position_y):
            return self.maps.MAX_COST, []
    
        visited.append((position_x, position_y))
        if position_x == self.end_x and position_y == self.end_y:
            return self.maps.get_position_value(position_x, position_y), []

        cost_right, cost_left, cost_up, cost_down = (self.maps.MAX_COST, []),(self.maps.MAX_COST, []), (self.maps.MAX_COST, []),(self.maps.MAX_COST, [])
        cost_down = self.find_least_cost_path(position_x+1, position_y, deepcopy(visited))
        cost_down[1].append("D")
        #cost_left = self.find_least_cost_path(position_x-1, position_y, deepcopy(visited))
        #cost_left[1].append("L")
        cost_right = self.find_least_cost_path(position_x, position_y+1, deepcopy(visited))
        cost_right[1].append("R")
        #cost_up = self.find_least_cost_path(position_x, position_y-1, deepcopy(visited))
        #cost_up[1].append("U")
        
        min_cost = self.get_least_cost_step(cost_right, cost_left, cost_up, cost_down)
        actual_cost = self.maps.get_position_value(position_x, position_y)

        return min_cost[0] + actual_cost, min_cost[1]

    def get_least_cost_step(self, cost_right, cost_left, cost_up, cost_down):
        return min(cost_right, cost_left, cost_up, cost_down)
