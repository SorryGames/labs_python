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

for i in range(0, n, m):
    localsum = sum(a[i:i+m])
    print("{} : [{}, {}]".format(localsum, i, i+m-1))