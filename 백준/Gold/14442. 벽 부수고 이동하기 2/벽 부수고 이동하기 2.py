from collections import deque
import sys

input=sys.stdin.readline
n,m,k = map(int,input().split())
maps=[list(map(int,input().strip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque([(0,0,k)]) # (x,y,남은 벽 부수기 횟수)

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][k] = 1
while q:
    x, y, remaining = q.popleft()

    if x == n - 1 and y == m - 1:
        print(visited[x][y][remaining])
        sys.exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 0 and visited[nx][ny][remaining] == 0:
                visited[nx][ny][remaining] = visited[x][y][remaining] + 1
                q.append((nx, ny, remaining))
            elif maps[nx][ny] == 1 and remaining > 0 and visited[nx][ny][remaining - 1] == 0:
                visited[nx][ny][remaining - 1] = visited[x][y][remaining] + 1
                q.append((nx, ny, remaining - 1))

print(-1)
