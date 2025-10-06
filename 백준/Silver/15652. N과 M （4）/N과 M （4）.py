
import sys
input = sys.stdin.readline
N, M = map(int,input().split())

def dfs(start,depth,st):
    if depth==M:
        print(" ".join(st))
        return
    
    for i in range(start,N+1):
        dfs(i,depth+1,st+f"{i}")

dfs(1,0,"")
