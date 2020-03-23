import sys
import random
from sqrt_structure import SqrtDecomposition

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

    def __init__(self, test_count, array_size, output=None):
        self.test_count = test_count
        self.array = [0] * array_size
        self.sqrt_array = SqrtDecomposition(self.array.copy())
        self.output = output
        if self.output is not None:
            self.cout = open(self.output, "w")
            self.clr_green = self.clr_gray = self.clr_red = self.clr_end = ''
        else:
            self.clr_green = bcolors.OKGREEN
            self.clr_gray = bcolors.WARNING
            self.clr_red = bcolors.FAIL
            self.clr_end = bcolors.ENDC

    def print(self, text):
        if self.output is None:
            print(text)
        else:
            text = text
            self.cout.write(text + "\n")

    def generate(self):
        n = len(self.array)
        self.print(self.clr_gray
            + "Initialize array"
            + self.clr_end
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
                self.print(self.clr_gray 
                    + "Assign [{}, {}] a value of {}".format(l+1, r+1, value) 
                    + self.clr_end 
                    + " ==> "
                    + str(self.array))
            elif key == 2:
                self.add(l, r, value)
                self.print(self.clr_gray 
                    + "Add [{}, {}] a value of {}".format(l+1, r+1, value) 
                    + self.clr_end
                    + " ==> "
                    + str(self.array))
            elif key == 3:
                if self.check(l, r):
                    self.print(self.clr_green 
                        + "Check [{}, {}] - OK".format(l+1, r+1) 
                        + self.clr_end)
                else:
                    self.print(self.clr_red 
                        + "Check [{}, {}] - FAIL!".format(l+1, r+1) 
                        + self.clr_end)
                    break
        else: 
            self.print(self.clr_green 
                + "All tests are passed!".format(l+1, r+1) 
                + self.clr_end)
        if self.output is not None:
            self.cout.close()

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