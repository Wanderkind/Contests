import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
 
 
L=[]
n=int(input())
for _ in range(n):
    L.append(input())
 
 
for i in range(n):
    for j in range(i+1,n):
        if L[i][j]=='W':
            if L[j][i]!='L':
                exit(print('incorrect'))
        elif L[i][j]=='L':
            if L[j][i]!='W':
                exit(print('incorrect'))
        else:
            if L[j][i]!='D':
                exit(print('incorrect'))
 
print('correct')
