

from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    
    n=int(input())
    if n%2:
        a=[1]*n
    
    elif n==2:
        a=[1,3]
    
    elif n%4==2:
        a=[1,3]+[2]*(n-2)
        
    
    else:
        k=n//2-1
        a=[1,3]*k+[2,2]
    
    print(*a,sep=' ')
    

for _ in range(int(input())):
    
    sol()
    print()
