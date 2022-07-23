import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
 
L=[]
D={}
d={}
n=int(input())
for k in range(n):
    i=input().strip()
    L.append(i)
    if i not in D:
        D[i]=0
    d[k]=D[i]
    D[i]+=1
for k in range(n):
    if d[k]==0:
        z=''
    else:
        z=f'({d[k]})'
    print(str(L[k])+z)
