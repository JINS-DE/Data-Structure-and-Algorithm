def solution(queue1, queue2):    
    sum1=sum(queue1)
    sum2=sum(queue2)
    
    arr = queue1+queue2
    
    p1=0
    p2=len(queue1)
    
    if (sum1+sum2)%2 != 0 :
        return -1
    goal=sum1+sum2//2
    
    answer = 0
    while True:
        if answer==4*len(queue1):
            return -1
        
        if sum1>sum2:
            sum1-=arr[p1]
            sum2+=arr[p1]
            p1+=1
        elif sum1<sum2:
            sum1+=arr[p2]
            sum2-=arr[p2]
            p2+=1
        else:
            return answer
        if p1>=len(arr):
            p1=0
        elif p2>=len(arr):
            p2=0
        answer+=1
    
    return answer