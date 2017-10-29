from map import Map
from copy import deepcopy

#Assuming that there is only one least cost path, if there are more than one, the code is going to bring only one
# At first a simple recursive solution would solve the problem(was my first solution!!!), but the memory footprint would be big, for that reason i am saving the steps to reduce calculation effort

class Robot:
    
    def __init__(self, maps, start, end):

        self.maps = maps
        self.start_x = start[0]
        self.end_x = end[0]
        self.start_y = start[1]
        self.end_y = end[1]
        self.algorithms = NaiveImplementation(maps, self.end_x, self.end_y)

    def get_min_cost_path(self):

        path = []
        visited = []
        value = self.algorithms.find_least_cost_path(self.start_x, self.start_y, visited)
        return (value[0], list(reversed((value[1]))))

class NaiveImplementation:

    def __init__(self, maps, end_x, end_y):
        self.maps = maps
        self.end_x = end_x
        self.end_y = end_y

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
