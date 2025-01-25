import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for i in range(m):
    u, w = map(int, input().split())
    adj[u].append(w)
    adj[w].append(u)

dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)
dfs_print = []
bfs_print = []

def dfs(v):
    if dfs_visited[v] == 0:
        dfs_print.append(v)
        dfs_visited[v] = 1
        for i in adj[v]:
            dfs(i)

dfs(v)

q = deque([v])
bfs_visited[v] = 1

while q:
    v = q.popleft()
    bfs_print.append(v)
    for i in adj[v]:
        if bfs_visited[i] == 0:
            bfs_visited[i] = 1
            q.append(i)

print(*dfs_print)
print(*bfs_print)
