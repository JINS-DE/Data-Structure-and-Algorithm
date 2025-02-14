def combi(n,weight):
    global answer

    if weight<500:

        return
    if N==n:
        answer+=1
        return
    for i in range(N):

        if v[i]==0:
            v[i]=1
            combi(n+1,weight+kit[i]-K)
            v[i]=0

import sys
input = sys.stdin.readline
N,K=map(int,input().split())
kit = list(map(int,input().split()))
v=[0]*N
answer=0
combi(0,500)
print(answer)