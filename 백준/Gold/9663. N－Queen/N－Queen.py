n=int(input())
answer=0
v1=[0]*n
v2=[0]*(2*n)
v3=[0]*(2*n)

def N_Queen(row):
    global answer
    if row == n:
        answer+=1
        return
    for col in range(n):
        if v1[col]== v2[row+col] == v3[row-col]==0:
            v1[col]= v2[row+col]=v3[row-col]=1
            N_Queen(row+1)
            v1[col]= v2[row+col]=v3[row-col]=0
N_Queen(0)
print(answer)
