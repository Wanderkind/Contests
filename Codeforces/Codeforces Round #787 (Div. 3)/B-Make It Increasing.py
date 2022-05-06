import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    l=[*map(int,input().split())]
    cont=1
    s=0
    while cont:
        if l[-1]<n-1:
            print(-1)
            cont=0
            break
        z=n-1
        while z>0:
            z-=1
            while l[z]>=l[z+1]:
                l[z]//=2
                s+=1
            if l[z]<z:
                print(-1)
                cont=0
                break
        if cont:print(s)
        break
