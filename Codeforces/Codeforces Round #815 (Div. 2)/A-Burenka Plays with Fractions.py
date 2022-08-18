

from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    a,b,c,d=U()
    p,q=a*d,b*c
    try:
        if p==q:
            y=0
        elif p%q==0 or q%p==0:
            y=1
        else:
            y=2
    except ZeroDivisionError:
        y=1
    print(y)
