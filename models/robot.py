from models.algorithms import NaiveImplementation, OptimalImplementation

class Robot:
    
    def __init__(self, maps, start, end, approach="NaiveImplementation"):

        self.maps = maps
        self.start_x = start[0]
        self.end_x = end[0]
        self.start_y = start[1]
        self.end_y = end[1]
        cls_name = getattr(models.algorithms, approach)
        self.algorithms = cls_name(maps, self.end_x, self.end_y)

    def get_min_cost_path(self):
        value = self.algorithms.get_min_cost_path(self.start_x, self.start_y)
        return value[0], value[1]

