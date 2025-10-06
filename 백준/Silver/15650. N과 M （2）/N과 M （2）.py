import sys
input = sys.stdin.readline
N, M = map(int,input().split())
def dfs(n,st):
    if n>N:
        if len(st)==M:
            print(" ".join(st))
        return
    dfs(n+1,st+f"{n}")
    dfs(n+1,st)

dfs(1,"")