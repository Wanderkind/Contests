import sys
input=sys.stdin.readline
for _ in range(int(input())):
    x,y=map(int,input().split())
    while 1:
        N=y//x
        if N<1:
            print('0 0')
            break
        if abs(y/x-N)>0.000001:
            print('0 0')
            break
        print(f'1 {N}')
        break
