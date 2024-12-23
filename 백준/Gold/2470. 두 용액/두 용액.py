import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
li.sort()

left = 0
right = n - 1
answer = abs(li[left] + li[right])
final = [li[left], li[right]]

while left < right:
    left_val = li[left]
    right_val = li[right]

    sum_ = left_val + right_val

    if abs(sum_) < answer:
        answer = abs(sum_)
        final = [left_val, right_val]
        if answer == 0:
            break

    if sum_ < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
