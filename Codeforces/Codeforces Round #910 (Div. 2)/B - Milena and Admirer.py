import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *

for _ in range(int(input())):
    
    n = int(input())
    a = [*U()] # len = n
    #s = sum(a)
    
    i = n - 1
    cnt = 0
    while i >= 0:
        t = a[i]
        if i == n - 1 or t <= a[i + 1]:
            i -= 1
        else:
            p, q = divmod(t, a[i + 1])
            k = p + (1 if q else 0)
            #newl = [t//k]*(1 if k - t % k else 0) + [t//k + 1]*(1 if t % k else 0)
            a[i] = t//k  + (0 if k - t % k else 1)
            cnt += k - 1
            #print(a)
    print(cnt)
