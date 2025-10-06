import sys
input = sys.stdin.readline
N, M = map(int,input().split())

def dfs(depth,idx,lst):
    if depth==M:
        print(" ".join(map(str,lst)))
        return
    
    for i in range(idx,N+1):
        dfs(depth+1,i+1,lst+[i])
    
dfs(0,1,[])