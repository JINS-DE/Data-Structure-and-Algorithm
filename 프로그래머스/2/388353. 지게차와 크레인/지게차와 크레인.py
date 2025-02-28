from collections import deque
def solution(storage, requests):
    answer = 0
    n=len(storage)
    m=len(storage[0])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    # vistied 배열 만들기
    visited = [[-1]+[1] * (m)+[-1] for _ in range(n)]
    visited = [[-1]*(m+2)] + visited + [[-1]*(m+2)]
    
    def forklift(alpa):
        queue = deque([(0,0)])
        alpa_li = []
        v=[[0]*(m+2) for _ in range(n+2)]
        v[0][0]=1
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=dx[i]+x
                ny=dy[i]+y
                if 0<=nx<n+2 and 0<=ny<m+2 and v[nx][ny]==0 and visited[nx][ny]==-1:
                    v[nx][ny]=1
                    queue.append((nx,ny))
                if 0<=nx<n+2 and 0<=ny<m+2 and visited[nx][ny]==1 and storage[nx-1][ny-1]==alpa:
                    alpa_li.append((nx,ny))
        
        for x,y in alpa_li:
            visited[x][y]=-1
    
    def crane(alpa):
        for i in range(n):
            for j in range(m):
                if storage[i][j]==alpa:
                    visited[i+1][j+1]=-1
                    
    tmp=set()                                           
    for request in requests:
        if len(request)==1:
            forklift(request)
        else:
            if request[0] not in tmp:
                crane(request[0])

                tmp.add(request[0])

    for i in visited:
        answer+=i.count(1)
                    
        
        
    

#     def forklift(alpa):
#         nonlocal n,m
#         queue=deque()
#         for i in range(n):
#             for j in range(m):
#                 if storage[i][j]==alpa and visited[i][j]:
#                     queue.append((i,j))
        
#         while queue:
#             i,j=queue.popleft()
#             visited[i][j]=-1
#             for k in range(4):
#                 nx=dx[k]+i
#                 ny=dy[k]+j
#                 if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
#                     visited[nx][ny]=1

#     def crane(alpa):
#         queue=deque()
#         for i in range(n):
#             for j in range(m):
#                 if storage[i][j]==alpa and visited[i][j]!=-1:
#                     if visited[i][j]:
#                         queue.append((i,j))
#                     visited[i][j]=-1
#         v = [[0] * m for _ in range(n)]
#         while queue:
#             i,j=queue.popleft()
#             for k in range(4):
#                 nx=dx[k]+i
#                 ny=dy[k]+j
                
#                 if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
#                     visited[nx][ny]=1
                    
#                 if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1 and v[nx][ny]==0:
#                     queue.append((nx,ny))
#                     v[nx][ny]=1
                    
                
#     tmp=set()                                           
#     for request in requests:
#         if len(request)==1:
#             forklift(request)
#         else:
#             if request[0] not in tmp:
#                 crane(request[0])
#                 tmp.add(request[0])
            
#     for i in visited:
#         answer+=m-i.count(-1)
        
    
    
    return answer