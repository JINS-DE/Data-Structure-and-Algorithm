arr = [] 
for _ in range(9):
    arr.append(list(map(int,input().strip())))

zero_li = []
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            zero_li.append((i,j))
def is_possible(r,c,num):
    for i in range(9):
        if arr[r][i]==num:
            return False
        if arr[i][c]==num:
            return False
    nr = (r//3)*3
    nc = (c//3)*3

    for dr in range(3):
        for dc in range(3):
            if arr[nr+dr][nc+dc] == num:
                return False
    return True
    
def dfs(idx):
    if idx == len(zero_li):
        for row in arr:
            print(*row,sep='')
        exit(0)

    r,c = zero_li[idx]
    for i in range(1,10):
        if is_possible(r,c,i):
            arr[r][c] = i
            dfs(idx+1)
            arr[r][c] = 0
dfs(0)