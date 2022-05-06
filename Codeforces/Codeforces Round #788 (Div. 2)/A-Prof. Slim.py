import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    L=[*map(int,input().split())]
    t=[abs(i) for i in L]
    l=t[:]
    for i in range(n-1,0,-1):
        if l[i]==l[i-1]:
            del l[i]
    c=len(l)
    if c==1:
        print('YES')
    else:
        m=[]
        for i in range(c):
            if i==0:
                if l[i]<l[i+1]:
                    m.append(i)
            elif i==c-1:
                if l[i-1]>l[i]:
                    m.append(i)
            else:
                if l[i-1]>l[i] and l[i]<l[i+1]:
                    m.append(i)
        if len(m)>1:
            print('NO')
        else:
            k=m[0]
            C=len([i for i in L if i<0])
            if k==0:
                z=t[0]
                v=t.count(z)
                if C>v:
                    print('NO')
                else:
                    print('YES')
            elif k==c-1:
                z=t[-1]
                v=t.count(z)
                if n-C>v:
                    print('NO')
                else:
                    print('YES')
            else:
                z=t.index(l[k])
                y=z
                while t[y]==l[k]:
                   y+=1
                if z<=C<=y:
                    print('YES')
                else:
                    print('NO')
