def solution(n, s):
    if s//n==0:
        return [-1]
    answer=[]
    for i in range(n,0,-1):
        tmp=s//i
        answer.append(tmp)
        s-=tmp
    return answer