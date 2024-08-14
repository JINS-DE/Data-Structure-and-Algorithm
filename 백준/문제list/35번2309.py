# 아홉 난쟁이의 키가 주어졌을 때, 일곱 난쟁이들의 키의 합이 100이 됨을 이용하여 프로그램 작성
# a=[20,7,23,19,10,15,25,8,13]

# 조합문제임 조합으로 해결하면 쉬움
import sys
from itertools import combinations
input=sys.stdin.readline
a=[int(input()) for _ in range(9)]
# for i in combinations(a,7):
#     if sum(i)==100:
#         for j in sorted(i):
#             print(j)
#         break

# 완전 탐색으로 풀어보자
a=[20,7,23,19,10,15,25,8,13]
tmp=[]
def dfs(depth,start):
    if depth==7:
        if sum(tmp)==100:
            for j in sorted(tmp): 
                print(j)
            sys.exit() # 함수 나가기
        return
    for i in range(start,len(a)):
        tmp.append(a[i])
        dfs(depth+1,i+1)
        tmp.pop()
dfs(0,0)
