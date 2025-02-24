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
        
        if new_start >= heap[0]:
            heapq.heappop(heap)
        else:
            answer+=1
            
        heapq.heappush(heap,arr[idx][1])

    return answer