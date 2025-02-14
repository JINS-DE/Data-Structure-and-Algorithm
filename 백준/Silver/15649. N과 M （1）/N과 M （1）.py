def dfs(depth,li):
    if depth==m:
        answer.append(li)
        return
    for i in range(1,n+1):
        if visited[i]==0:
            visited[i]=1
            dfs(depth+1,li+[i])
            visited[i]=0
            


n,m = map(int,input().split())
answer=[]
visited =[0]*(n+1)
dfs(0,[])

for lst in answer:
    print(*lst)