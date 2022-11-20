

from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    
    s=input()
    l=len(s)
    
    if any(i not in 'Yes' for i in s):
        print("no")
        return 0
    
    a=s[0]
    d='Yes'.index(a)
    
    for i in range(l):
        #print(s[i],'Yes'[(d+i)%3])
        if s[i]!='Yes'[(d+i)%3]:
            print("no");return 0
    
    print('yes');return 0

for _ in range(int(input())):
    #print()
    sol()
