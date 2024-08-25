import sys
input=sys.stdin.readline
N,K=map(int,input().split())
li=[int(input()) for _ in range(N)]
cnt=0
for i in range(N-1,-1,-1):
    if li[i]<=K:
        cnt+=K//li[i]
        K%=li[i]

print(cnt)