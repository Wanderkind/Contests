import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

T=int(input())
for h in range(T):
    n=int(input())
    a=[*U()] #len n
    A=[i%10 for i in a]
    k=list(set(a))
    if 0 in A:
        if len(k)==1:
            y=1
        elif len(k)==2:
            p,q=sorted(k)
            if p%10==5 and p+5==q:
                y=1
            else:
                y=0
        else:
            y=0
    elif 5 in A:
        if len(k)==1:
            y=1
        else:
            y=0
    else:
        b=[(w//10)%2 for w in a]
        c=[(w in [1,2,4,8])+0 for w in A]
        e=[b[i]^c[i] for i in range(n)]
        if len(list(set(e)))==2:
            y=0
        else:
            y=1
    print(['No','Yes'][y])
