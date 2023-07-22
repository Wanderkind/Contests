
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    
    n, k = U()
    l = sorted([*U()])
    d = [l[i+1]-l[i] for i in range(n-1)]
    #print(d) ######
    m = 0
    cnt = 0
    for i in range(n-1):
        if d[i] <= k:
            cnt += 1
        else:
            if cnt > m: m = cnt
            cnt = 0
    
        #print(d[i], k, cnt)
    if cnt > m : m = cnt
    print(n-1-m)
    
for _ in range(int(input())):
    sol()
