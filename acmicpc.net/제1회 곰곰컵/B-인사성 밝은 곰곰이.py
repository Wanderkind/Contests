import sys
input=sys.stdin.readline
#U=lambda:map(int,input().split())

y=0
z=[]
for _ in range(int(input())):
    i=input().strip()
    if i=='ENTER':
        y+=len(set(z))
        z=[]
    else:
        z.append(i)
print(y+len(set(z)))
