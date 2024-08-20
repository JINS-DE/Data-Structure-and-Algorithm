from collections import deque
import sys
input = sys.stdin.readline

# 입력받기
R, C = map(int, input().split())
water = []  # 물의 위치를 저장하는 리스트
escape_map = [[] for _ in range(R)]  # 지도 정보를 저장하는 리스트

# 지도 초기화 및 위치 정보 저장
for i in range(R):
    line = input().strip()
    for j in range(C):
        if line[j] == 'D':  # 비버의 굴 위치
            end = (i, j)
        elif line[j] == 'S':  # 고슴도치의 시작 위치
            start = (i, j)
        elif line[j] == '*':  # 물의 위치
            water.append((i, j))
        escape_map[i].append(line[j])

# BFS를 위한 큐 초기화
water_queue = deque(water)  # 물의 확산을 처리하는 큐
mouse_queue = deque([start])  # 고슴도치의 이동을 처리하는 큐
direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # 상하좌우 방향 정의

# 고슴도치가 이동한 시간(거리)을 저장하는 배열, 초기값은 -1
dist = [[-1] * C for _ in range(R)]
dist[start[0]][start[1]] = 0  # 시작 위치의 시간은 0으로 설정

# BFS를 통한 탐색
while mouse_queue:
    # 물의 확산 처리
    for _ in range(len(water_queue)):
        w_x, w_y = water_queue.popleft()
        for dx, dy in direction:
            nx, ny = w_x + dx, w_y + dy
            if 0 <= nx < R and 0 <= ny < C and escape_map[nx][ny] == '.':
                escape_map[nx][ny] = '*'  # 물이 확산된 위치 표시
                water_queue.append((nx, ny))

    # 고슴도치의 이동 처리
    for _ in range(len(mouse_queue)):
        m_x, m_y = mouse_queue.popleft()
        # 도착지점(D)에 도착하면 종료
        if (m_x, m_y) == end:
            print(dist[m_x][m_y])
            sys.exit(0)
        for dx, dy in direction:
            nx, ny = m_x + dx, m_y + dy
            if 0 <= nx < R and 0 <= ny < C and dist[nx][ny] == -1:
                if escape_map[nx][ny] == '.':  # 이동 가능하면
                    dist[nx][ny] = dist[m_x][m_y] + 1
                    mouse_queue.append((nx, ny))
                elif escape_map[nx][ny] == 'D':  # 비버의 굴에 도착하면
                    print(dist[m_x][m_y] + 1)
                    sys.exit(0)

# 탈출이 불가능한 경우
print("KAKTUS")
