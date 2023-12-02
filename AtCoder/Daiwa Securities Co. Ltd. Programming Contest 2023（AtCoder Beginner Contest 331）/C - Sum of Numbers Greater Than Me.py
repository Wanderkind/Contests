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
ab = [*U()]
a = sorted(ab)
L = []
s = 0
prev = 100000000

for i in range(n - 1, -1, -1):
    A = a[i]
    if A < prev:
        L.append(s)
    else:
        L.append(L[-1])
    prev = A
    s += A
l = L[::-1]

d = {}
for i in range(n):
    d[a[i]] = l[i]

for i in ab:
    print(d[i], end = ' ')
