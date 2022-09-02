


import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n=int(input())
    a=[*U()] # len n
    b=[*U()] # len n
    y=1
    
    if any(a[i]>b[i]for i in range(n)):
        print('NO');y=0;continue
    
    if y:
        for i in range(n):
            if y and b[(i+1)%n]+1<b[i]:
                if b[i]!=a[i]:
                    print('NO');y=0;continue
    
    if y:print('YES')
