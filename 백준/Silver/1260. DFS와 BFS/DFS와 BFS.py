import sys
from collections import deque
input=sys.stdin.readline
n,m,v=map(int,input().split())
li=[[] for _ in range(n+1)]

for i in range(m):
    start,end=map(int,input().split())
    li[start].append(end)
    li[end].append(start) # 양방향 그래프이므로 반대 방향도 추가

def dfs(li,start,visited=None):
    if visited is None:
        visited=[0]*len(li)
    visited[start]=1
    print(start,end=' ') # 방문한 노드 출력

    li[start].sort() # 방문 순서 오름차순으로
    for i in li[start]:
        if not visited[i]:
            dfs(li,i,visited)
            
    

def bfs(li,start):
    visited=[0]*len(li)
    queue=deque([start])
    while queue:
        v=queue.popleft()
        if visited[v]==0:
            visited[v]=1
            print(v,end=" ")
            li[v].sort()
            queue.extend(li[v])

dfs(li,v)
print()
bfs(li,v)
