import sys
input = sys.stdin.readline
board=[]
for _ in range(9):
    board.append(list(map(int,input().strip())))

zero_li = []
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            zero_li.append((i,j))

def is_right(r,c,num):
    for i in range(9):
        if board[i][c]==num:
            return False
        if board[r][i]==num:
            return False
    r=(r//3)*3
    c=(c//3)*3
    for i in range(3):
        for j in range(3):
            if board[r+i][c+j]==num:
                return False

    return True

def dfs(idx):
    
    if idx == len(zero_li):
        for i in board:
            print(*i,sep="")
        sys.exit(0)

    r,c=zero_li[idx]

    for i in range(1,10):
        
        if is_right(r,c,i):
            board[r][c]=i
            dfs(idx+1)
            board[r][c]=0
            
            

dfs(0)
