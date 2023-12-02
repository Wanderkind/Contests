import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import
#from random import *
#from functools import *
#from collections import *


m, d = U()
x, y, z = U()
a = x*m*d + (y - 1)*d + (z - 1)
b = a + 1
r = b % d
q = (b % (m*d))//d
p = b//(m*d)
print(p, q + 1, r + 1)
