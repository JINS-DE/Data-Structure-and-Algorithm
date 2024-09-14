import sys,heapq
input=sys.stdin.readline

n,m=map(int,input().split())
heap=[]

for i in map(int,input().split()):
    heapq.heappush(heap,-i)

want_count=list(map(int,input().split()))

for i in want_count:
    box = -(heapq.heappop(heap))
    remain = box-i
    if remain<0:
        break
    heapq.heappush(heap,-remain)

if remain < 0 :
    print(0)
else:
    print(1)
    