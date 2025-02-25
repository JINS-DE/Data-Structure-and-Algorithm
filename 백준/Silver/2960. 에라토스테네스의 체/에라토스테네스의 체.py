import sys
n,k = map(int,sys.stdin.readline().split())
visited=[False,False]+[True]*(n-1)
cnt=0
for i in range(2,n+1):
    
    if visited[i]:
        for j in range(i,n+1,i):
            if visited[j]:
                cnt+=1
                visited[j]=False
            if cnt==k:
                print(j)
                break