import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

n=int(input())
l=[0]+[*U()]
c=l[-1]
z=0
while 1:
    z+=1
    c=l[c-1]
    if c==0:break
print(z)
