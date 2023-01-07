from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    n=int(input())
    l=[input()for _ in range(n)]
    for i in l[::-1]:
        print(i)
    

#for _ in range(int(input())):
    
sol()
    #print()
