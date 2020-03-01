import math

class SqrtDecomposition:

    def __init__(self, array, func=lambda a : sum(a)):
        self.array = array
        self.sqrt_array = self.build(array, func) 

    def build(self, array, func):
        n = len(array)
        m = int(math.sqrt(n))
        temp = []

        for i in range(0, n, m): 
            temp.append(func(array[i:i+m]))

        return temp


a = SqrtDecomposition([1, 2, 3, 4, 5])
print(a)
print(vars(a))