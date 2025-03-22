import sys
input = sys.stdin.readline
n=int(input())
photo = [list(map(int,input().strip())) for _ in range(n)]

def devide_conquer(r,c,n):
    global answer
    color = photo[r][c]
    st='('
    for i in range(r,r+n):
        for j in range(c,c+n):
            if photo[i][j] != color:
                st+=devide_conquer(r,c,n//2)
                st+=devide_conquer(r,c+n//2,n//2)
                st+=devide_conquer(r+n//2,c,n//2)
                st+=devide_conquer(r+n//2,c+n//2,n//2)
                return st+')'
    if color:
        return '1'
    else:
        return '0'
    

print(devide_conquer(0,0,n))
