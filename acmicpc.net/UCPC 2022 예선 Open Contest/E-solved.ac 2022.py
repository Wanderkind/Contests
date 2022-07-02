from math import*
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())


N=int(input())
if N==0:exit(print(0))

KK=[0,
0,0,0,0,0,30,31,31,30,31,30,31,
31,29,31,30,31,30,31,31,30,31,30,31,
31,28,31,30,31,30,31,31,30,31,30,31,
31,28,31,30,31,30,31,31,30,31,30]

from itertools import accumulate as AC
K=list(AC(KK))

L=[]
for _ in range(N):
    date,time,lev=input().split()
    
    Y,M,D=map(int,date.split('/'))
    h,m,s=map(int,time.split(':'))
    YM=(Y-2019)*12+M-1
    DP=K[YM]
    S=(DP+D)*86400+3600*h+60*m+s
    L.append([int(lev),S])

tN=L[-1][1]

AA=BB=0
for i in range(N):
    a,b=L[i]
    p=max(0.5**((tN-b)/31536000),0.9**(N-i-1))
    AA+=p*a
    BB+=p

print(round(AA/BB))
