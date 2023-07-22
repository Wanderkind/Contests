
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    
    n, C = U()
    s = [*U()]
    
    a = 4*n
    b = 4*sum(s)
    c = sum(i*i for i in s) - C
    
    print(round((-b + sqrt(b*b-4*a*c))/8/n))

for _ in range(int(input())):
    sol()
