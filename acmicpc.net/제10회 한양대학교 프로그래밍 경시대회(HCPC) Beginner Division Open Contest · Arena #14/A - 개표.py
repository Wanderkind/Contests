import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import
#from random import *
#from functools import *
#from collections import *



def sol():
    n = int(input())
    p, q = divmod(n, 5)
    for _ in range(p):
        print("++++", end = ' ')
    for _ in range(q):
        print("|", end = '')
    print()

for _ in range(int(input())):
    sol()
