import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
from math import *
#from itertools import *
#from random import *
#from functools import *


n, m, k = U()
ans = 0
for _ in range(n):
    s = [int(i) for i in input()]
    cnt = 0
    for i in range(m):
        if not s[i]:
            cnt += 1
        else:
            ans += max(cnt - k + 1, 0)
            cnt = 0
    ans += max(cnt - k + 1, 0)
print(ans)
