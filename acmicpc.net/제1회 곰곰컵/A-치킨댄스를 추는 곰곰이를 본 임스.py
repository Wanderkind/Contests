import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

#for _ in range(int(input())):

n=int(input())
a,b=U()
print(min(n,a//2+b))
