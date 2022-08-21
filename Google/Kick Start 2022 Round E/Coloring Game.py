
from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

def H(a):
    return sqrt(sum(i*i for i in a))

def prod(a):
    z=1
    for i in a:z*=i
    return z

def p(a,b):
    s=1
    for i in range(b):s*=a-i
    return s

def c(a,b):
    s=p(a,b)
    for i in range(b):s//=b-i
    return s

for h in range(int(input())):
    n=int(input())
    y=(n+4)//5
    print(f'Case #{h+1}: {y}')
