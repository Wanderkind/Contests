import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n=int(input())
    print(2)
    l=[]
    i=-1
    while 1:
        i+=2
        k=-1
        w=0
        r=[]
        while 1:
            k+=1
            t=i*2**k
            if 2*t<=n:
                l+=[t,2*t]if w==0 else [2*t]
                w+=1
            else:
                break
        if w==0:
            break
    cha=list(set([i+1 for i in range(n)])-set(l))
    print(*(l+cha),sep=' ')
