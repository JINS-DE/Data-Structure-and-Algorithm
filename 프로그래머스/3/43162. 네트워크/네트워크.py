def solution(n, computers):
    answer = 0
    visited = [0]*n
    def dfs(node):
        visited[node]=1
        for i in range(n):
            if computers[node][i]==1 and i!=node and visited[i]==0:
                dfs(i)
        return
    for i in range(n):
        if visited[i]==0:
            dfs(i)
            answer+=1
    return answer