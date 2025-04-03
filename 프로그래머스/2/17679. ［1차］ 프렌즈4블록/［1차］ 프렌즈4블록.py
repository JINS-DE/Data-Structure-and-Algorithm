def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    def find_4block():
        remove_lst = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]=="":
                    continue
                if board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]:
                    remove_lst.add((i,j))
                    remove_lst.add((i+1,j))
                    remove_lst.add((i,j+1))
                    remove_lst.add((i+1,j+1))
        return remove_lst
    
    remove_lst = find_4block()
    
    while remove_lst:
        answer+=len(remove_lst)
        
        # 4블록 제거
        for i,j in remove_lst:
            board[i][j]=''
        
        # 블록 아래로 내리기
        for col in range(n):
            top,buttom=m-1,m-1
            while top >=0:
                if board[top][col]!='' and board[buttom][col]!='':
                    top-=1
                    buttom-=1
                elif board[top][col]==board[buttom][col]=='':
                    top-=1
                else:
                    board[top][col],board[buttom][col] = board[buttom][col], board[top][col]
                    top-=1
                    buttom-=1
        
        # 다시 4블록 확인
        remove_lst=find_4block()
    
    
    return answer