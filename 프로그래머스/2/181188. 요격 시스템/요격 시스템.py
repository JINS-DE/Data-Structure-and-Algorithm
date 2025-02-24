def solution(targets):
    answer = 0 
    targets.sort(key=lambda x : x[1])
    tmp=0
    for s,e in targets:
        if tmp <= s :
            tmp = e
            answer+=1
        
    
    return answer 