n=int(input())
m=int(2*n)
a,b=divmod(m,8)
init=int(str(b)*(b>0)+'8'*a) if a>0 else b
print(m)
print(init//2)
