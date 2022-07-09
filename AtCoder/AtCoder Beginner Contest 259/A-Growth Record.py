U=lambda:map(int,input().split())
 
n,m,x,t,d=U()
 
if m<=x:
    z=t-(x-m)*d
else:
    z=t
print(z)
