from itertools import combinations
l,c=map(int,input().split())
alpa = input().split()
alpa.sort()

vowels = {'a', 'e', 'i', 'o', 'u'}
answer = []

for comb in combinations(alpa,l):
    mo_count=0
    for char in comb:
        if char in vowels:
            mo_count+=1
    ja_count = l-mo_count
    if mo_count >= 1 and ja_count >=2:
        print(''.join(comb))