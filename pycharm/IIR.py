import numpy as np
class IIR:
    def __init__(self, a, b):
        self.a = np.frombuffer(a)
        self.b = np.frombuffer(b)
        self.y = np.zeros([3])
        self.x = np.zeros([3])

    def filter(self,x):
        self.x[0] = self.x[1]
        self.x[1] = self.x[2]
        self.x[2] = x

        y = (self.b[0] * self.x[2] + self.b[1] * self.x[1] + self.b[2] * self.x[0]
                                   - self.a[1] * self.y[1] - self.a[2] * self.y[0])

        self.y[0] = self.y[1]
        self.y[1] = self.y[2]
        self.y[2] = y

        return y
