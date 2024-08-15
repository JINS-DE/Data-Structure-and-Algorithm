import sys
input=sys.stdin.readline
N=int(input())
a=list(map(int,input().split()))
tmp=[0]*N
visited=[0]*N
result=[]

def dfs(depth):
    if depth==N:
        result.append(diff_sum(tmp))
        return 
    for i in range(N):
        if visited[i]==0:
            visited[i]=1
            tmp[depth]=a[i]
            dfs(depth+1)
            visited[i]=0
def diff_sum(a):
    total_sum =0
    for i in range(1,N):
        total_sum += abs(a[i]-a[i-1])
    return total_sum
dfs(0)
print(max(result))
