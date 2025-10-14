import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

# 1. 초기화
adj = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
build_time = [0] * (N + 1)
result_time = [0] * (N + 1) # 각 건물이 최종 완성되는 시간

# 2. 입력
for i in range(N):
    line = list(map(int,input().split()))
    build_time[i+1]=line[0]
    pre_node = line[1:-1]
    in_degree[i+1] = len(pre_node)
    for node in pre_node:
        adj[node].append(i+1)

# 3. 차수 0인애 q에 넣기
q= deque()
for node in range(1,N+1):
    if in_degree[node]==0:
        result_time[node]=build_time[node]
        q.append(node)

# 4. 위상정렬 
while q:
    curr=q.popleft()
    for nxt in adj[curr]:
        in_degree[nxt]-=1
        result_time[nxt] = max(result_time[nxt],result_time[curr]+build_time[nxt])
        if in_degree[nxt]==0:
            q.append(nxt)


# 5. 결과 출력
for i in range(1, N + 1):
    print(result_time[i])