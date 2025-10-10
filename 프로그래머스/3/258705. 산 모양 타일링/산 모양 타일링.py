"""
사다리꼴 안의 삼각형의 개수 = 2n+1 개
윗변의 길이 n, 아랫변의 길이 n+1
"""
def solution(n, tops):
    mod = 10007
    dp=[[0,0] for _ in range(n)]
    
    dp[0][0] = 2 if tops[0]==0 else 3
    dp[0][1] = 1
    
    for i in range(1,n):
        if tops[i]:
            dp[i][0] = dp[i-1][0]*3 + dp[i-1][1] * 2   
        else:
            dp[i][0] = dp[i-1][0]*2 + dp[i-1][1]    
            
        dp[i][1] = dp[i-1][0] + dp[i-1][1]
        
        dp[i][0]%=mod
        dp[i][1]%=mod
    
    answer = dp[n-1][0] + dp[n-1][1]
    answer%=mod
    return answer