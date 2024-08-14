# 그래프를 딕셔너리로 표현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

# DFS 함수 정의
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # 방문한 노드를 저장할 집합 생성
    
    visited.add(start)  # 현재 노드를 방문 처리
    print(start)  # 방문한 노드를 출력

    # 현재 노드와 연결된 다른 노드들을 재귀적으로 방문
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 시작 노드를 'A'로 하여 DFS 실행
dfs(graph, 'A')

