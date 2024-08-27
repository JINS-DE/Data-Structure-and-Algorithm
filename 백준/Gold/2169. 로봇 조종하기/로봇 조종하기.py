import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-sys.maxsize] * M for _ in range(N)]
dp[0][0] = arr[0][0]

# dp 초기화, 맨 위에 줄은 위에서 내려오지도 오->왼쪽으로 오지도 않는다. 맨 위에 줄은 arr첫 줄 그대로 들어가면 된다. 
for j in range(1, M):
    dp[0][j] = dp[0][j - 1] + arr[0][j]

# 왼쪽에서 오른쪽 이동 방향 "--------->"
# 오른쪽에서 왼쪽 이동 방향 "<---------"
for i in range(1, N):
    # temp의 왼쪽 배열 temp[0] 의미 : 왼쪽에서 오른쪽으로 이동하면서 가치를 담아줄 배열
    # temp의 오른쪽 배열 temp[1] 의미 : 오른쪽에서 왼쪽으로 이동하면서 가치를 담아줄 배열
    temp = [[None] * M, [None] * M]
    
    # temp[0][0]은 왼쪽 처음, 자기 가치와 위쪽 가치를 더해 놓고 시작.
    # temp[1][-1]은 오른쪽 처음, 자기 가치와 위쪽 가치를 더해 놓고 시작. 
    temp[0][0], temp[1][-1] = dp[i - 1][0] + arr[i][0], dp[i - 1][-1] + arr[i][-1]
    for j in range(1, M):
        # 왼쪽에서 오른쪽으로 가면서 위에 가치와 왼쪽의 가치중 max값을 자기의 가치와 합한다. 
        temp[0][j] = max(temp[0][j - 1], dp[i - 1][j]) + arr[i][j]
        # 오른쪽에서 왼쪽으로 가면서 위에 가치와 오른쪽의 가치중 max값을 자기의 가치와 합한다. 
        temp[1][M - j - 1] = max(temp[1][M - j], dp[i - 1][M - j - 1]) + arr[i][M - j - 1]
    for j in range(M):
        # 왼쪽으로 갔을 때와 오른쪽으로 갔을 때의 max값은 dp에 넣는다. 
        dp[i][j] = max(temp[0][j], temp[1][j])

print(dp[-1][-1])