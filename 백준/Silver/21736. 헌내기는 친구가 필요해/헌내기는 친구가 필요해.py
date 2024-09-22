from collections import deque
import sys
input = sys.stdin.readline
# 입력 받기
N, M = map(int, input().split())

campus = [list(input().strip()) for _ in range(N)]

# 도연이의 위치 찾기
start_x, start_y = 0, 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start_x, start_y = i, j
    if start_x > 0 :
        break

# 이동 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 탐색
def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    people_count = 0

    while queue:
        cx, cy = queue.popleft()

        # 현재 위치에서 사람을 만나면 카운트 증가
        if campus[cx][cy] == 'P':
            people_count += 1

        # 상하좌우로 이동 가능한지 체크
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            
            # 캠퍼스 범위 안에 있고, 벽이 아니며, 아직 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < M and campus[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return people_count

# 도연이가 만난 사람의 수 구하기
result = bfs(start_x, start_y)

# 결과 출력
if result > 0:
    print(result)
else:
    print("TT")