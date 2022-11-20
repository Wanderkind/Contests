

from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    
    l,r,x=U()
    a,b=U() # l<=a,b<=r
    
    if a==b:return 0
    
    if x>r-l:return -1
    
    if abs(a-b)>=x:return 1
    
    # ab 차가 x보다 작은 경우만 따지면 됨
    
    al= a-l>=x
    ar= r-a>=x
    
    bl= b-l>=x
    br= r-b>=x
    
    if not (al or ar): return -1
    if not (bl or br): return -1
    
    '''
    if a>b:
        a*=-1
        b*=-1
        l*=-1
        r*=-1
    '''
    
    if al^ar and bl^br and al!=bl:return 3
    
    #if all([al,ar,bl,br]): return 1111111111
    if al==bl or ar==br: return 2
    
    
    
    

for _ in range(int(input())):
    
    print(sol())
    print()
