import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

# 도시의 개수 N, 버스의 개수 M
n = int(input())
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 출발점과 도착점 입력
start, end = map(int, input().split())

# 거리 리스트 초기화 (무한대로 설정)
distance = [INF] * (n + 1)
distance[start] = 0  # 출발 도시의 거리는 0으로 설정

# 다익스트라 알고리즘 시작
heap = []
# 최소힙 초기값 : 가중치 0, start 노드
heapq.heappush(heap, (0, start))  # (비용, 도시)
while heap:
    current_weight,current_node=heapq.heappop(heap)
    
    # 이미 처리된 도시라면 continue
    if current_weight>distance[current_node]:
        continue

    # 인접한 도시들 확인
    for next_node, next_weight in graph[current_node]:
        # 현재 가중치 + 갈 예정의 도시의 가중치
        tmp_weight=current_weight+next_weight

        # 더 짧은 경로가 있을시 갱신하고 큐에 추가한다. 
        if tmp_weight < distance[next_node]:
            distance[next_node]=tmp_weight
            heapq.heappush(heap,(tmp_weight,next_node))

# 도착 도시의 최소 비용 출력
print(distance[end])
