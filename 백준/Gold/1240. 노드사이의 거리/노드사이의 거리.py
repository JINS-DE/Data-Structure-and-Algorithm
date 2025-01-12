import sys
input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

def dfs(s, e, distance):
    if s == e:
        return distance
    visited[s] = 1
    for node, dist in adj[s]:
        if visited[node] == 0:
            result = dfs(node, e, distance + dist)
            if result is not None:
                return result
    visited[s] = 0  
    return None

for _ in range(m):
    visited = [0] * (n+1)
    s, e = map(int, input().split())
    print(dfs(s, e, 0))
