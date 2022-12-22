from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    
    s=input()
    print(len(s)//len(set(s)))
    

#for _ in range(int(input())):
sol()
