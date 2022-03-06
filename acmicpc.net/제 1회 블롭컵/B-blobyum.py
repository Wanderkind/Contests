n,k=map(int,input().split())
l=[*map(int,input().split())]
d=[];s=0;M=0
for i in range(-k,n):
    s+=l[i];d+=[s]
for i in range(n):
    z=d[i+k]-d[i]
    if M<z:M=z
print(M)
