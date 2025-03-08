N,M = map(int,input().split())

answer=[]
def dfs(n,lst):
    if n == N+1:
        if len(lst)==M:
            answer.append(lst)
        return
    dfs(n+1,lst+[n])
    dfs(n+1,lst)


        
dfs(1,[])

for i in answer:
    print(*i)