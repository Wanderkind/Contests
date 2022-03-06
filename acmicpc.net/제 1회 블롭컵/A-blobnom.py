n=int(input())
l=[*map(int,input().split())];d=[];M=max(l)
if len(l)>2:
    for i in range(1,n-1):
        a,b,c=l[i-1],l[i],l[i+1]
        b+=min(a,c)
        d+=[b]
    print(max(max(d),M))
else:print(max(l))
