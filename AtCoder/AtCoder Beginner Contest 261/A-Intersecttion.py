U=lambda:map(int,input().split())
 
a,b,c,d=U()
z=-1
for i in range(101):
    if a<=i<=b and c<=i<=d:
        z+=1
print(max(z,0))
