from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    indegree[v]+=1
q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    x=q.popleft()
    print(x,end=' ')
    for i in graph[x]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
            


