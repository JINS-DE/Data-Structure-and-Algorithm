def solution(n):
    if n%2:
        return 0
    dp=[0,3,11]
    for i in range(3,n//2+1):
        dp.append(dp[i-1]*3+sum(dp[1:i-1])*2+2)

    return dp[n//2]%1000000007
        