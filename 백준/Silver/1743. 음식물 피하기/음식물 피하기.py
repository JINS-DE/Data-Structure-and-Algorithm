import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N,M,K = map(int,input().split())
board =[[0]*M for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

answer=0
def dfs(r,c):
    size = 1
    for i in range(4):
        nr = dr[i]+r
        nc = dc[i]+c
        if 0<=nr<N and 0<=nc<M and board[nr][nc]==1:
            board[nr][nc]=0
            size+=dfs(nr,nc)
    return size
    
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            board[i][j]=0
            answer=max(answer,dfs(i,j))
print(answer)