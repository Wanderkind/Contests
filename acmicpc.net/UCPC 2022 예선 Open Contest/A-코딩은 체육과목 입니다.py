from math import*
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

n=ceil(int(input())/4)
for _ in range(n):
    print('long',end=' ')
print('int')
