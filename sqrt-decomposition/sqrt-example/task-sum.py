import sys
sys.path.append("/home/matvey/Desktop/python/sqrt-decomposition/sqrt-class")
from implementation import SqrtDecomposition

cin = open("sum2.in", "r") 
cout = open("sum2.out", "w")

n = int(cin.readline())
a = [ int(i) for i in cin.readline().strip().split(" ") ]

m = int(cin.readline())

answer = SqrtDecomposition(a)
for i in range(m):
	l, r = [ int(i) for i in cin.readline().strip().split(" ") ] 
	cout.write("{}\n".format(answer.get(l-1, r-1)))


cin.close()