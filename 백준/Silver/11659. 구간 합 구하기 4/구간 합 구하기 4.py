import sys
input = sys.stdin.readline
n,m = map(int,input().split())
li = list(map(int,input().split()))

prefix = [0]*n
for i,v in enumerate(li):
    if i==0:
        prefix[i]+=v
    else:
        prefix[i]+=prefix[i-1]+v

for t in range(m):
    i,j = map(int,input().split())
    if i==1:
        print(prefix[j-1])
    else:
        print(prefix[j-1]-prefix[i-2])