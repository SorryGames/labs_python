import math


class SqrtDecomposition:

    def __init__(self, array):
        self.array = array
        self.sqrt_array = self.build(array)
        self.mark_array = [ (0, 0) for i in range(0, len(self.sqrt_array)) ]

    def build(self, array):
        n = len(array)
        m = int(math.sqrt(n))
        temp = []

        for i in range(0, n, m):
            temp.append(sum(array[i:i+m]))
        
        return temp

    def push(self, i):
        n = len(self.array)
        m = int(math.sqrt(n))
        
        self.array[i] = 
            




    def get(self, l, r):
        n = len(self.array)
        m = int(math.sqrt(n))
        result = 0

        l = max(l, 0)
        r = min(r, n-1)

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

    def define(self, l, r, value):
        n = len(self.array)
        m = int(math.sqrt(n))

        l = max(l, 0)
        r = min(r, n-1)

        while l % m and l <= r:
            self.sqrt_array[l // m] = value - self.array[l]
            self.array[l] = value
            l += 1

        while l + m <= r:
            self.sqrt_array[l // m] = value * m
            self.mark_array[l // m] = (1, value)
            l += m

        while l <= r:
            self.sqrt_array[l // m] = value - self.array[l]
            self.array[l] = value
            l += 1

    def add(self, l, r):
        n = len(self.array)
        m = int(math.sqrt(n))
        result = 0

        l = max(l, 0)
        r = min(r, n-1)

        while l % m and l <= r:
            self.sqrt_array[l // m] += value
            self.array[l] += value
            l += 1

        while l + m <= r:
            self.sqrt_array[l // m] += value
            self.mark_array[l // m] = (2, value)
            l += m

        while l <= r:
            result += self.array[l]
            l += 1

        return result