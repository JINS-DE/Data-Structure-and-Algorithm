'''
양쪽이 대칭이 되는 팰린드롬을 만들어야 한다.
* 해결방안
- 자기 자신은 팰린드롬이다.
- 거리가 1인 바로 옆에 있는 인덱스가 같으면 팰린드롬이다.
    ex) 11 , 22, 33 
- 거리가 2이상 팰린드롬은 양쪽(left,right)가 같을 때 그 안에(left+1, right-1)가 팰린드롬이면 팰린드롬이다.
'''

import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
M = int(input())
Q = [list(map(int, input().split())) for _ in range(M)]

dp = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(i,N):
        right=j
        left=j-i
        # dp초기화 : i가 0일 때는 자기 자신임으로 True, i가 1일 때는 left,right가 같으면 True
        if i==0 or (i==1 and li[left]==li[right]):
            dp[left][right]=True
            continue
        # i가 2이상인 경우(거리가 2이상), 예) 1 2 1, 1 2 3 2 1 
        # left,right가 같을 때 사이 안에 내용이 팰린드롬이면 팰린드롬이다. 
        if li[left]==li[right] and dp[left+1][right-1]:
            dp[left][right]=True

for area in Q:
    left, right = area[0]-1, area[1]-1
    print(1 if dp[left][right] else 0)