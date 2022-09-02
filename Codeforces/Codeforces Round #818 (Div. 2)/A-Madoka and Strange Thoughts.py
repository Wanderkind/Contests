import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n=int(input())
    print(n+2*(n//2)+2*(n//3))
