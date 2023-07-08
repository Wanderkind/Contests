
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    #a = [*U()]
    #n, k = U()
    n = int(input())
    i = 0
    for _ in range(n):
        a, b = U()
        if a > b: i += 1
    print(i)
    

for _ in range(int(input())):
    sol()
