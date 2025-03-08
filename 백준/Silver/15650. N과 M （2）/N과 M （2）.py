N,M = map(int,input().split())

answer=[]
def dfs(depth,lst,k):
    if depth==M:
        answer.append(lst)
        return
    for i in range(k,N+1):
        dfs(depth+1,lst+[i],i+1)


        
dfs(0,[],1)

for i in answer:
    print(*i)