from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x):
    print(x); sys.stdout.flush()
#from itertools import *
#from random import *


n = int(input())
k = n*(n + 1) // 2
print(k)
print(k*k)
print(k*k)
