import sys
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().strip()))for _ in range(n)]

visited = [[[0,0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque([(0,0,0)])

while q:
    x,y,k = q.popleft()

    if x==n-1 and y==m-1:
        print(visited[x][y][k])
        sys.exit()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] ==0 and visited[nx][ny][k]==0:
                visited[nx][ny][k] = visited[x][y][k]+1
                q.append((nx,ny,k))
            elif graph[nx][ny]==1 and k==0:
                visited[nx][ny][k+1] = visited[x][y][k]+1
                q.append((nx,ny,k+1))
print(-1)