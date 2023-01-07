from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    n=int(input())
    a=[*U()]
    
    print(sum(i%2==1 for i in a))
    

for _ in range(int(input())):
        
    sol()
    #print()
