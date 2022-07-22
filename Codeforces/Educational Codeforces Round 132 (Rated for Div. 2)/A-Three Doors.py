import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n=int(input())
    d=[*U()]
    if d[n-1]==0 or any(d[i]==i+1 for i in range(3)):
        print('NO')
    else:
        print('YES')
