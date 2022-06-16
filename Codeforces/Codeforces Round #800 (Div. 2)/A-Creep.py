import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    a,b=U()
    d=abs(a-b)
    x=min(a,b)
    if x<d:
        if a<b:
            t='1'*a+'0'*a+'1'*(b-a)
        else:
            t='0'*b+'1'*b+'0'*(a-b)
    else:
        if a<b:
            t='10'*a+'1'*(b-a)
        else:
            t='01'*b+'0'*(a-b)
    print(t)
