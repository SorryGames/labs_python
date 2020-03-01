import math

class SqrtDecomposition:

    def __init__(array):
        self.array = array
        self.sqrt_array = build(array) 

    def build(array):
        pass        

a = [1, 2, 3, 4, 5]


n = len(a)
m = int(math.sqrt(len(a)))

_sum = lambda a : sum(a)
_min = lambda a : min(a)

for i in range(0, n, m):
    result = _min(a[i:i+m])
    print("{} : [{}, {}]".format(result, i, min(i+m-1, n-1)))