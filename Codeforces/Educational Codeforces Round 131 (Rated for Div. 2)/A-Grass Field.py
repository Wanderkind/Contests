import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
 
for _ in range(int(input())):
    a,b=U()
    c,d=U()
    if a+b+c+d==0:
        print(0)
    elif a+b+c+d==4:
        print(2)
    else:
        print(1)
