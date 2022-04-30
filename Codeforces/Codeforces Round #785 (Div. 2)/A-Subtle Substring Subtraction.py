import sys
input=sys.stdin.readline
for _ in range(int(input())):
    S=list(input().strip())
    n=len(S)
    for i in range(len(S)):
        S[i]=ord(S[i])-96
    z=sum(S)
    if n%2==0:
        print('Alice',z)
    else:
        if n==1:
            print('Bob',z)
        else:
            p,q=S[0],S[-1]
            if p>q:
                a=z-q
                b=q
            else:
                a=z-p
                b=p
            if a>b:
                print('Alice',a-b)
            else:
                print('Bob',b-a)
