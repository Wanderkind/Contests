from math import factorial as f
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
m=998244353
n=int(input())
w=1
for i in range(n+2,2*n+1):
    w=((w%m)*i)%m
z=((2**n%m)*(w%m)%m)
print(z)
