from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

n,x=U()
t=[*U()] # len n

i=0
while 1:
    if t[i]<x:break
    i=(i+1)%n
    x+=1

print(i+1)
