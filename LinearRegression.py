import numpy as np
import math

class LinearRegression:
    def __init__(self) -> None:
        self.m = 1
        self.b = 0
    
    def y_predict(self, x):
        return self.m * x + self.b
    
    def standard_fit(x, y):
        # diff between y and y_predict
        print(x, y)
    
    def experimental_fit(x, y):
        # diff between y_predict and line (shortest distance)
        print(x, y)
    
    def loss_standard(y, y_predicted):
        print(y, y_predicted)
    
    def loss_experimental(y, y_predicted):
        print(y, y_predicted)

