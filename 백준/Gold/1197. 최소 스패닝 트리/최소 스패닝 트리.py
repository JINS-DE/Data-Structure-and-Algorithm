'''
최소 스패닝 트리를 구하는 문제.
입력에서 간선 리스트들이 주어진다. 크루스칼 사용

크루스칼 로직
1. 간선 정렬 : 가중치 기준 오름차순 정렬 (sort(key=lambda x : x[2]))
2. 간선 선택 : 정렬된 간선 중 사이클 형성 안되는 애들로 선택
3. 사이클 검사 : 사이클 형성 시 그 간선을 버림 (union-find)


'''

# 크루스칼 로직
import sys
v,e=map(int,input().split())
graph=[]
for i in range(e):
    u,v,w=map(int,input().split())
    graph.append((u,v,w))

def union(parent,rank,u,v):
    root_u = find(parent,u)
    root_v = find(parent,v)
    if rank[root_u] > rank[root_v]:
        parent[root_v]=root_u
    elif rank[root_u] < rank[root_v]:
        parent[root_u]=root_v
    else:
        parent[root_u]=root_v
        rank[root_v]+=1
    
def find(parent,u):
    if parent[u]!=u:
        parent[u]=find(parent,parent[u])
    return parent[u]
def kruscal(graph,e):
    mst=0
    parent=list(range(e+1))
    rank=[0]*(e+1)
    # 그래프 오름차순 정렬
    graph.sort(key=lambda x : x[2])
    for u,v,w in graph:
        # 인덱스 0부터 시작
        u-=1
        v-=1
        # 사이클 검사
        if find(parent,u)!=find(parent,v):
            union(parent,rank,u,v)
            mst+=w
    return mst
print(kruscal(graph,e))
