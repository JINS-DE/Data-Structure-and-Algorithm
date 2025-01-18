from itertools import combinations

N = int(input())

result = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        num = ''.join(map(str, reversed(j)))
        result.append(int(num))
result.sort()
if N >= len(result):
	print(-1)
else:
	print(result[N])