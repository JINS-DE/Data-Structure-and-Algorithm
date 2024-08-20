'''
모든 도시를 방문하며 거리를 잰다. 
'''
from collections import deque
import sys
input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

# 거리 리스트 초기화 
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시의 거리는 0으로 설정

# 초기 큐(x)
queue=deque([x])

# 큐가 존재할 때까지
while queue:
    # 현재 노드
    current_node=queue.popleft()
    # 그래프에서 다음으로 갈 노드들 꺼내기
    for next_node in graph[current_node]:
        # 다음으로 갈 노드가 방문하지 않았다면!
        if distance[next_node]==-1:
            # 다음으로 갈 노드 = 현재 노드의 거리 수 + 1
            distance[next_node]=distance[current_node]+1
            # 다음 노드 큐 추가
            queue.append(next_node)
            
            
# 최종 결과 출력 (거리 K인 도시 찾기)
found = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

# 만약 거리 K인 도시가 없다면 -1 출력
if not found:
    print(-1)