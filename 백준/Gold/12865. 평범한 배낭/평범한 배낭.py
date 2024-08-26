import sys
input = sys.stdin.readline

N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    weight, value = info[i-1]
    # print(weight, value)
    for w in range(K+1):
        # print(f"w: {w}")
        if w >= weight:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)
        else:
            dp[i][w] = dp[i-1][w]
        # print(dp[i])

print(dp[N][K])
