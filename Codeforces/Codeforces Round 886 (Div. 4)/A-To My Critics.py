
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def f(a, b): return a + b >= 10

def sol():
    a, b, c = U()
    if f(a, b) or f(b, c) or f(c, a):
        print("YES")
    else: print("NO")

for _ in range(int(input())):
    sol()
