from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    n = int(input())
    a = [*U()]
    
    s = []
    for i in range(n-1):
        if a[i] > a[i+1]:
            s.append(a[i])
    
    print(max(s) if s else 0)

for _ in range(int(input())):
    sol()
