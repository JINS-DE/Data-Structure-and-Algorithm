N=int(input())
col_visited=[0]*N
r_slice_visited = [0]*(2*N-1)
l_slice_visited = [0]*(2*N-1)
answer=0
def dfs(row):
    global answer
    if row == N:
        answer+=1
        return
    for col in range(N):
        if col_visited[col]==0 and r_slice_visited[row+col]==0 and l_slice_visited[row-col]==0:
            col_visited[col]= r_slice_visited[row+col]=l_slice_visited[row-col]=1
            dfs(row+1)
            col_visited[col]= r_slice_visited[row+col]=l_slice_visited[row-col]=0
dfs(0)

print(answer)