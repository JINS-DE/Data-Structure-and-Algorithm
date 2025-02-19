def solution(scores):
    answer=1
    whanho_score = sum(scores[0])
    whanho_a = scores[0][0]
    whanho_b = scores[0][1]
    scores.sort(key=lambda x : (-x[0], x[1]))
    
    max_b=0
    for a,b in scores:
        if whanho_a < a and whanho_b < b:
            return -1
        if b >= max_b:
            max_b = b
            if a+b > whanho_score:
                answer+=1
                
    return answer