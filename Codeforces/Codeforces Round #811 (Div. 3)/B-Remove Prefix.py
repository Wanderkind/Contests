import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

T=int(input())
for _ in range(T):
    n=int(input())
    q=0
    a=[*U()] #len n
    A=set(a)
    d={}
    for i in A:
        d[i]=0
    i=0
    while i<n:
        i+=1
        w=a[-i]
        if d[w]==0:
            d[w]+=1
            continue
        else:
            q=1
            break
    print(n-i+q)
