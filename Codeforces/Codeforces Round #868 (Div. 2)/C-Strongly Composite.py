
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())
# from itertools import *

#def f(t): return (t - 1)*t//2


from collections import Counter as C
def fc(n):
    sq = isqrt(n)
    l=[]
    i=2
    while n>1:
        if i > sq:
            l.append(n)
            break
        if n%i:i+=1
        else:l.append(i);n//=i
    c=C(l)
    return [[i, c[i]] for i in c]


def sol():
    n = int(input())
    a = [*U()] # len n
    p = [fc(i) for i in a]
    
    ww = {}
    for i in p:
        for j in i:
            a, b = j
            if a not in ww:
                ww[a] = b
            else:
                ww[a] += b
    #print(ww)
    w = []
    for i in ww:
        w.append(ww[i])
    #print(w)
    
    ans = 0
    for i in range(len(w)):
        t = w[i]//2
        ans += t
        w[i] -= t*2
    print(ans + sum(w)//3)
    

for _ in range(int(input())):
    sol()
