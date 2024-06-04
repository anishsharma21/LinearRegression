import pandas as pd
from ErrorDirection import ErrorDirection
import numpy as np

class LinearRegression:
    def __init__(self) -> None:
        self.m = 1
        self.b = 0
        self.points = []
        self.learning_rate = 0.0001
        self.max_iterations = 1000

    def crude_fit(self):
       x = np.array([point[0] for point in self.points])
       y = np.array([point[1] for point in self.points])
       n = len(self.points)

       for i in range(self.max_iterations):
           y_predict = self.m * x + self.b
           error = y - y_predict

           b_gradient = (- 2 / n) * np.sum(error)
           m_gradient = (- 2 / n) * np.sum(x * error)

           self.b = self.b - self.learning_rate * b_gradient
           self.m = self.m - self.learning_rate * m_gradient

           new_error = np.sum((y - self.m * x - self.b) ** 2)

           if new_error < 0.0001:
               break

    def standard_fit(self):
        num_points = len(list(self.points))
        sum_of_y = sum([y for _, y in self.points])
        sum_of_x = sum([x for x, _ in self.points])
        sum_of_x_squared = sum([x**2 for x, _ in self.points])
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
