from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())


T=int(input())
for _ in range(T):
    n=int(input())
    k=int(sqrt(2*(n-1)))
    w={}
    for i in range(n):
        w[i]=1
    for i in range(n,2*n):
        w[i]=0
    l=[]
    for i in range(n-1,-1,-1):
        t=k*k-i
        while w[t]==0:
            k-=1
            t=k*k-i
        l.append(t)
        w[t]=0
    print(*l[::-1],sep=' ')
