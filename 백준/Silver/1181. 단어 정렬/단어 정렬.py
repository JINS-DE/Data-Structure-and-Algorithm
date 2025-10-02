import sys
input = sys.stdin.readline

n=int(input())
sets = set()
for _ in range(n):
    alpha = input().strip()
    sets.add(alpha)
    
alpha_li = list(sets)
alpha_li.sort(key = lambda x : (len(x),x) )

for st in alpha_li:
    print(st)