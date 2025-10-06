
import sys
input = sys.stdin.readline
N, M = map(int,input().split())

def dfs(depth,st):
    if depth==M:
        print(" ".join(st))
        return
    
    for i in range(1,N+1):
        dfs(depth+1,st+f"{i}")

dfs(0,"")