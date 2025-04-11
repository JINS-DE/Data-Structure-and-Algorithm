from collections import deque

def solution(board):
    r = len(board)
    c = len(board[0])
    visited = [[-1] * c for _ in range(r)]

    # 시작점과 도착점 찾기
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'G':
                target = (i, j)
            elif board[i][j] == 'R':
                start = (i, j)

    q = deque([start])
    visited[start[0]][start[1]] = 0

    def move_point(x, y):
        result = []
        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx, ny = x, y
            # 계속 이동하다가 벽 또는 경계 만나면 멈춤
            while True:
                tx = nx + dx[i]
                ty = ny + dy[i]
                if 0 <= tx < r and 0 <= ty < c and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
            if (nx, ny) != (x, y):  # 이동한 경우만 추가
                result.append((nx, ny))
        return result

    while q:
        x, y = q.popleft()
        if (x, y) == target:
            return visited[x][y]
        for nx, ny in move_point(x, y):
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return -1
