import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

l=[*U()]
b=list(set(l))
if len(b)==2:
    p,q=b
    if l.count(p) in [2,3]:
        print('Yes')
        exit()
print('No')
