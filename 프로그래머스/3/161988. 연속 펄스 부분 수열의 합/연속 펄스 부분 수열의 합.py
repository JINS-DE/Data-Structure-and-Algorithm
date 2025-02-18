def solution(sequence):
    n=len(sequence)
    
    # 1, -1, 1 일 때
    dp1=[0] * n
    dp1[0] = sequence[0]
    for i in range(1,n):
        if i%2==0:
            dp1[i]=max(dp1[i-1]+sequence[i], sequence[i])
        else:
            dp1[i]=max(dp1[i-1]-sequence[i], -sequence[i])
    
    # -1, 1, -1 일 때
    dp2=[0] * n
    dp2[0] = -sequence[0]
    for i in range(1,n):
        if i%2==0:
            dp2[i]=max(dp2[i-1]-sequence[i], -sequence[i])
        else:
            dp2[i]=max(dp2[i-1]+sequence[i], sequence[i])
    answer=max(max(dp1),max(dp2))
    
    return answer