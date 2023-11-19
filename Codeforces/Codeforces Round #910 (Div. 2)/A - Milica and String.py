import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *

for _ in range(int(input())):
    n, k = U()
    s = input()
    a = s.count('A')
    b = s.count('B')
    if b == k:
        print(0)
    else:
        print(1)
        if b < k:
            i = 0
            cnt = 0
            while cnt < k - b:
                i += 1
                if s[i - 1] == 'A':
                    cnt += 1
            print(i, 'B')
        else:
            i = 0
            cnt = 0
            while cnt < b - k:
                i += 1
                if s[i - 1] == 'B':
                    cnt += 1
            print(i, 'A')
