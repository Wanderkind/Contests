from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())


a=[10,18,25,31,36,40,43,45,46]
T=int(input())
for _ in range(T):
    n=int(input())
    if n==45:
        print(123456789)
        continue
    for i in range(9):
        if n<a[i]:
            l=i+1
            break
    d=n-l*(l+1)//2
    k=9-l
    q=d-k*(l-1)
    print(str(1+q)+''.join([str(9-t) for t in range(l-1)][::-1]))
