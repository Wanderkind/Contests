import sys
input=sys.stdin.readline

for _ in range(int(input())):
    l=list(input().strip())
    n=len(l)
    while 1:
        if ('1' not in l and '0' not in l):
            print(n)
            break
        elif '1' not in l:
            if l[0]=='0':
                print(1)
            else:
                i=-1
                while i<n-1:
                    i+=1
                    if l[i]=='0':
                        break
                print(i+1)
        elif '0' not in l:
            if l[-1]=='1':
                print(1)
            else:
                i=0
                while 0<1:
                    i+=1
                    if l[n-i]=='1':
                        break
                print(i)
        else:
            one=-1
            zer=-1
            i=-1
            while i<n-1:
                i+=1
                if l[i]=='1':
                    one=i
                if l[i]=='0':
                    zer=i
                    break
            if one!=-1 and zer!=-1:
                print(zer-one+1)
        break
