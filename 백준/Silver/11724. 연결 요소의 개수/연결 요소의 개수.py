import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline
n,m= map(int,input().split())
parent=list(range(n+1))

def union(u,v):
    root_u=find(u)
    root_v=find(v)
    if root_u!=root_v:
        parent[root_u]=root_v

def find(u):
    if parent[u] != u:
        parent[u]=find(parent[u])
    return parent[u]        


for i in range(m):
    u,v= map(int,input().split())
    union(u,v)
for i in range(len(parent)):
    find(i)
print(len(set(parent))-1)