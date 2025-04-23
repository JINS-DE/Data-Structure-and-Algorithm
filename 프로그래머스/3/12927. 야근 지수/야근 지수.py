from heapq import heapify, heappop,heappush

def solution(n, works):
    answer = 0
    heap=[]
    for work in works:
        heappush(heap,-work)
    
    for _ in range(n):
        x=-heappop(heap)
        x-=1
        if x<0:
            break
        heappush(heap,-x)

    
    for h in heap:
        h=-h
        answer+=h*h
        
    return answer 