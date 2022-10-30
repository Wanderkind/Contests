from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

P=sorted([float(input())for _ in range(10)])[::-1]

k=10**9

for i in range(9):
    k*=P[i]/(i+1)

print(k)
