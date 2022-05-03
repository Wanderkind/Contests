from itertools import permutations
l=[''.join(i) for i in permutations('abcdefghijklmnopqrstuvwxyz',2)]
for _ in range(int(input())):
    print(l.index(input())+1)
