#from itertools import combinations as C
#from itertools import permutations as P
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    n=int(input())
    a=sorted([*U()])
    
    if n==1:
        print(a[0])
    elif n==2:
        print(sum(a)/2)
    else:
        print(max(a[-2], sum(a)/n))

sol()
