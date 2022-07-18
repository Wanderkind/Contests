
from collections import*
from math import*
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n,m=U()
    a=[*U()]
    s=[1]*m
    A=[min(i,m+1-i)for i in a]
    C=Counter(A)
    for i in C:
        if m%2 and i==m//2+1:
            s[i-1]=0
        else:
            s[i-1]=0
            if C[i]!=1:
                s[m-i]=0
    print(''.join([chr(i+65)for i in s]))
