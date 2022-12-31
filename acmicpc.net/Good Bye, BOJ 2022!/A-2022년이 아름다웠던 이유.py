#from itertools import combinations as C
#from itertools import permutations as P
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

from collections import Counter as C
def fc(n):
    l=[]
    i=2
    while n>1:
        if n%i:i+=1
        else:l.append(i);n/=i
    c=C(l)
    return [[i,c[i]]for i in c]

def s(n):
    c=fc(n)
    return prod(sum(i[0]**j for j in range(i[1]+1)) for i in c)-n

def sol():
    n=int(input())
    if s(n)<=n:return False
    
    for i in range(2,n):
        if n%i==0:
            if s(i)>i:return False
    
    return True
    

for _ in range(int(input())):
    
    print("Good Bye" if sol() else "BOJ 2022")
