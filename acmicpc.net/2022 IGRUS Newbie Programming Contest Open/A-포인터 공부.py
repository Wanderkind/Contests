import sys
input=sys.stdin.readline

def p(i):
    if i==0: return 'a'
    if i==1: return 'ptr'
    return f'ptr{i}'

n=int(input())
print('int a;')
for i in range(1,n+1):
    s=f"int {'*'*i}{p(i)} = &{p(i-1)};"
    print(s)
