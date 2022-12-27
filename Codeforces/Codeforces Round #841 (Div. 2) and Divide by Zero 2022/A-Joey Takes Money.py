
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    
    n=int(input())
    a=sorted([*U()])
    
    ans=prod(a)+n-1
    
    print(2022*ans)
    
    
    
    
    
for _ in range(int(input())):
    sol()
    print()
