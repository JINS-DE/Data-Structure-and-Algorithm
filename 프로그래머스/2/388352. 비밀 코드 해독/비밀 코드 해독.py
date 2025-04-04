from itertools import combinations

def solution(n, q, ans):
    answer=0
    def possible_code(c):
        for i in range(len(q)):
            cnt=0
            for j in c:
                if j in q[i]:
                    cnt+=1
            if cnt != ans[i]:
                return False
        return True
            
    for code in combinations(range(1,n+1),5):
        if possible_code(code):
            answer+=1

    return answer