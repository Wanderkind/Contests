from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x):
    print(x); sys.stdout.flush()
#from itertools import *
#from random import *

n = int(input())
a = sorted(list(set([*U()])))
m = max(a)

n = len(a)
if len(a) == 1:
    print(0)
    exit()

p = []
for i in a:
    while 2*i < m:
        i <<= 1
    p.append(i)
p.sort()
q = [2*i for i in p]
p += q
#print(p)
m = 10**10
for i in range(n):
    d = p[i + n - 1] - p[i]
    if d < m: m = d
print(m)
