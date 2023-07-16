
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    n, m, k = U()
    xx, yy = U()
    
    l = []
    for _ in range(k):
        l.append([*U()])
    
    for i in l:
        x, y = i
        if (x-xx + y-yy) % 2 == 0:
            print("no")
            return 0
    
    print("yes")
for _ in range(int(input())):
    sol()
