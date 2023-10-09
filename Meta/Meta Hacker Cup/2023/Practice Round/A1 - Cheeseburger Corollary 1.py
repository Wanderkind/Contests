import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *

ans = []
for h in range(int(input())):
    s, d, k = U()
    bun = 2*(s + d)
    pat = s + 2*d
    good = bun >= k + 1 and pat >= k
    ans.append(f"Case #{h + 1}: {'YES' if good else 'NO'}")

for i in ans:
    print(i)
