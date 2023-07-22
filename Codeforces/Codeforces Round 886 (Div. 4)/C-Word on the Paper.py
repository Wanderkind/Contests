
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    l = ''
    for _ in range(8):
        a = input().replace('.', '')
        l += a
    
    print(l)
    
for _ in range(int(input())):
    sol()
