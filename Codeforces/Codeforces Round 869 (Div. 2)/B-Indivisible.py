
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())
# from itertools import *


def sol():
    n = int(input())
    
    if n == 1:
        print(1)
    elif n % 2 == 0:
        l = []
        for i in range(n//2):
            l += [i*2 + 2, i*2 + 1]
        print(*l, sep = ' ')
    else:
        print(-1)


for _ in range(int(input())):
    sol()
