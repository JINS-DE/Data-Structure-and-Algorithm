import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
m=int(input())
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]  # 각 부품별 필요한 개수를 저장할 DP 테이블
for i in range(m):
    x,y,k=map(int,input().split())
    graph[y].append((x,k)) # x 가야할 곳, k 가중치
    indegree[x]+=1

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
while q:
    node=q.popleft()
    
    for next_node, next_weight in graph[node]:
        if dp[node].count(0)==n+1: # node가 기본 부품일 경우
            dp[next_node][node] += next_weight
        else:
            for i in range(1,n+1):
                dp[next_node][i] += dp[node][i] * next_weight
        
        indegree[next_node] -= 1
        if indegree[next_node]==0:
            q.append(next_node)

# 결과 출력
for i in range(1, n + 1):
    if dp[n][i] > 0:
        print(i, dp[n][i])