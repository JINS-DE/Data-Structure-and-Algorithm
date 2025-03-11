def dfs(node,cnt):
    global answer
    if node==num2:
        answer=cnt
        return

    for next in adj[node]:
        if v[next]==0:
            v[next]=1
            dfs(next,cnt+1)



import sys
input = sys.stdin.readline
n=int(input())
num1, num2 = map(int,input().split())
m=int(input())

adj=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

v=[0]*(n+1)
answer=-1
dfs(num1,0)

print(answer)