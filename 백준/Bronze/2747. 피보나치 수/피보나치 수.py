import sys
n=sys.stdin.readline()
dp = {}
def fibonacci_top_down(n):
    # 기본 조건: F(0)과 F(1)
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # 이미 계산된 값이 있다면 그 값을 사용
    if n in dp:
        return dp[n]

    # 값을 계산하고 dp에 저장
    dp[n] = fibonacci_top_down(n - 1) + fibonacci_top_down(n - 2)
    return dp[n]

# 예시: F(5)를 구할 때
print(fibonacci_top_down(int(n)))  # 결과: 5