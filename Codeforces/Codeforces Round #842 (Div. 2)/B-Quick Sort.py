
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

def sol():
    n,k = U()
    p = [*U()] # len n
    d={}
    for i in range(n):
        d[p[i]]=i
    #o = p.index(1)
    w = d[1]
    #z = 1
    for z in range(2,n+1):
        #z+=1
        #print(z) ######
        if d[z]<w:
            z-=1
            break
        w=d[z]
    w=ceil((n-z)/k)
    print(w)
    

for _ in range(int(input())):
    sol()
    print()
