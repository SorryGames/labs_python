import math


class SqrtDecomposition:

    def __init__(self, array):
        self.array = array
        self.sqrt_array = self.build(array)

    def build(self, array):
        n = len(array)
        m = int(math.sqrt(n))
        temp = []

        for i in range(0, n, m):
            temp.append(sum(array[i:i+m]))
        
        return temp

    def get(self, l, r):
        n = len(self.array)
        m = int(math.sqrt(n))
        result = 0

        while l % m and l <= r:
            result += self.array[l]
            l += 1

        while l + m <= r:
            result += self.sqrt_array[l // m]
            l += m

        while l <= r:
            result += self.array[l]
            l += 1

        return result