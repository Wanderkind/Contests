

from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n,m=U()
    if (n%2)^(m%2):
        y=0
    else:
        y=1
    print(['Burenka','Tonya'][y])
