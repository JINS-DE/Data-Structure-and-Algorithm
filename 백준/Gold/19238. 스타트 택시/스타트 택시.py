from collections import deque

# BFS로 최단 거리 계산
def bfs_find_closest_passenger(taxi_x, taxi_y, fuel):
    queue = deque([(taxi_x, taxi_y, 0)])  # (현재 위치 x, y, 이동 거리)
    visited = [[False] * N for _ in range(N)]
    visited[taxi_x][taxi_y] = True
    candidates = []

    while queue:
        x, y, dist = queue.popleft()

        # 승객이 있는 위치라면 후보로 추가
        if (x, y) in passenger_start:
            candidates.append((dist, x, y))

        # 4방향 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    # 후보 중 가장 가까운 승객 선택 (거리 > 행 > 열 순서로 정렬)
    if candidates:
        candidates.sort()
        return candidates[0]  # (거리, x, y)
    return None

# 목적지까지의 거리 계산
def bfs_to_destination(start_x, start_y, dest_x, dest_y, fuel):
    queue = deque([(start_x, start_y, 0)])  # (현재 위치 x, y, 이동 거리)
    visited = [[False] * N for _ in range(N)]
    visited[start_x][start_y] = True

    while queue:
        x, y, dist = queue.popleft()

        # 목적지 도착
        if (x, y) == (dest_x, dest_y):
            return dist

        # 4방향 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return -1  # 목적지에 도달할 수 없음

# 입력 처리
N, M, fuel = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]  # 0: 빈칸, 1: 벽

taxi_x, taxi_y = map(int, input().split())
taxi_x, taxi_y = taxi_x - 1, taxi_y - 1  # 0-index로 변환

passenger_start = {}
passenger_dest = {}

for _ in range(M):
    start_x, start_y, dest_x, dest_y = map(int, input().split())
    passenger_start[(start_x - 1, start_y - 1)] = (dest_x - 1, dest_y - 1)

# 시뮬레이션 시작
for _ in range(M):
    # 가장 가까운 승객 찾기
    result = bfs_find_closest_passenger(taxi_x, taxi_y, fuel)
    if not result:  # 승객을 찾을 수 없음
        print(-1)
        exit(0)

    dist_to_passenger, px, py = result

    # 연료 부족 시 종료
    if fuel < dist_to_passenger:
        print(-1)
        exit(0)

    # 승객 위치로 이동
    fuel -= dist_to_passenger
    destination_x, destination_y = passenger_start.pop((px, py))

    # 목적지까지 거리 계산
    dist_to_destination = bfs_to_destination(px, py, destination_x, destination_y, fuel)
    if dist_to_destination == -1 or fuel < dist_to_destination:
        print(-1)
        exit(0)

    # 목적지까지 이동
    fuel -= dist_to_destination
    fuel += dist_to_destination * 2  # 도착 시 연료 충전
    taxi_x, taxi_y = destination_x, destination_y

# 모든 승객을 이동시킨 후 남은 연료 출력
print(fuel)
