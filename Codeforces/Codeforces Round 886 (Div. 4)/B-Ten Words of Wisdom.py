
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    n = int(input())
    m = 0
    for i in range(n):
        a, b = U()
        if a <= 10:
            if b > m:
                m = b
                k = i + 1
    
    print(k)

for _ in range(int(input())):
    sol()
