from collections import Counter
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
n=int(input())
k=[*U()]
l=[i%7 for i in k]
c=Counter(l)
e=[[(i*j)%7 for j in range(min(c[i]+1,7))]for i in c]

L=[]
C=len(c)

if C==1:
    for i in e[0]:
        L.append(i%7)

if C==2:
    for i in e[0]:
        for j in e[1]:
            L.append((i+j)%7)

if C==3:
    for i in e[0]:
        for j in e[1]:
            for k in e[2]:
                L.append((i+j+k)%7)

if C==4:
    for i in e[0]:
        for j in e[1]:
            for k in e[2]:
                for l in e[3]:
                    L.append((i+j+k+l)%7)

if C==5:
    for i in e[0]:
        for j in e[1]:
            for k in e[2]:
                for l in e[3]:
                    for m in e[4]:
                        L.append((i+j+k+l+m)%7)

if C==6:
    for i in e[0]:
        for j in e[1]:
            for k in e[2]:
                for l in e[3]:
                    for m in e[4]:
                        for n in e[5]:
                            L.append((i+j+k+l+m+n)%7)

if C==7:
    for i in e[0]:
        for j in e[1]:
            for k in e[2]:
                for l in e[3]:
                    for m in e[4]:
                        for n in e[5]:
                            for o in e[6]:
                                L.append((i+j+k+l+m+n+o)%7)

print(['NO','YES'][4 in L])
