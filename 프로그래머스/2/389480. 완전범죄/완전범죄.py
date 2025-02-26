def solution(info, n, m):
    length = len(info)
    # dp[i][a][b] : info[i] 사용했을 때 a의 누적 흔적, b의 누적 흔적
    dp=[[[False]*m for _ in range(n)] for _ in range(length+1)]
    dp[0][0][0] = True
    
    for i in range(length):
        a_cost, b_cost = info[i]
        for a in range(n):
            for b in range(m):
                if dp[i][a][b]:
                    # a가 훔칠 때
                    na=a+a_cost
                    nb=b
                    if na<n:
                        dp[i+1][na][nb]=True
                    
                    # b가 훔칠 때
                    na=a
                    nb=b+b_cost
                    if nb<m:
                        dp[i+1][na][nb]=True

    answer=-1
    for a in range(n):
        for b in range(m):
            if dp[length][a][b]:
                if answer==-1 or a<answer:
                    answer=a
    return answer