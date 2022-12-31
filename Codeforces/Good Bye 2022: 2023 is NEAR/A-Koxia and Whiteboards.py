
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

def sol():
    n,m=U()
    a=sorted([*U()])
    b=[*U()]
    #print(a,b) ########
    
    for i in range(m):
        k=b[i]
        if k>a[-1]:
            a.append(k)
            del a[0]
        else:
            l,r=0,n
            for _ in range(32):
                t=(l+r)//2
                if a[t]>k:
                    r=t
                else:
                    l=t
                #print(t) ##########
            
            while a[t]<k:
                t+=1
                    
            
            a.insert(t, k)
            if t>0: del a[0]
            else: del a[1]
        #print(a) #############   
    
    print(sum(a))
    
    
for _ in range(int(input())):
    sol()
    print()
