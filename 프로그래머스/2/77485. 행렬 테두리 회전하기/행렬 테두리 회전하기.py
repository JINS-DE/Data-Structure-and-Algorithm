def solution(rows, columns, queries):
    answer = []
    board=[[i*columns+j for j in range(1,columns+1)] for i in range(rows)]
    def turn(x1,y1,x2,y2):
        before=board[x1-1][y1-1]
        min_ = rows*columns
        # 맨위 좌->우 
        for y in range(y1-1,y2):
            tmp=board[x1-1][y]
            board[x1-1][y]=before
            before = tmp
            min_=min(min_,before)
            
        #오른쪽 위->아래
        for x in range(x1,x2):
            tmp=board[x][y2-1]
            board[x][y2-1]=before
            before = tmp
            min_=min(min_,before)
            
        # 아래 우->좌
        for y in range(y2-2,y1-2,-1):
            tmp=board[x2-1][y]
            board[x2-1][y]=before
            before = tmp
            min_=min(min_,before)
        # 왼쪽 아래->위
        for x in range(x2-2,x1-2,-1):
            tmp=board[x][y1-1]
            board[x][y1-1]=before
            before = tmp
            min_=min(min_,before)
        return min_
    
    for querie in queries:
        x1,y1,x2,y2 = querie
        answer.append(turn(x1,y1,x2,y2))

    
    
            
    return answer