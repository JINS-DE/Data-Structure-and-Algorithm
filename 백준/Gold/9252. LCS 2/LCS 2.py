st1 = input().strip()
st2 = input().strip()

n = len(st1)
m = len(st2)

# dp 테이블 초기화: n+1 x m+1 크기
dp = [[""] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 현재 비교할 문자: st1의 (i-1)번째 문자와 st2의 (j-1)번째 문자
        if st1[i - 1] == st2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + st1[i-1]
        else:
            if len(dp[i][j-1])>len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
answer=len(dp[-1][-1])
print(answer)
if answer!=0:
    print(dp[-1][-1])