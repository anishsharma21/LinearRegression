import numpy as np
import math

class LinearRegression:
    def __init__(self) -> None:
        self.m = 1
        self.b = 0
        self.points = []
    
    def standard_fit(self):
        # minimising sum of square differences
        SSE = sum([self.error_squared(y, self.y_predict(x)) for x, y in self.points])
        return SSE
    
    def experimental_fit(x, y):
        # minimising perpendicular distance to line
        pass

    def error_squared(self, y, y_predicted):
        return (y - y_predicted) ** 2

    def y_predict(self, x):
        return self.m * x + self.b

    def x_y_to_points(self, x_vals, y_vals):
        self.points = [(x, y) for x in x_vals for y in y_vals]
        return self.points
