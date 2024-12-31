import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
count = 0

for k in range(n):
    target = arr[k]
    start, end = 0, n - 1
    while start < end:
        if start == k:  # 현재 target 값을 제외해야 함
            start += 1
            continue
        if end == k:  # 현재 target 값을 제외해야 함
            end -= 1
            continue

        if arr[start] + arr[end] == target:
            count += 1
            break  # 한 번 찾으면 더 이상 찾을 필요 없음
        elif arr[start] + arr[end] < target:
            start += 1
        else:
            end -= 1

print(count)
