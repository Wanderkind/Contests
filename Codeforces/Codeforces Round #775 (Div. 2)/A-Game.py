for _ in range(int(input())):
    n=int(input())
    I=[*map(int,input().split())]
    if 0 not in I:print(0)
    else:
        x=0
        while 1:
            x+=1
            if I[x]<1:
                m=x
                break
        x=n-1
        while 1:
            x-=1
            if I[x]<1:
                M=x
                break
        print(M-m+2)
