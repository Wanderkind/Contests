import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import
#from random import *
#from functools import *
#from collections import *


for _ in range(int(input())):
    s, t = input().split()
    try:
        w = s.index('x')
    except ValueError:
        w = s.index('X')
    q = t[w]
    if 97 <= ord(q) <= 122:
        print(chr(ord(q) - 32), end = '')
    else:
        print(q, end = '')
