import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

if n == 1:  # 예외 처리 (n이 1이면 차이를 만들 수 없음)
    print(0)
    sys.exit()

arr.sort()

left = 0
right = 1
answer = sys.maxsize

while right < n:
    gap = arr[right] - arr[left]

    if gap >= m:
        answer = min(answer, gap)
        left += 1
        if left == right:  # left와 right가 같아지면 right도 증가
            right += 1
    else:
        right += 1

print(answer)
