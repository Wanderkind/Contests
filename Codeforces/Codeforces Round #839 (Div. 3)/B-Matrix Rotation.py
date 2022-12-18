

from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

def q(a, b, c, d):
    return (a<b and b<d and c<d and a<c)

def sol():
    a,b=U()
    c,d=U()
    
    print("yes" if (q(a, b, c, d)or q(c, a, d, b)or q(d, c, b, a)or q(b, d, a, c) )else "no")

for _ in range(int(input())):
    sol()
