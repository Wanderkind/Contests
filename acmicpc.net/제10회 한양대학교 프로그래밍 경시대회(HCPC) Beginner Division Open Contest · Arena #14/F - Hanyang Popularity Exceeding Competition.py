import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import
#from random import *
#from functools import *
#from collections import *


x = 0
for _ in range(int(input())):
    p, c = U()
    l = p - c
    r = p + c
    if l <= x <= r:
        x += 1

print(x)
