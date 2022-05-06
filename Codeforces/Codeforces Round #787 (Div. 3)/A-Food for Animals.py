import sys
input=sys.stdin.readline

for _ in range(int(input())):
    a,b,c,x,y=map(int,input().split())
    if a>=x and b>=y:
        z=1
    elif not (a<x and b<y):
        if a<x:
            if a+c>=x:
                z=1
            else:
                z=0
        else:
            if b+c>=y:
                z=1
            else:
                z=0
    else:
        if x+y-a-b<=c:
            z=1
        else:
            z=0
    print(['NO','YES'][z])
