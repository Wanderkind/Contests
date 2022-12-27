
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

m=10**9+7

def sol():
    
    n=int(input())
    ans=n*n*(n+1)-n*(n+1)*(2*n+1)//6
    
    print ((2022*ans)%m)
    
    
for _ in range(int(input())):
    sol()
    print()
