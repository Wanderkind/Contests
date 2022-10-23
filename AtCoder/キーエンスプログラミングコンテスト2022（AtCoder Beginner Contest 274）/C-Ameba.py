
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

n=int(input())
l=[*U()]
d=[0 for _ in range(2*n+2)]

for i in range(n):
    k=d[l[i]]
    d[2*i+2]=k+1
    d[2*i+3]=k+1

for i in range(1,2*n+2):
    print(d[i])
