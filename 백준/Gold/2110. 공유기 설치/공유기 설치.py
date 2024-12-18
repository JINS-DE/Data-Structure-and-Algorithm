import sys
input = sys.stdin.readline
N,C = map(int,input().split())
li=sorted([int(input()) for _ in range(N)])
start,end=1,li[-1]-li[0]
answer = 0

if C==2:
    print(li[-1]-li[0])
else:
    while(start<end):
        mid = (start+end)//2
        count = 1
        ts = li[0]
        
        for i in range(N):
            if li[i]-ts>=mid:
                count+=1
                ts=li[i]
        if count >= C:
            answer = mid
            start = mid + 1
        else:
            end = mid
    print(answer)