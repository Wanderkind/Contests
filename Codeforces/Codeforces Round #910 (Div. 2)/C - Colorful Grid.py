import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *

for _ in range(int(input())):
    
    n, m, k = U()
    
    if k < n + m - 2:
        print("NO")
    
    elif (n + m - k) % 2:
        print("NO")
    
    else:
        print("YES")
        
        for j in range(m - 1):
            print("BR"[j % 2], end = ' ')
        print()
        for _ in range(n - 3):
            for j in range(m - 1):
                print("R", end = ' ')
            print()
        for _ in range(2):
            for j in range(m - 2):
                print("R", end = ' ')
            print("BR"[(n + m) % 2])
        
        for i in range(n - 2):
            for j in range(m - 1):
                print("B", end = ' ')
            print("RB"[(i + m) % 2])
        for j in range(m - 2):
            print("B", end = ' ')
        print(["R R", "B B"][(n + m) % 2])
