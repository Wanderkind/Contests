

from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())



for _ in range(int(input())):
    m,s=U()
    b=[*U()] # len m
    
    S=sum(b) # 8
    k=2*(S+s) # 42
    i=isqrt(k) # 6
    
    if max(b)>i:
        print('no')
        continue
    
    print(['no','yes'][i*(i+1)==k])
    #print(f'i={i}')
