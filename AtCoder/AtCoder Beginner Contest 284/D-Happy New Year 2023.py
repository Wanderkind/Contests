from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


#from collections import Counter as C

def sol():
    n=int(input())
    z=1
    while 1:
        z+=1
        if n%z==0:
            break
    
    n//=z
    if n%z==0:
        p=z
        q=n//z
    else:
        q=z
        p=int(sqrt(n))
    
    print(p,q)

for _ in range(int(input())):
        
    sol()
    #print()
