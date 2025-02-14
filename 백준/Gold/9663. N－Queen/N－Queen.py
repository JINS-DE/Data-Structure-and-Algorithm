def Nqueen(row):
    global answer
    if N==row:
        answer+=1
        return
    
    for col in range(N):
        if v1[col] == v2[row+col] == v3[row-col]==0:
            v1[col]= v2[row+col]= v3[row-col]=1
            Nqueen(row+1)
            v1[col]= v2[row+col]= v3[row-col]=0
answer=0
N=int(input())
v1 = [0]*N
v2 = [0]*(2*N)
v3 = [0]*(2*N)
Nqueen(0)
print(answer)