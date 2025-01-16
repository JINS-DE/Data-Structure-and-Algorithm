'''
1. 0의 개수가 k개 보다 많으면 못킴
2. 0의 개수가 짝수면 k도 짝수 0의 개수가 홀수면 k도 홀수
3. 한행의 모든 램프를 킬 수 있으면 똑같이 생긴 다른 행도 킬 수 있으므로 똑같은 값을 가진
행들의 개수를 구함함
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [input().strip() for _ in range(n)]
k=int(input())
answer = defaultdict(int)

for i in range(n):
    count_0 = arr[i].count('0')
    if count_0 <= k and count_0%2 == k%2:
        answer[arr[i]]+=1
max_ = 0 

for i,j in answer.items():
    max_ = max(max_,j)
print(max_)