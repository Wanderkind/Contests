
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    n, k = U()
    br = [*U()]
    colors = list(set(br))
    
    w = {}
    for i in range(n):
        q = br[i]
        if q not in w:
            w[q] = [i]
        else:
            w[q].append(i)
    
    d = []
    for u in w:
        l = []
        aa = w[u]
        aa = [-1] + aa + [n]
        #print(aa)
        
        for i in range(1, len(aa)):
            l.append(aa[i] - aa[i-1]-1)
        m = max(l)
        l.remove(m)
        l.append(m//2)
        #print(l)
        d.append(max(l))
    
    print(min(d)) ###############
    

for _ in range(int(input())):
    sol()
