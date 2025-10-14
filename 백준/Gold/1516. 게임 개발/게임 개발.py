import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

# 1. 자료구조 초기화
adj = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
build_time = [0] * (N + 1)
result_time = [0] * (N + 1) # 각 건물이 최종 완성되는 시간

# 2. 입력 받으며 그래프, 진입차수, 건설시간 완전하게 생성
for i in range(1, N + 1):
    line = list(map(int, input().split()))
    build_time[i] = line[0]
    
    prerequisites = line[1:-1]
    in_degree[i] = len(prerequisites)
    
    for pre in prerequisites:
        adj[pre].append(i)

# 3. 진입차수가 0인 노드를 큐에 추가 (위상정렬 시작점)
q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)
        result_time[i] = build_time[i] # 선수 건물이 없으므로 바로 건설 시작 및 완료

# 4. 위상 정렬 실행
while q:
    current_node = q.popleft()

    for next_node in adj[current_node]:
        # ★ 핵심 로직 ★
        # next_node는 current_node가 끝난 후에야 지을 수 있으므로,
        # next_node의 완료 시간은 최소한 current_node의 완료 시간만큼은 걸린다.
        # 여러 선수 건물 중 가장 늦게 끝나는 시간을 저장해야 하므로 max 사용
        result_time[next_node] = max(result_time[next_node], result_time[current_node])
        
        in_degree[next_node] -= 1

        # 모든 선수 건물이 완성되었다면
        if in_degree[next_node] == 0:
            # 저장된 가장 늦은 완료 시간(시작 시간)에 자신의 건설 시간을 더한다
            result_time[next_node] += build_time[next_node]
            q.append(next_node)

# 5. 결과 출력
for i in range(1, N + 1):
    print(result_time[i])