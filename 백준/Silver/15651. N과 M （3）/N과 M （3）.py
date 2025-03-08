N,M = map(int,input().split())

answer=[]
def dfs(depth,lst):
    if depth==M:
        answer.append(lst)
        return
    for i in range(1,N+1):
        dfs(depth+1,lst+[i])


        
dfs(0,[])

for i in answer:
    print(*i)
