


from itertools import*
from collections import*
from math import*
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n=int(input())
    c=[*U()]
    ans=[0]*n
    d={}
    for i in range(n):
        if c[i] not in d:
            d[c[i]]=[i]
        else:
            d[c[i]].append(i)
    for i in d:
        D=d[i]
        w=1
        for j in range(len(D)-1):
            w+=(D[j+1]-D[j])%2
        ans[i-1]=w
    print(*ans, sep=' ')
