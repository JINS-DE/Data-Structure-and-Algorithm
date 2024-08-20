from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
room = [list(map(int, input().strip())) for _ in range(n)]

# 방문 및 벽 부순 횟수 초기화
dist = [[-1] * n for _ in range(n)]
dist[0][0] = 0

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 구현하기 위해 큐를 사용합니다.
dq = deque([(0, 0)])

while dq:
    x, y = dq.popleft()

    # 목적지에 도착하면 탐색 종료
    if x == n - 1 and y == n - 1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스 범위 확인
        if 0 <= nx < n and 0 <= ny < n:
            # 아직 방문하지 않은 경우
            if dist[nx][ny] == -1:
                if room[nx][ny] == 1:  # 빈 방(1)을 만난 경우
                    dist[nx][ny] = dist[x][y]
                    dq.appendleft((nx, ny))
                else:  # 벽(0)을 만난 경우
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))

# 도착지점의 최단 경로 출력
print(dist[n-1][n-1])
