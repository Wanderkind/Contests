
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())
# from itertools import *

#def f(t): return (t - 1)*t//2

def sol():
    
    n, k = U()
    l = [*U()]
    
    s = []
    for i in range(k):
        z = []
        for j in range(i, n, k):
            z.append(l[j])
        s.append(z)
    #print(s)
    
    a = []
    for i in range(k):
        z = s[i]
        u = 0
        for j in z:
            if (j-1)%k != i:
                u += 1
        a.append(u)
    
    if not sum(a):
        print(0)
    elif sum(a) == 2 and a.count(1) == 2:
        print(1)
    else:
        print(-1)

for _ in range(int(input())):
    sol()
