import sys
input = sys.stdin.readline
N,M=map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer=[]
def dfs(n,lst):
    if n==M:
        answer.append(lst)
        return
    prev=100001
    for i in range(N):
        if arr[i]==prev:
            continue
        else:
            prev=arr[i]
            dfs(n+1,lst+[arr[i]])


dfs(0,[])

for i in answer:
    print(*i)