from collections import deque

def find_decreasing_number(n):
    if n > 1022:  # 감소하는 수는 최대 1022개
        return -1

    queue = deque(range(10))  # 초기값: 0 ~ 9를 큐에 넣음
    count = -1  # 순서를 셀 변수

    while queue:
        current = queue.popleft()
        count += 1

        if count == n:  # N번째 감소하는 수를 찾으면 반환
            return current

        last_digit = current % 10  # 현재 숫자의 마지막 자릿수
        for next_digit in range(last_digit):  # 감소하는 숫자를 만듦
            queue.append(current * 10 + next_digit)

n = int(input())
print(find_decreasing_number(n))
