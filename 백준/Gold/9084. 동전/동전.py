
# 예를 들어 1원 5원 10원이면, 1원 경우의 수 dp 위에 5원 경우의 수 dp 위에 10원 경우의 수 dp를 덮어쓰는 느낌
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    money_list = list(map(int, input().split()))
    goal = int(input())
    
    # dp 배열의 크기는 goal + 1로 설정해야 함
    dp = [0] * (goal + 1)
    dp[0] = 1  # 0원을 만드는 방법은 한 가지(아무 동전도 사용하지 않는 경우)
    
    # 각 동전별로 dp 배열을 업데이트
    for coin in money_list:
        for money in range(coin, goal + 1):  # 여기서 range(coin, goal + 1)로 수정
            dp[money] += dp[money - coin]  # 점화식 적용

    print(dp[goal])
