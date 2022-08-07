import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())


T=int(input())
for _ in range(T):
    n=int(input())
    l=[] #len n
    X,x,Y,y=0,0,0,0
    for _ in range(n):
        p,q=U()
        if p>X:
            X=p
        if p<x:
            x=p
        if q>Y:
            Y=q
        if q<y:
            y=q
    print(2*(X-x+Y-y))
