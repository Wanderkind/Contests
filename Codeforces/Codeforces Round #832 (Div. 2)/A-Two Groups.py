


from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

def sol():
    n=int(input())
    l=[*U()] # len n
    a=[]
    b=[]
    for i in l:
        if i>0:
            a.append(i)
        elif i<0:
            b.append(-i)
    print(abs(sum(a)-sum(b)))

for _ in range(int(input())):
    sol()
