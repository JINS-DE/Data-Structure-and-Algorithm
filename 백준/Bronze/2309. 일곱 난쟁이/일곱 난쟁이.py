import sys
from itertools import combinations
input=sys.stdin.readline
a=[int(input()) for _ in range(9)]
for i in combinations(a,7):
    if sum(i)==100:
        for j in sorted(i):
            print(j)
        break
