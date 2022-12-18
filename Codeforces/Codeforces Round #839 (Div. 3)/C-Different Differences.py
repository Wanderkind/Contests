

from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())


def sol():
    k,n=U()
    m=k-1
    init=k*(k-1)//2
    while 1:
        if init<n:
            break
        else:
            init -= m-1
            m -= 1
    a=[1]
    for i in range(k-1):
        a.append(a[-1]+max(m,1))
        m -= 1
    print(*a, sep = " ")

for _ in range(int(input())):
    sol()
