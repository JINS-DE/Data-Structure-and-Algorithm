import sys
input=sys.stdin.readline


n=int(input())
dp=[0]*(n+1)
path = ["" for _ in range(n+1)] # 최단 경로
path[1] = "1"

for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    prev = i-1
    if i%3==0 and dp[i]>dp[i//3]+1:
        dp[i]=dp[i//3]+1
        prev=i//3
    if i%2==0 and dp[i]>dp[i//2]+1:
        dp[i]=dp[i//2]+1
        prev=i//2
    path[i]=str(i)+" "+path[prev]
    

print(dp[n])
print(path[n])