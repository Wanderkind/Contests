
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())
# from itertools import *

def f(t): return (t - 1)*t//2

def sol():
    #l = [*U()]
    n, k = U()
    #t = f(n)
    for i in range(1, n + 1):
        a, b = f(i), f(n - i)
        if a + b == k:
            print("YES")
            z = [1 for _ in range(i)] + [-1 for _ in range(n - i)]
            print(*z, sep = ' ')
            return;
    print("NO")

for _ in range(int(input())):
    sol()


# make sure lang is right
