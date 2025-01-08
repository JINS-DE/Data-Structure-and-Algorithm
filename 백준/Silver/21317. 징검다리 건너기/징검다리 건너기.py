MAX = 999999

# DP 배열 및 징검다리 정보 초기화
d = [[MAX, MAX] for _ in range(21)]
v = [(0, 0) for _ in range(21)]

# 입력 받기
n = int(input())
for i in range(1, n):
    v1, v2 = map(int, input().split())
    v[i] = (v1, v2)

k = int(input())

# 초기 상태 설정
d[1][0] = 0
if n > 1:
    d[2][0] = v[1][0]
if n > 2:
    d[3][0] = min(v[1][0] + v[2][0], v[1][1])

# DP 점화식 계산
for i in range(4, n + 1):
    # 일반 점프만 사용하는 경우
    d[i][0] = min(v[i-1][0] + d[i-1][0], v[i-2][1] + d[i-2][0])
    # 매우 큰 점프를 사용하는 경우
    d[i][1] = min(
        v[i-1][0] + d[i-1][1],
        v[i-2][1] + d[i-2][1],
        k + d[i-3][0]
    )

# 결과 출력
print(min(d[n][0], d[n][1]))
