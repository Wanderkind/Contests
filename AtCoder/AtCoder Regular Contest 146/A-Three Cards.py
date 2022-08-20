
from math import *
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

n=int(input())
a=[*U()]

b=[[],[],[],[],[],[]]
for i in a:
    z=len(str(i))
    b[z-1].append(i)
b.reverse()
for i in range(6):
    b[i].sort(reverse=True)

w=[]
z=0
cs=0
for i in b:
    for j in i:
        w.append(str(j))
        z+=1
        if z==3:cs=1;break
    if cs:break

w.sort(reverse=True)
print(''.join(w))
