def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y]=1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<m:
                
                if visited[nx][ny]==0 and graph[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                elif graph[nx][ny]==1:
                    visited[nx][ny]+=1


import sys
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
time = 0
while True:
    visited=[[0 for _ in range(m)] for _ in range(n)]
    bfs(0,0)
    time += 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                graph[i][j]=0
    
    blank=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                blank+=1

    if blank==0:
        print(time)
        break