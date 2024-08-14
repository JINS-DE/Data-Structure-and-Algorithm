import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
# a=[5,2,3,1,4,2,3,5,1,7]
cnt=[0]*(10000+1)
for i in range(n):
    cnt[int(input())]+=1

for i in range(1,len(cnt)):
    if cnt[i]!=0:
        for _ in range(cnt[i]):
            print(i)
