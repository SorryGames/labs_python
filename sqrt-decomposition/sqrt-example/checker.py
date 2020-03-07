import sys
import random
sys.path.append("/home/matvey/Desktop/python/sqrt-decomposition/sqrt-class")
from implementation import SqrtDecomposition


class Checker: 

    def __init__(self, test_count, n):
        self.test_count = test_count
        self.array = [0] * n
        self.test_array = SqrtDecomposition(self.array)

    def generate(self):
        for i in range(self.test_count):
            key = random.randint(1, 3)
            if key == 1:
                pass
            elif key == 2:
                pass
            elif key == 3:
                pass

    def get(self, l, r): 
        result = 0
        for i in range(l, r+1):
             result += self.array[i]
        self.test_array.get(l, r)
        return result

    def add(self, l, r, value):
        for i in range(l, r+1):
            self.array[i] += value
        self.test_array.add(l, r, value)

    def assign(self, l, r): 
        for i in range(l, r+1):
            self.array[i] += value
        self.test_array.add(l, r, value)

    def check (self):
        pass



checker = Checker(100, 5)
checker.generate()
