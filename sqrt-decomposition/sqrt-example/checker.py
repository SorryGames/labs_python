import sys
import random
sys.path.append("/home/matvey/Desktop/python/sqrt-decomposition/sqrt-class")
from implementation import SqrtDecomposition

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Checker: 

    def __init__(self, test_count, array_size):
        self.test_count = test_count
        self.array = [0] * array_size
        self.sqrt_array = SqrtDecomposition(self.array.copy())

    def generate(self):
        n = len(self.array)
        print(bcolors.WARNING
            + "Initialize array"
            + bcolors.ENDC
            + " ==> "
            + str(self.array))
        for i in range(self.test_count):
            key = random.randint(1, 3)
            value = random.randint(-10, 10)
            l, r = random.randint(0, n-1), random.randint(0, n-1) 
            
            if l > r:
                l, r = r, l

            if key == 1:
                self.assign(l, r, value)
                
                print(bcolors.WARNING 
                    + "Assign [{}, {}] a value of {}".format(l+1, r+1, value) 
                    + bcolors.ENDC 
                    + " ==> "
                    + str(self.array))
            
            elif key == 2:
                self.add(l, r, value)
                
                print(bcolors.WARNING 
                    + "Add [{}, {}] a value of {}".format(l+1, r+1, value) 
                    + bcolors.ENDC
                    + " ==> "
                    + str(self.array))
            
            elif key == 3:

                if self.check(l, r):
            
                    print(bcolors.OKGREEN 
                        + "Check [{}, {}] - OK".format(l+1, r+1) 
                        + bcolors.ENDC)
            
                else:
            
                    print(bcolors.FAIL 
                        + "Check [{}, {}] - FAIL!".format(l+1, r+1) 
                        + bcolors.ENDC)
            
                    break

        else: 
            print(bcolors.OKGREEN 
                + "All tests are passed!".format(l+1, r+1) 
                + bcolors.ENDC)

    def get(self, l, r): 
        result = 0
        for i in range(l, r+1):
             result += self.array[i]
        return result

    def add(self, l, r, value):
        for i in range(l, r+1):
            self.array[i] += value
        self.sqrt_array.add(l, r, value)

    def assign(self, l, r, value): 
        for i in range(l, r+1):
            self.array[i] = value
        self.sqrt_array.assign(l, r, value)

    def check (self, l, r):
        return self.get(l, r) == self.sqrt_array.get(l, r)


checker = Checker(test_count=100000, array_size=5)
checker.generate()

# checker.assign(2, 3, -10)
# checker.add(1, 3, 2)
# print(checker.array)
# print(checker.sqrt_array.array)
# print(checker.sqrt_array.sqrt_array)

# print(checker.sqrt_array.get(2, 2))
# print(checker.check(2, 2))