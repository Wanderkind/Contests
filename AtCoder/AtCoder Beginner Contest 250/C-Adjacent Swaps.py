import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
#from math import*

n,q=U()
l=[i+1 for i in range(n)]
d={}
for i in range(n):
    d[i+1]=i
for _ in range(q):
    i=int(input())
    e=d[i]
    if e!=n-1:
        j=l[e+1]
        l[e]=j
        l[e+1]=i
        d[i]+=1
        d[j]-=1
    else:
        j=l[e-1]
        l[e]=j
        l[e-1]=i
        d[i]-=1
        d[j]+=1
for i in l:
    print(i,end=' ')
