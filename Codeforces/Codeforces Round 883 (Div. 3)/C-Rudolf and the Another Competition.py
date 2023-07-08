
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
from itertools import *
#from random import *


def sol():
    #a = [*U()]
    #n, k = U()
    #n = int(input())
    n, m, h = U()
    l = []
    for _ in range(n):
        u = sorted([*U()])
        uu = [*accumulate(u)]
        #print(u, uu) ###############
        v = [[0, 0]]
        for i in uu:
            if i > h:
                break
            else:
                v.append([len(v), v[-1][1]+i])
        l.append(v[-1])
    p, q = l[0]
    
    #print(p, q) #####################
    d = {}
    for i in l:
        a, b = i
        if a not in d:
            d[a] = [b]
        else:
            d[a].append(b)
    
    #print(d)
    a = 0
    for i in d:
        if i > p:
            a += len(d[i])
        if i == p:
            r = sorted(d[i])
            for u in range(len(r)):
                if r[u] == q:
                    a += u + 1
                    break
    
    print(a)

for _ in range(int(input())):
    sol()
