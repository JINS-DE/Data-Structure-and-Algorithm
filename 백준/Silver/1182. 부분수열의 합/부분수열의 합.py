from itertools import combinations
import bisect

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 배열을 반으로 나눠서 부분합 계산
mid = n // 2
left_part = arr[:mid]
right_part = arr[mid:]

left_sums = []
right_sums = []

# 부분합 구하기
for i in range(len(left_part) + 1):
    for comb in combinations(left_part, i):
        left_sums.append(sum(comb))

for i in range(len(right_part) + 1):
    for comb in combinations(right_part, i):
        right_sums.append(sum(comb))

# 정렬
right_sums.sort()

# 이분 탐색으로 m을 만족하는 쌍 찾기
answer = 0
for s in left_sums:
    target = m - s
    answer += bisect.bisect_right(right_sums, target) - bisect.bisect_left(right_sums, target)

# 공집합 제거
if m == 0:
    answer -= 1

print(answer)
