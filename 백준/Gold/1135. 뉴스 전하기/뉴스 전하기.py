"""
dp[u]는 u번째까지 걸리는 최소 시간
최소 시간 : 가장 많은 가지가 있는 애부터 처리해야 최소 시간 보장
   u
 / | \
dx dy dz

d1 = max(dx,dy,dz) # 가장큰애
d2 = max(dx,dy,dz) # 그다음큰애
d3 = max(dx,dy,dz) # 그다음큰애
dp[u] = max(d1,d2,d3)
"""

import sys
input = sys.stdin.readline
N = int(input())
parent = list(map(int,input().split()))
child = [[] for _ in range(N)]

for i in range(1,N):
    child[parent[i]].append(i)

dp = [0]*N
def dfs(u):
    # dp[u]의 값을 구하는게 목표

    child_lst = []
    for v in child[u]:
        dfs(v)
        child_lst.append(dp[v])
    
    child_lst.sort(reverse=True)

    dp[u]=0
    for i in range(len(child_lst)):
        dp[u] = max(dp[u],i+1+child_lst[i])

dfs(0)
print(dp[0])
