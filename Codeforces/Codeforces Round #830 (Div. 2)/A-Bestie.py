
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())
'''
def solve(n,a):
    
    cost=0
    G=gcd(*a)
    for h in range(n-1,-1,-1):
        if G==1:break
        i=h+1
        g=gcd(i,a[h])
        w=gcd(G,g)
        if w!=G:
            G=w
            cost+=n-h
        
    return cost
'''
def solvepsd(n,a,ex):
    
    cost=0
    G=gcd(*a)
    for h in range(n-1,-1,-1):
        if h!=ex:
            if G==1:break
            i=h+1
            g=gcd(i,a[h])
            w=gcd(G,g)
            if w!=G:
                G=w
                cost+=n-h
        
    return cost if G==1 else 10**9+1

for _ in range(int(input())):
    
    n=int(input())
    a=[*U()] #len n
    
    A=[solvepsd(n,a,i) for i in range(-1,n)]
    
    print(min(A))
