import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())

for _ in range(int(input())):
    n,K,r,c=U()
    p=(r-1)%K
    q=(c-1)%K
    a=n//K
    for h in range(a):
        for i in range(K):
            z=['.'for _ in range(K)]
            z[(q+p-i)%K]='X'
            Z=''.join(z)
            for _ in range(a):
                print(Z,end='')
            print('')
