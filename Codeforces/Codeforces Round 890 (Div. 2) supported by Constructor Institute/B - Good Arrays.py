from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    n = int(input())
    a = [*U()]
    
    s = sum(a)
    if n == 1 or s - n < n//2 or s - n < a.count(1):
        print("NO")
    else:
        print("YES")
    
    

for _ in range(int(input())):
    sol()
