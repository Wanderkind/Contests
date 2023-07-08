
from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#from itertools import *
#from random import *


def sol():
    #a = [*U()]
    #n, k = U()
    #n = int(input())
    l = [list(input()) for _ in range(3)]
    
    if l[0][0] == l[1][1] == l[2][2] and l[0][0] in "X+O":
        print(l[0][0])
        return 0
    if l[0][2] == l[1][1] == l[2][0] and l[0][2] in "X+O":
        print(l[0][2])
        return 0
    
    for i in range(3):
        if len(set(l[i])) == 1 and l[i][0] in "X+O":
            print(l[i][0])
            return 0
    
    ll = [[l[j][i] for j in range(3)] for i in range(3)]
    l = ll[:]
    for i in range(3):
        if len(set(l[i])) == 1 and l[i][0] in "X+O":
            print(l[i][0])
            return 0
    
    print("DRAW")

for _ in range(int(input())):
    sol()
