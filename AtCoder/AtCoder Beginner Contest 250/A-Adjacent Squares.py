import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
#from math import*
'''
for _ in range(int(input())):
    '''


h,w=U()
r,c=U()
if h!=1 and w!=1:
    a=r==1 or r==h
    b=c==1 or c==w
elif h==1 and w==1:
    a=b=2
else:
    if h==1:
        a=2
        b=c==1 or c==w
    else:
        a=r==1 or r==h
        b=2
print(4-a-b)
