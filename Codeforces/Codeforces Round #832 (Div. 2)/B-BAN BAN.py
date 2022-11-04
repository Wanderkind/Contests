


from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

def sol():
    n=int(input())
    t=(n+1)//2
    print(t)
    for i in range(t):
        a=3*i+2
        b=3*(n-i)
        print(a,b)
    

for _ in range(int(input())):
    sol()
