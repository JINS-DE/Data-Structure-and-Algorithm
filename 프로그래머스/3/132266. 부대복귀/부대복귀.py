from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # 목적지에서 시작해서 모든 노드까지의 최단 거리 구함 (단 한번의 BFS로)
    dist = [-1] * (n + 1)
    dist[destination] = 0
    q = deque([destination])
    
    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)
    
    for start in sources:
        answer.append(dist[start])
    
    return answer
