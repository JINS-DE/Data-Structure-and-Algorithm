import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 원형 배열 처리
arr += arr[:k-1]

# 슬라이딩 윈도우 알고리즘
window = defaultdict(int)
unique_count = 0
max_count = 0

# 초기 윈도우 설정
for i in range(k):
    if window[arr[i]] == 0:
        unique_count += 1
    window[arr[i]] += 1

# 쿠폰 포함한 초밥 계산
max_count = unique_count + (1 if window[c] == 0 else 0)

for i in range(k, len(arr)):
    # 왼쪽 초밥 제거
    left_sushi = arr[i - k]
    window[left_sushi] -= 1
    if window[left_sushi] == 0:
        unique_count -= 1

    # 오른쪽 초밥 추가
    right_sushi = arr[i]
    if window[right_sushi] == 0:
        unique_count += 1
    window[right_sushi] += 1

    max_count = max(max_count, unique_count + (1 if window[c] == 0 else 0))

print(max_count)
