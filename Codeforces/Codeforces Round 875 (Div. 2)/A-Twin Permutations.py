
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())
# from itertools import *


def sol():
    n = int(input())
    # n, k = U()
    a = [*U()]
    
    print(*[n+1-i for i in a], sep = ' ')

for _ in range(int(input())):
    sol()
