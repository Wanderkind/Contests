

from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())


for _ in range(int(input())):
    n,m=U()
    if n==m==1:print(0);continue
    m,n=sorted([n,m])
    print(m*2+n-2)
