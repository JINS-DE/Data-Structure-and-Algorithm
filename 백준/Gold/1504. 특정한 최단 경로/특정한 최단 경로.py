def dijkstra(start):
    distance = [INF]*(N+1)
    distance[start] = 0
    heap=[]
    heapq.heappush(heap,(0,start))

    while heap:
        now_dist, now_node = heapq.heappop(heap)
        
        if now_dist > distance[now_node]:
            continue

        for next_node, next_dist in graph[now_node]:
            cost = now_dist + next_dist
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(heap,(cost,next_node))

    return distance

import sys,heapq
input = sys.stdin.readline
INF = 1e9
N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())

A=dijkstra(1)
B=dijkstra(v1)
C=dijkstra(v2)

answer = min(A[v1]+B[v2]+C[N], A[v2]+C[v1]+B[N])

if answer >= 1e9:
    print(-1)
else:
    print(answer)