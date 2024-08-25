import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    s, e = map(int, input().split())
    li.append((s, e))

# 종료 시간 기준으로 정렬하고, 종료 시간이 같으면 시작 시간이 빠른 순으로 정렬
li.sort(key=lambda x: (x[1], x[0]))

cnt = 0
t_e = 0  # 가장 마지막에 선택한 회의의 종료 시간
for s, e in li:
    if t_e <= s:  # 이전 회의 종료 시간 이후에 시작하는 회의일 때만
        cnt += 1
        t_e = e
print(cnt)