import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
    visited[n] = 1
    for i in range(len(adj[n])):
        next = adj[n][i][0]
        if not visited[next]:
            dist[next] = adj[n][i][1] + dist[n]
            dfs(next)


n = int(input())
visited = [0 for i in range(n+1)]
adj = [[] for i in range(n+1)]
dist = [0 for i in range(n+1)]
for i in range(1,n):
    u, v, w = map(int, input().split())
    adj[u].append([v,w])
    adj[v].append([u,w])

dfs(1)
print(max(dist))
