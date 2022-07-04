U=lambda:map(int,input().split())

for _ in range(int(input())):
    n,m=U()
    for i in range(n):
        if 0<i%4<3:
            for j in range(m):
                print('01'[0<j%4<3],end=[' ','\n'][j==m-1])
        else:
            for j in range(m):
                print('10'[0<j%4<3],end=[' ','\n'][j==m-1])
