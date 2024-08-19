from collections import deque

# 미로의 크기와 미로 정보를 입력받습니다.
n, m = map(int, input().split())  # n: 행(row)의 수, m: 열(column)의 수
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

# 상하좌우로 이동하기 위한 방향 벡터입니다.
# 순서대로 상, 하, 좌, 우를 나타냅니다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 구현하기 위해 큐를 사용합니다.
queue = deque()
queue.append((0, 0))  # 시작점 (0, 0)을 큐에 추가합니다.

# BFS 알고리즘 수행
while queue:
    x, y = queue.popleft()  # 큐에서 현재 위치를 꺼냅니다.
    
    # 현재 위치에서 상하좌우로 이동 가능한지 확인합니다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 미로의 범위를 벗어나면 무시합니다.
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        # 이동할 수 없는 칸(벽)이라면 무시합니다.
        if maze[nx][ny] == 0:
            continue
        
        # 아직 방문하지 않은 칸이라면 이동합니다.
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1  # 이동한 칸에 현재까지의 경로 길이를 더합니다.
            queue.append((nx, ny))  # 새로운 위치를 큐에 추가합니다.

# (N, M) 위치까지의 최단 경로 길이를 출력합니다.
# 여기서 n-1, m-1은 배열의 인덱스가 0부터 시작하기 때문에 사용합니다.
print(maze[n-1][m-1])
