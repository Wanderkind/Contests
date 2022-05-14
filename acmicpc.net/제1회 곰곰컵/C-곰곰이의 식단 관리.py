import sys
input=sys.stdin.readline
from collections import Counter
from math import ceil
#U=lambda:map(int,input().split())
n=int(input())
c=Counter(input().strip())['C']
print(ceil(c/(n-c+1)))
