N,M = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
answer=[]
v=[0]*N
def dfs(n,lst,s):
    if n==M:
        answer.append(lst)
        return
    prev=None
    for i in range(s,N):
        if v[i]==0 and prev!=arr[i]:
            prev=arr[i]
            v[i]=1
            dfs(n+1,lst+[arr[i]],i+1)
            v[i]=0
    
dfs(0,[],0)


for i in answer:
    print(*i)