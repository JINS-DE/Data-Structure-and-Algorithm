n,m = map(int,input().split())
answer = []
v = [0]*(n+1)
def dfs(depth,li):
    if depth==m:
        answer.append(li)
        return
    for i in range(1,n+1):
        if v[i]==0:
            v[i]=1
            dfs(depth+1,li+[i])
            v[i]=0
    
dfs(0,[])

for i in answer:
    print(*i)