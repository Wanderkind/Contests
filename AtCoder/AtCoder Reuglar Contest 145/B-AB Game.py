from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

n,a,b=U()
n-=a-1
if n<0:
    exit(print(0))
if b>=a:
    exit(print(n))
p,q=divmod(n,a)
z=b*p
print(z+min(b,q))
