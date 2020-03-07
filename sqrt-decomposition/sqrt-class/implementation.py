import math


class SqrtDecomposition:

    def __init__(self, array):
        self.array = array
        self.sqrt_array = self.build(array)
        self.mark_array = [ (2, 0) for i in range(0, len(self.sqrt_array)) ]

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
        
        multiplier = self.mark_array[i // m][0]
        addend = self.mark_array[i // m][1]

        if multiplier == 2:
            return
        
        l = (i // m) * m
        r = l + m - 1
        while (l <= r):
            self.array[l] = self.array[l] * multiplier + addend
            l += 1

        self.mark_array[i // m] = (2, 0)
        return

    def get(self, l, r):
        n = len(self.array)
        m = int(math.sqrt(n))
        result = 0

        l = max(l, 0)
        r = min(r, n-1)

        self.push(l)
        while l % m and l <= r:
            result += self.array[l]
            l += 1

        while l + m - 1 <= r:
            result += self.sqrt_array[l // m]
            l += m

        self.push(l)
        while l <= r:
            result += self.array[l]
            l += 1

        return result

    def assign(self, l, r, value):
        n = len(self.array)
        m = int(math.sqrt(n))

        l = max(l, 0)
        r = min(r, n-1)

        self.push(l)
        while l % m and l <= r:
            self.sqrt_array[l // m] = value - self.array[l]
            self.array[l] = value
            l += 1

        while l + m - 1 <= r:
            self.sqrt_array[l // m] = value * m
            self.mark_array[l // m] = (0, value)
            l += m

        self.push(l)
        while l <= r:
            self.sqrt_array[l // m] = value - self.array[l]
            self.array[l] = value
            l += 1

    def add(self, l, r, value):
        n = len(self.array)
        m = int(math.sqrt(n))
        result = 0

        l = max(l, 0)
        r = min(r, n-1)

        self.push(l)
        while l % m and l <= r:
            self.sqrt_array[l // m] += value
            self.array[l] += value
            l += 1

        while l + m - 1 <= r:
            self.sqrt_array[l // m] += value
            self.mark_array[l // m] = (1, value)
            l += m

        self.push(l)
        while l <= r:
            result += self.array[l]
            l += 1

        return result