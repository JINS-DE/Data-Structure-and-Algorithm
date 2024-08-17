import sys
import heapq
input=sys.stdin.readline
n=int(input())
left=[]
right=[]
for i in range(n):
    x=int(input())
    if len(left)<=len(right):
        heapq.heappush(left,-x)
    else:
        heapq.heappush(right,x)
    
    if right and -left[0] > right[0]:
        max_heap = -heapq.heappop(left)
        min_heap = heapq.heappop(right)        
        heapq.heappush(left,-min_heap)
        heapq.heappush(right,max_heap)
    elif len(left)<len(right):
        heapq.heappush(left,-heapq.heappop(right[0]))
    print(-left[0])