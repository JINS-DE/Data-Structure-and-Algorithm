'''
과제 
- 소요 시간 di일
- 마감 기한 ti일
'''

import sys
input = sys.stdin.readline
n=int(input())
li=[]
for i in range(n):
    d,t=map(int,input().split())
    li.append((d,t))

# 마감 날짜 내림차순 정렬
li.sort(key=lambda x :x[1], reverse=True)

# 마지막 과제 무조건 해야 하는 날에 하고 남는 날 
d_day= li[0][1]-li[0][0]

for i in range(1,n):
    if li[i][1] < d_day:
        # 남은 날 앞으로 땡겨 주기
        d_day = li[i][1] - li[i][0]
    else:
        d_day = d_day-li[i][0]

print(d_day)
