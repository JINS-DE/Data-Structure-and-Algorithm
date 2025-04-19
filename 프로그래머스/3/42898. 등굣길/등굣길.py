from collections import deque
def solution(m, n, puddles):
    dp=[[0]*m for _ in range(n)]
    for x,y in puddles:
        dp[y-1][x-1]=-1

    # dp[x][y]=dp[x-1][y] + dp[x][y-1]
    
    # print(dp)
    dp[0][0]=1
    for i in range(n):
        for j in range(m):
            if dp[i][j]==-1:
                dp[i][j]=0
                continue
            if i>0 :
                dp[i][j]+=dp[i-1][j]
            if j>0 :
                dp[i][j]+=dp[i][j-1]
            
    # print(dp)

    return dp[n-1][m-1]%1000000007
