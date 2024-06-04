import pandas as pd
from ErrorDirection import ErrorDirection

class LinearRegression:
    def __init__(self) -> None:
        self.m = 1
        self.b = 0
        self.points = []
        self.learning_rate = 0
        self.iterations = 0

    def crude_fit(self, learning_rate = 0.5): # doesn't work for negative gradients
        self.learning_rate = learning_rate
        # first we get the initial SSE with our initialised m and b variables
        initial_SSE = self.sum_of_squared_differences(self.m, self.b)
        # lets add a little bit to the learning_rate
        b_mod = self.b + learning_rate
        # now lets calculate the SSE with the new b value
        new_b_SSE = self.sum_of_squared_differences(self.m, b_mod)
        # now lets calculate the difference between the initial and new SSE
        diff = initial_SSE - new_b_SSE
        # for now, we will return whether the 

    def standard_fit(self):
        num_points = len(list(self.points))
        sum_of_y = sum([y for x, y in self.points])
        sum_of_x = sum([x for x, y in self.points])
        sum_of_x_squared = sum([x**2 for x, y in self.points])
        sum_of_product_of_x_and_y = sum([x*y for x, y in self.points])

        self.m = (num_points * sum_of_product_of_x_and_y - sum_of_x * sum_of_y) / (num_points * sum_of_x_squared - sum_of_x ** 2)
        self.b = (sum_of_y - self.m * sum_of_x) / num_points

    
    def experimental_fit(x, y):
        # minimising perpendicular distance to line
        pass

    def sum_of_squared_differences(self, m, b):
        return sum([self.error_squared(y, m * x + b) for x, y in self.points])
    
    def error_squared(self, y, y_predicted):
        return (y - y_predicted) ** 2

    def error_direction(self, previous_SSE, new_SSE):
        return ErrorDirection.ERROR_INCREASED if previous_SSE - new_SSE < 0 else ErrorDirection.ERROR_DECREASED

    def x_y_to_points(self, x_vals: pd.Series, y_vals: pd.Series):
        print(len(x_vals))
        print(len(y_vals))
        self.points = [(x_vals[i], y_vals[i]) for i in x_vals]
        return self.points
