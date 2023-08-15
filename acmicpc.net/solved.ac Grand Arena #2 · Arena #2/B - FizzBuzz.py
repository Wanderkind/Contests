from math import *
import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x):
    print(x); sys.stdout.flush()
#from itertools import *
#from random import *


s = []
for _ in range(3):
    s.append(input())

def st(s): return s in "FizzBuzz"

ans = 0
for i in range(3):
    if not st(s[i]):
        ans = int(s[i]) + 3 - i
        break

p, q = ans % 3, ans % 5
if p*q:
    print(ans)
else:
    if ans % 3 == 0:
        print("Fizz", end = '')
    if ans % 5 == 0:
        print("Buzz", end = '')
