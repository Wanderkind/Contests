import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import
#from random import *
#from functools import *
#from collections import *


n = int(input())

for i in range(1, n + 1):
    for j in range(n):
        print(i, end = ' ')
    print()
