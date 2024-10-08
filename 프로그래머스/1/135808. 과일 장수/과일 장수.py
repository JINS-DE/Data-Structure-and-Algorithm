def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        answer+=min(score[i*m:i*m+m])*m
        
    return answer