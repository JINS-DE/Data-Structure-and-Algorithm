import sys
import heapq
input = sys.stdin.readline
N,K = map(int,input().split())
adj = [[] for _ in range(200001)]
for i in range(200001):
    if i<200000:
        adj[i].append((i+1,1))
    if i>0:
        adj[i].append((i-1,1))
    if i*2<200001:
        adj[i].append((i*2,0))
dp = [float("inf")]*200001
dp[N]=0
heap = [(0,N)]
while heap:
    weight, curr = heapq.heappop(heap)

    if dp[curr] < weight:
        continue

    for nxt, nxt_weight in adj[curr]:
        total = weight+nxt_weight
        if total < dp[nxt]:
            dp[nxt] = total
            heapq.heappush(heap,(total,nxt))

print(dp[K])