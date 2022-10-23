from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

'''
def solve():
    return 0
'''

h,w=U()
L=[0 for _ in range(w)]

for _ in range(h):
    i=input()
    for j in range(w):
        L[j]+= i[j]=='#'

print(*L,sep=' ')
