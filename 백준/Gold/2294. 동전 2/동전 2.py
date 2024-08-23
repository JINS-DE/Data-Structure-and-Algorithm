import sys
input = sys.stdin.readline
n,k = map(int,input().split())
coin_list = list(int(input()) for _ in range(n))
dp = [100001]*(k+1)
dp[0] = 0

for coin in coin_list:
    for i in range(coin,k+1):
        dp[i]=min(dp[i],dp[i-coin]+1)

if dp[-1] == 100001 :
    print(-1)
else :
    print(dp[-1])