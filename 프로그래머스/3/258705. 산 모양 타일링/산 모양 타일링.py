"""
사다리꼴 안의 삼각형의 개수 = 2n+1 개
윗변의 길이 n, 아랫변의 길이 n+1

dp[n][0] : 오른쪽 끝이 삼각형으로 끝나는 경우
dp[n][1] : 오른쪽 끝이 왼쪽으로긴 마름모로 끝나는 경우
"""
def solution(n, tops):
    # 1. 초기화
    mod = 10007
    dp = [[0,0] for _ in range(n)]
    dp[0][0] = 3 if tops[0]==1 else 2
    dp[0][1] = 1
    
    # 2. memorization
    for i in range(1,n):
        if tops[i]==1:
            dp[i][0] = dp[i-1][0]*3 + dp[i-1][1]*2
        else:
            dp[i][0] = dp[i-1][0]*2 + dp[i-1][1]
        
        dp[i][0] %= mod
        dp[i][1] = (dp[i-1][1] + dp[i-1][0])%mod
        
    return (dp[n-1][0] + dp[n-1][1])%mod