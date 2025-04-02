def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    def remove_block():
        result = set()
        # 4블록 제거
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]=='':
                    continue
                if board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]:
                    result.add((i,j))
                    result.add((i+1,j))
                    result.add((i,j+1))
                    result.add((i+1,j+1))
        return result
        
    remove_set = remove_block()
    while remove_set:
        answer+=len(remove_set)
        for i,j in remove_set:
            board[i][j]=''
        for col in range(n):
            top, buttom = m-1, m-1
            while top>=0:
                if board[top][col]!='' and board[buttom][col]!='':
                    top-=1
                    buttom-=1
                elif board[top][col]=='' and board[buttom][col]=='':
                    top-=1
                else:
                    board[top][col], board[buttom][col] = board[buttom][col], board[top][col]
                    top-=1
                    buttom-=1
                
        remove_set = remove_block()
    
    
    
    return answer