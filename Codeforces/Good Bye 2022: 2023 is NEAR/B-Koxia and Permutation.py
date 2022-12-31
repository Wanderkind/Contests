
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

'''
def P(a):
    for i in range(2, isqrt(a)+1):
        if a%i==0:
            return False
    return True
'''

def wow(n):
    if n%2:
        l=[];a=(n+1)//2;b=a-1
        for i in range(n//2):
            l+=[a,b]
            a += 1; b -= 1
        l.append(n)
    else:
        l=[];a=(n+1)//2;b=a+1
        for i in range(n//2):
            l+=[a,b]
            a -= 1; b += 1
        #l.append(n)
    #print(l)
    return l

def sol():
    
    n,k=U()
    
    if k==1:
        return [*range(1,n+1)]
    
    else:
        return wow(n)
            
    
for _ in range(int(input())):
    s=sol()
    print(*s, sep = ' ')
    print()
