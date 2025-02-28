def find_melt_cheese():
    global n,m
    flag=True
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                flag = False
                air_cnt=0
                for k in range(4):
                    nx=dx[k]+i
                    ny=dy[k]+j
               
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny]==-1:
                        air_cnt+=1

                    if air_cnt>=2:
                        queue.append((i,j))
                        break
    return flag

def aircheck(a,b):
    q.append((a,b))
    graph[a][b]=-1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=-1
                q.append((nx,ny))

import sys
from collections import deque
input=sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=deque()
q=deque()
answer=0

aircheck(0,0)

while True:
    
    if find_melt_cheese():
        print(answer)
        break
        
    while queue:
        x,y=queue.popleft()
        graph[x][y]=-1
        for k in range(4):
            nx=dx[k]+x
            ny=dy[k]+y
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                aircheck(nx,ny)
    answer+=1