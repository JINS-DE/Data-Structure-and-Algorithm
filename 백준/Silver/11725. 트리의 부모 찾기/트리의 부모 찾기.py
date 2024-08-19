import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 호출 한도를 늘려줍니다.
n=int(input())
# 인접 리스트 만들기
li = [[] for _ in range(n + 1)]
for i in range(n - 1):
    start, end = map(int, input().split())
    li[start].append(end)
    li[end].append(start)

# 각 노드의 부모를 저장할 배열
parent = [0] * (n + 1)

# DFS로 부모 찾기
def dfs(node):
    for child in li[node]:  # 현재 노드에 연결된 모든 자식 노드를 탐색
        if parent[child] == 0:  # 자식 노드가 아직 부모가 지정되지 않았다면
            parent[child] = node  # 현재 노드를 자식 노드의 부모로 설정
            dfs(child)  # 자식 노드에 대해 재귀 호출

# 루트 노드는 1번 노드로 설정하고 시작
dfs(1)

# 2번 노드부터 n번 노드까지의 부모를 출력
for i in range(2, n + 1):
    print(parent[i])






