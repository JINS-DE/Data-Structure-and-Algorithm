import sys
input = sys.stdin.readline
N,C = map(int,input().split())
li=[int(input()) for _ in range(N)]
start, end = 1, max(li)

while start<=end:
    mid = (start+end)//2
    lan_cnt=0
    for i in li:
        lan_cnt+=i//mid
    if lan_cnt>=C:
        start=mid+1
    else:
        end=mid-1
print(end)