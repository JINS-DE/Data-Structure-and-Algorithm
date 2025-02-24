import heapq 
def solution(book_time):
    arr=[]
    for time in book_time:
        inr, out = time
        ih,im = map(int,inr.split(':'))
        oh,om = map(int,out.split(':'))
        arr.append([ih*60+im,oh*60+om+10])
    arr.sort()
    print("arr:",arr)
    answer=1
    heap = []
    heapq.heappush(heap,arr[0][1])
    
    for idx in range(1,len(arr)):
        new_start = arr[idx][0]
        tmp=[]
        
        finished_time=heapq.heappop(heap)
        if new_start >= finished_time:
            heapq.heappush(heap,arr[idx][1])
        else:
            heapq.heappush(heap,finished_time)
            heapq.heappush(heap,arr[idx][1])
        answer = max(answer,len(heap))
    return answer