import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
from math import *
#from itertools import *
#from random import *
#from functools import *


def sol():
    n = int(input())
    floor = int(log2(n))
    while n:
        a = floor + 1
        b = n - 2**floor + 1
        print(str(a) + str(b).zfill(18))
        floor -= 1
        n >>= 1

for _ in range(int(input())):
    sol()
