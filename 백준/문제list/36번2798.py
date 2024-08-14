'''
카드의 합이 21이 넘지 않는 한도 내에서 카드의 합을 최대한 크게 만드는 게임이다.
각 카드의 양의 정수 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
딜러는 M의 숫자를 외치면 제한된 시간 안에 N장의 카드 중에 3장의 카드를 골라야 한다.
M을 넘지않으면서 M과 최대한 가깝게 만들어야 한다. 

N장의 카드가 주어졌을 때 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구하기
'''
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
a=list(map(int,input().split()))

tmp=[0]*3
sum_li=[]

def dfs(depth,start):
    if depth==3:
        sum_li.append(sum(tmp))
        return
    else:
        for i in range(start,len(a)):
            tmp[depth]=a[i]
            dfs(depth+1,i+1)
dfs(0,0)

closest =None
for i in sum_li:
    if i <= M:
        if closest is None or i > closest:
            closest = i
print(closest)
