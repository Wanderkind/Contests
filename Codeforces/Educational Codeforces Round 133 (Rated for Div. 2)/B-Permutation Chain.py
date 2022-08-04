import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

T=int(input())
for _ in range(T):
    n=int(input())
    l=[*range(1,n+1)]
    print(n)
    if n==2:
        print('1 2\n2 1')
    else:
        print(*l,sep=' ')
        l[0],l[-1]=l[-1],l[0]
        print(*l,sep=' ')
        j=2
        i=-1
        while 1:
            i+=1
            
            l[-i-1],l[-i-2]=l[-i-2],l[-i-1]
            print(*l,sep=' ')
            j+=1
            if j==n:break
            
            l[i],l[i+1]=l[i+1],l[i]
            print(*l,sep=' ')
            j+=1
            if j==n:break
