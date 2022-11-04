import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

def sol():
    n=int(input())
    l=[*U()] # len n
    
    t=(l[0]==min(l))
    
    print(['alice','bob'][t])    

for _ in range(int(input())):
    sol()
