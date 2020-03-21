import sys
import random
sys.path.append("/home/matvey/Desktop/python/sqrt-decomposition/sqrt-class")
from graphics import *
from implementation import SqrtDecomposition

class SpeedTest: 

    def __init__(self):
        pass

    def generate(self, array_length):
        self.array = [0] * array_length
        

    def fast_solve(self):
        pass

    def slow_solve(self):
        pass

    def results(self, array):
        win = GraphWin('Application', 1280, 800)
        win.getMouse()
        win.close()


test = SpeedTest()
test.results([])
