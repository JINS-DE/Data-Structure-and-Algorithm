# 첫째 줄에는 잘라진 하얀색 색종이의 개수를 출력
# 둘째 줄에는 파란색 색종이 개수 출력
import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def count_colors(x,y,n):
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                # 1사분면 확인
                count_colors(x,y,n//2)
                # 2사분면 확인
                count_colors(x+n//2,y,n//2)
                # 3사분면 확인
                count_colors(x,y+n//2,n//2)
                # 4사분면 확인
                count_colors(x+n//2,y+n//2,n//2)
                return
    if color ==0:
        result.append(0)
    else:
        result.append(1)
count_colors(0,0,n)


print(result.count(0))
print(result.count(1))