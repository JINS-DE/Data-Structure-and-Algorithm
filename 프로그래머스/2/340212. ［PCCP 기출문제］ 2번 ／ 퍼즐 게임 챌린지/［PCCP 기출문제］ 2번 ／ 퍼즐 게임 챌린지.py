def total_time(diffs,times,level):
    time=0
    for i in range(len(diffs)):
        if diffs[i] > level:
            wrong = diffs[i]-level
            time += (times[i]+times[i-1])*wrong + times[i]
        else:
            time += times[i]  
            
    return time

def solution(diffs, times, limit):
    answer = 0
    
    start = 1
    end = max(diffs)-1
    while start<=end:
        mid = (start+end)//2
        print("mid:",mid)
        time = total_time(diffs,times,mid)
        print(time)
        if time > limit:
            start = mid+1
        elif time <= limit:
            end = mid-1
    answer = start
    return answer