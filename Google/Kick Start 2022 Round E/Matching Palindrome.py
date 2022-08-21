

import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for h in range(int(input())):
    n=int(input())
    s=input().strip() # len n
    for i in range(1,n+1):
        a,b=s[:i],s[i:]
        if a[::-1]==a and b[::-1]==b:
            y=a;break
    print(f'Case #{h+1}: {y}')
