from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

T=int(input())
for _ in range(T):
    n,H,M=U()
    a=60*H+M
    l=[] #len n
    for _ in range(n):
        h,m=U()
        l.append((60*h+m-a)%1440)
    e=min(l)
    p,q=divmod(e,60)
    print(p,q)
