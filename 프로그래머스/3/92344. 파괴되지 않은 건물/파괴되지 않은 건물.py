def solution(board, skill):
    answer = 0
    N=len(board)
    M=len(board[0])
    prefix = [[0]*(M+1) for _ in range(N+1)]
    for type_, r1, c1, r2, c2, degree in skill:
        if type_ == 1: 
            degree=-degree
        
        prefix[r1][c1]+=degree
        prefix[r1][c2+1]-=degree
        prefix[r2+1][c1]-=degree
        prefix[r2+1][c2+1]+=degree
    
    for col in range(M+1):
        for row in range(1,N+1):
            prefix[row][col]=prefix[row-1][col]+prefix[row][col]
    
    for row in range(N+1):
        for col in range(1,M+1):
            prefix[row][col]=prefix[row][col-1]+prefix[row][col]
    
    for row in range(N):
        for col in range(M):
            board[row][col] += prefix[row][col]
    
    for row in range(N):
        for col in range(M):
            if board[row][col]>0:
                answer+=1
    
    
        
        
            
    return answer