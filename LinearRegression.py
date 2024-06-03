import pandas as pd
from ErrorDirection import ErrorDirection

class LinearRegression:
    def __init__(self) -> None:
        self.m = 1
        self.b = 0
        self.points = []
        self.learning_rate = 0
        self.iterations = 0

    def crude_fit(self, learning_rate = 0.5):
        self.learning_rate = learning_rate
        initial_SSE = self.sum_of_squared_differences(self.m, self.b)
        new_b = self.b + learning_rate
        mod_b_SSE = self.sum_of_squared_differences(self.m, new_b)
        b_error_direction = self.error_direction(initial_SSE, mod_b_SSE)
        final_b = self.find_b_crude(initial_SSE, b_error_direction)
        new_m = self.m + learning_rate
        mod_m_SSE = self.sum_of_squared_differences(new_m, self.b)
        m_error_direction = self.error_direction(initial_SSE, mod_m_SSE)
        final_m = self.find_m_crude(initial_SSE, m_error_direction)
        print(f"B-Value: {final_b}")
        print(f"M-value: {final_m}")
        print(f"Total iterations: {self.iterations}")

    def find_b_crude(self, current_SSE: float, error_direction: ErrorDirection):
        self.iterations += 1
        new_b = self.b + self.learning_rate * (-error_direction.value)
        mod_b_SSE = self.sum_of_squared_differences(self.m, new_b)
        b_error_direction = self.error_direction(current_SSE, mod_b_SSE)
        if b_error_direction == ErrorDirection.ERROR_INCREASED:
            return self.b
        else:
            self.b = new_b
            return self.find_b_crude(mod_b_SSE, error_direction)
    
    def find_m_crude(self, current_SSE: float, error_direction: ErrorDirection):
        self.iterations += 1
        new_m = self.m + self.learning_rate * (-error_direction.value)
        mod_m_SSE = self.sum_of_squared_differences(new_m, self.b)
        m_error_direction = self.error_direction(current_SSE, mod_m_SSE)
        if m_error_direction == ErrorDirection.ERROR_INCREASED:
            return self.m
        else:
            self.m = new_m
            return self.find_m_crude(mod_m_SSE, error_direction)


    def standard_fit(self):
        # minimising sum of square differences
        SSE = self.sum_of_squared_differences()
        return SSE
    
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
