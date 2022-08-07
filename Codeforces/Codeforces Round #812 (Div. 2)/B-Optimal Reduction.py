import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())


T=int(input())
for _ in range(T):
    n=int(input())
    a=[*U()] # len n
    l=[]
    w=1
    z=0
    for i in range(n-1):
        d=a[i+1]-a[i]
        l.append(d)
        if d<0:
            z=1
        if z==1 and d>0:
            print('NO')
            w=0
            break
    if w:
        print('YES')
