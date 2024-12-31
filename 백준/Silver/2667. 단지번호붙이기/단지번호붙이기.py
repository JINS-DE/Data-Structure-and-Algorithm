import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

# 방향 벡터 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]
result = []

def dfs(x, y):
    count = 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 조건 수정: nx, ny의 방문 여부와 그래프 값 확인
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
            count += dfs(nx, ny)
    return count

# 모든 좌표를 탐색하며 단지 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(dfs(i, j))

# 결과 출력
print(len(result)) 
for count in sorted(result):  
    print(count)
