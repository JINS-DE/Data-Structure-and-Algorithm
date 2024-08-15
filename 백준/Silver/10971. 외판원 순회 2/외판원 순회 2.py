import sys
input = sys.stdin.readline
n=int(input())
# n개의 비용(도시 i->j로 가기위한 비용)
graph = [list(map(int, input().split())) for _ in range(n)]
min_cost = float('inf') # 최소 비용 저장하는 변수 초기값 무한대
visited = [False]*n  # 방문 여부
# n = 4  # 도시의 수
# graph = [
#     [0, 10, 15, 20],
#     [5, 0, 9, 10],
#     [6, 13, 0, 12],
#     [8, 8, 9, 0]
# ]

def dfs(current, cost, depth):
    global min_cost
    
    if depth==n: #모든 도시 방문
        if graph[current][0] > 0:
            min_cost = min(min_cost, cost+graph[current][0])
        return
    
    for next in range(n):
        if not visited[next] and graph[current][next] > 0:
            visited[next] = True
            dfs(next, cost + graph[current][next], depth + 1)
            visited[next] = False

visited[0] = True
dfs(0,0,1)
print(min_cost)
