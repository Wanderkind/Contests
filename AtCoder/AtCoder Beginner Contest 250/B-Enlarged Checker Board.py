import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
#from math import*
'''
for _ in range(int(input())):
    '''

n,a,b=U()
for i in range(n):
    if i%2==0:
        s=(b*'.'+b*'#')*(n//2)+b*'.'*(n%2)
    else:
        s=(b*'#'+b*'.')*(n//2)+b*'#'*(n%2)
    for _ in range(a):
        print(s)
