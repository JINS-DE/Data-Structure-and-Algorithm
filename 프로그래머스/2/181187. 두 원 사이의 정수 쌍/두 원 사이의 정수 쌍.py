def solution(r1, r2):
    answer=0
    for i in range(1,r2+1):
        r1_max = int((r1*r1-i*i-1)**0.5) if r1>i else -1
        r2_max = int((r2*r2-i*i)**0.5)
        answer+=r2_max-r1_max
        
    return answer*4