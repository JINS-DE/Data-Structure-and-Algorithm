'''
*문제 접근 방식
1. 팰린드롬 판단: 먼저, 문자열의 특정 부분이 팰린드롬인지 빠르게 판단할 수 있어야 합니다.
2. 최소 분할 수 계산: 문자열의 최소 분할 수를 구하기 위해 DP를 활용합니다.

*단계별로 접근하는 방법
1. 팰린드롬 판단을 위한 DP 배열 만들기
먼저, 주어진 문자열의 모든 부분 문자열이 팰린드롬인지 아닌지를 저장하는 2차원 배열 is_palindrome를 만듭니다.

is_palindrome[i][j]는 문자열의 i부터 j까지의 부분 문자열이 팰린드롬이면 True, 아니면 False입니다.
이 배열을 채우기 위해 다음과 같은 점화식을 사용할 수 있습니다:

점화식:
기저 사례:
길이가 1인 문자열은 항상 팰린드롬이다. 즉, is_palindrome[i][i] = True
길이가 2인 문자열 s[i] == s[i+1]이면 팰린드롬이다. 즉, is_palindrome[i][i+1] = (s[i] == s[i+1])
일반 사례:
길이가 3 이상인 문자열은 양 끝 문자가 같고, 가운데 부분 문자열이 팰린드롬이면 팰린드롬이다. 즉, is_palindrome[i][j] = (s[i] == s[j] and is_palindrome[i+1][j-1])

2. 최소 분할 수 계산을 위한 DP 배열 만들기
두 번째로, 최소 분할 수를 저장하는 1차원 배열 dp를 정의합니다.

dp[i]는 문자열의 처음부터 i까지의 최소 팰린드롬 분할 수를 의미합니다.
점화식:

만약 s[0:i+1]가 팰린드롬이면, dp[i] = 1입니다. (문자열 전체가 하나의 팰린드롬으로 구성될 수 있으므로)
그렇지 않다면, dp[i]는 문자열을 0부터 j까지의 최소 분할 수(dp[j])와 문자열의 j+1부터 i까지가 팰린드롬이라면 1을 더한 값의 최소값이 됩니다.
점화식으로 설명하기
dp[i] = min(dp[j] + 1) (단, 0 <= j < i 그리고 s[j+1:i+1]가 팰린드롬일 때)
'''

def min_palindrome_partition(s):
    n = len(s)
    
    # 팰린드롬 여부를 저장할 2차원 배열
    is_palindrome = [[False] * n for _ in range(n)]
    
    # DP 배열 초기화
    dp = [float('inf')] * n
    
    # 팰린드롬 여부를 미리 계산
    for i in range(n):
        is_palindrome[i][i] = True  # 길이가 1인 팰린드롬
    
    for length in range(2, n+1):  # 부분 문자열의 길이
        for left in range(n-length+1):
            right = left + length - 1
            if length == 2:
                is_palindrome[left][right] = (s[left] == s[right])
            else:
                is_palindrome[left][right] = (s[left] == s[right]) and is_palindrome[left+1][right-1]
    
    # 최소 분할 수 계산
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 1  # 전체가 팰린드롬인 경우
            # print(f"i={i} ,dp={dp}]")
        else:
            for j in range(i):
                if is_palindrome[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
                # print(f"i={i}, j={j } ,dp={dp}]")
    
    return dp[-1]

# 입력
s = input()
print(min_palindrome_partition(s))