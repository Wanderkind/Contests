from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n=int(input())
    if n==2:
        print('2 1')
        continue
    if n%2:
        l=[1]
        for i in range(2,n+1):
            if i%2:
                l.append(i-1)
            else:
                l.append(i+1)
    else:
        l=[1]
        for i in range(2,n+1):
            if i<n-1:
                if i%2:
                    l.append(i-1)
                else:
                    l.append(i+1)
            elif i==n-1:
                l.append(n)
            else:
                l.append(n-2)
    print(*l,sep=' ')
