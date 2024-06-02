import pandas as pd

class LinearRegression:
    def __init__(self) -> None:
        self.m = 1
        self.b = 0
        self.points = []

    def crude_fit(self, learning_rate=0.01):
        num_points = (len(self.points))
        av_SSE = self.sum_of_squared_differences(self.m, self.b) / num_points
        print(av_SSE)
        prev_m = self.m
        prev_b = self.b
        self.m += learning_rate
        self.b += learning_rate
        new_m_av_SSE = self.sum_of_squared_differences(self.m, prev_b) / num_points
        new_b_av_SSE = self.sum_of_squared_differences(prev_m, self.b) / num_points
        print(new_b_av_SSE)
        print(new_m_av_SSE)
        b_direction = self.multiplier(av_SSE, new_b_av_SSE)
        m_direction = self.multiplier(av_SSE, new_m_av_SSE)
        print(b_direction, m_direction)
    
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

    def multiplier(self, original_SSE, new_SSE):
        return -1 if original_SSE - new_SSE < 0 else 1

    def x_y_to_points(self, x_vals: pd.Series, y_vals: pd.Series):
        print(len(x_vals))
        print(len(y_vals))
        self.points = [(x_vals[i], y_vals[i]) for i in x_vals]
        return self.points
