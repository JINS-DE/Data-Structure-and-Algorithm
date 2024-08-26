'''
# dp 설계
- dp 테이블 : dp=[[0]*(N) for _ in range(N)]
- dp[시작행렬][끝행렬] = 최소 연산 횟수

'''

# python3 시간 초과
# pypy3로 통과

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
for i in range(1,N):
    for j in range(i,N):
        left=j-i
        right=j
        dp[left][right]=sys.maxsize
        for k in range(left,right):
            dp[left][right]=min(dp[left][right],dp[left][k]+dp[k+1][right]+arr[left][0]*arr[k][1]*arr[right][1])

print(dp[0][N - 1])