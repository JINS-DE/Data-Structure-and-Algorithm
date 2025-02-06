def solution(land):
    def dfs(r, c, group):
        stack = [(r, c)]
        visited[r][c] = group
        cnt = 1  # 현재 그룹의 크기
        
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx, ny = x + dr[i], y + dc[i]
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = group
                    stack.append((nx, ny))
                    cnt += 1
        return cnt

    n, m = len(land), len(land[0])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    visited = [[0] * m for _ in range(n)]
    oil_amount = {}
    
    group = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                oil_amount[group] = dfs(i, j, group)
                group += 1
    
    max_oil = 0
    for i in range(m):  # 각 세로줄 탐색
        groups = {visited[j][i] for j in range(n) if visited[j][i] != 0}  # 중복 제거한 그룹
        max_oil = max(max_oil, sum(oil_amount[g] for g in groups))
    
    return max_oil


