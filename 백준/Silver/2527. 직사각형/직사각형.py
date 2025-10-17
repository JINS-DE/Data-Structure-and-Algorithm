import sys
input = sys.stdin.readline
"""
접점을 기준으로 계산
x 축에서 접점이 0개 1개 무한대
y 축에서 접점이 0개 1개 무한대 

표로 나타내면
    0 1 inf
0   d d d
1   d c b
inf d b a
"""
answer = [
    ['d','d','d'],
    ['d','c','b'],
    ['d','b','a']
          ]
for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
    
    # x축 교차 판정
    if p1 < x2 or p2 < x1:
        x_intersec = 0
    elif p1 == x2 or p2 == x1:
        x_intersec = 1
    else:
        x_intersec = 2

    # y축 교차 판정
    if q1 < y2 or q2 < y1:
        y_intersec = 0
    elif q1 == y2 or q2 == y1:
        y_intersec = 1
    else:
        y_intersec = 2
    
    print(answer[x_intersec][y_intersec])