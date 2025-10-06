import sys
input = sys.stdin.readline
N, M = map(int,input().split())
visited = [0]*(N+1)
def dfs(depth,lst):
    if depth==M:
        print(" ".join(map(str,lst)))
        return
    
    for i in range(1,N+1):
        if visited[i]:
            continue
        visited[i]=1
        dfs(depth+1,lst+[i])
        visited[i]=0
dfs(0,[])