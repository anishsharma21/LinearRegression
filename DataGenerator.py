import numpy as np

class DataGenerator:
    def __init__(self, x_arr):
        self.x_arr = x_arr

    def generate_y(self):
        plus_or_negative = lambda: -1 if np.random.randint(0, 10) / 10 - 0.5 < 0 else 1
        m_base = plus_or_negative() * np.random.randint(100, 1000) / 100
        return np.array([(m_base * (self.x_arr[i] + self.x_arr[round(len(self.x_arr) / 2)] * plus_or_negative() * np.random.normal(loc=0, scale=abs(np.random.normal(loc=0.5, scale=0.1))))) for i in range(len(self.x_arr))]).reshape(-1, 1)