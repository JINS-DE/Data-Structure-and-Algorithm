import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
total = int(input())

answer = 0
start, end = 1, max(arr)

while start <= end:
    mid = (start+end)//2
    cnt=0
    for i in arr:
        if i > mid:
            cnt += mid
        else:
            cnt += i

    if cnt <= total :
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)