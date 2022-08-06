from itertools import combinations as p
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

n,m=U()
for i in p([*range(1,m+1)],n):
    print(*i,sep=' ')
