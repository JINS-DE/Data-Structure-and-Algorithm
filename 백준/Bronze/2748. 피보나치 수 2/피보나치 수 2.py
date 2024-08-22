n=int(input())
# dp 배열 생성
dp=[0]*(n+1)
# dp 초기값 생성
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    # dp 식 선언
    dp[i]=dp[i-1]+dp[i-2]
# 결과
print(dp[n])