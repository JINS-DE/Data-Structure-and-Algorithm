import sys
import heapq
input=sys.stdin.readline
n=int(input())
tmp=[]
for _ in range(n):
    x=int(input())
    heapq.heappush(tmp,x)
    
answer=0

while len(tmp)>1:
    a=heapq.heappop(tmp)
    b=heapq.heappop(tmp)
    sum=a+b
    answer+=sum
    heapq.heappush(tmp,sum)

print(answer)