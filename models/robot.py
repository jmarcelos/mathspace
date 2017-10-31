from models.algorithms import NaiveImplementation, OptimalImplementation

factory_map = {
            "Naive": NaiveImplementation,
            "Optimal": OptimalImplementation}

class Robot:
   

    def __init__(self, maps, start, end, approach="Optimal"):

        self.maps = maps
        self.start_x = start[0]
        self.end_x = end[0]
        self.start_y = start[1]
        self.end_y = end[1]
        self.algorithms = factory_map[approach](maps, self.end_x, self.end_y)

    def get_min_path(self):
        value = self.algorithms.get_min_cost_path(self.start_x, self.start_y)
        return value[1]

