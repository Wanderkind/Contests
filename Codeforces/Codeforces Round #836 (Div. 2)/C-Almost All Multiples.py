

from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    
    n,x=U()
    
    if n%x:
        print(-1)
    
    else:
        a=[i+1 for i in range(n)]
        a[0]=x
        a[n-1]=1
        k=n//x
        
        t=x
        
        while t<n:
            
            i=1
            while i<n:
                i+=1
                if k%i==0:
                    break
            
            a[t-1]=t*i
            t*=i
            k//=i
        
        print(*a, sep=' ')
            
            
    

for _ in range(int(input())):
    
    sol()
    print()
