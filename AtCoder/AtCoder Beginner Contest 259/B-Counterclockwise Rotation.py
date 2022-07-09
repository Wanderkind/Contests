from math import*
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
 
a,b,D=U()
d=pi*D/180
print(cos(d)*a-sin(d)*b, sin(d)*a+cos(d)*b)
