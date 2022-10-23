

from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

'''
def nd(n,s):
    
    for i in range(n-1):
        if s[i]>s[i+1]:
            return False
    return True

def op(n,s,z):
    
    for i in range(z,n):
        s[i]=1-s[i]
    
    return s
'''

def solve():
    
    n=int(input())
    s=[int(i) for i in input()] #len n
    
    t=-1
    
    w=0
    for i in range(n):
        S=s[i]
        if S!=w:
            t+=1
            w=S
    
    return max(t,0)


for _ in range(int(input())):
    print(solve())
