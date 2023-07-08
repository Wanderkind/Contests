
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    #a = [*U()]
    #n, k = U()
    #n = int(input())
    n, d, h = U()
    l = [*U()]
    
    u = []
    for i in range(n-1):
        u.append(min(l[i+1]-l[i], h))
    u.append(h)
    #print(u)
    
    f = lambda x: (h*h - (h - x)**2)*d/h/2
    print(sum(f(x) for x in u))

for _ in range(int(input())):
    sol()
