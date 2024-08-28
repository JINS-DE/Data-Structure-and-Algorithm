import sys
input=sys.stdin.readline

N=int(input())
P=list(map(int,input().split()))
P.sort()
answer=0

for i in range(N):
    for j in range(i+1):
        answer+=P[j]
print(answer)
