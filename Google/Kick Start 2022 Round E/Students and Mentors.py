


import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())


for h in range(int(input())):
    n=int(input())
    r=[*U()] #len n
    Rs=sorted(r)
    m=[]
    for i in r:
        rs=Rs[:]
        rs.remove(i)
        l,r=0,n-1
        for _ in range(14):
            t=(l+r)//2
            if rs[t]>2*i:
                r=t
            else:
                l=t
        while rs[t]>2*i and t>1:
            t-=1
        x=rs[t]
        if x>2*i:
            x=-1
        m.append(x)
    print(f'Case #{h+1}:',end=' ')
    print(*m,sep=' ')
