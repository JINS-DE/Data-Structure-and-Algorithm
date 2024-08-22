'''
정점의 집합을 둘로 분할, 정점 끼리 서로 인접하지 않도록 분할! = 이분 그래프
'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 호출 한도를 늘려줍니다.

def dfs(start, visited, graph, group):
    visited[start] = group # 현재 노드의 그룹 저장 

    for v in graph[start]:
        if visited[v]==0:
            # -group : 현재 노드의 그룹과 다른 값 전달
            result = dfs(v,visited,graph,-group)
            if not result:
                return False
        else:
            # 이미 방문한 곳 중에, 노드가 현재 그룹과 같으면 이분 그래프가 아니다.
            if visited[v]==group:
                return False
    return True 


# 테스트 케이스 개수 K
k=int(input())

# 정점의 개수 V, 간선의 개수 E
for i in range(k):
    V, E = map(int,input().split())
    graph=[[] for _ in range(V+1)]
    visited=[0]*(V+1)
    for j in range(E):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 모든 정점 확인
    for i in range(1, V+1):
        if visited[i] == 0:
            result = (dfs(i, visited, graph, 1))
            if not result:
                break
    print("YES") if result else print("NO")