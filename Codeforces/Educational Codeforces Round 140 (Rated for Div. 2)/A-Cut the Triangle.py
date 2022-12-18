 
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

def sol():
    input()
    x1,y1=U()
    x2,y2=U()
    x3,y3=U()
    
    if len(set([x1, x2, x3]))<3 and len(set([y1, y2, y3]))<3:
        return False
        
    return True
    

for _ in range(int(input())):
    
    print("Yes" if sol() else "No")
