import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
def dfs(depth,st):
    if depth==M:
        print(" ".join(map(str,st)))
        return
    
    for i in range(N):
        dfs(depth+1,st+[lst[i]])

dfs(0,[])