'''
1. 주어진 입력들을 union_find 한다.
2. 1번 컴퓨터에 연결되어 있는 친구들을 찾는다. 
'''
import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline
vertex=int(input())
edge=int(input())

parent=list(range(vertex+1))

def union(v,u):
    root_v=find(v)
    root_u=find(u)
    if root_v!=root_u:
        parent[root_u]=root_v
def find(u):
    if parent[u] != u:
        parent[u]=find(parent[u])
    return parent[u]

for i in range(edge):
    v,u=map(int,input().split())
    union(v,u)

cnt=0
for i in parent:
    if find(i)==find(parent[1]):
        cnt+=1

print(cnt-1)