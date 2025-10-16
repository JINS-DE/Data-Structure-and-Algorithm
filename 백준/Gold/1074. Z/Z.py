import sys
sys.setrecursionlimit(1000000)
N,r,c = map(int,sys.stdin.readline().split())

def z(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    if r < half and c < half:  # 왼쪽 위
        return z(n - 1, r, c)
    elif r < half and c >= half:  # 오른쪽 위
        return half * half + z(n - 1, r, c - half)
    elif r >= half and c < half:  # 왼쪽 아래
        return 2 * half * half + z(n - 1, r - half, c)
    else:  # 오른쪽 아래
        return 3 * half * half + z(n - 1, r - half, c - half)

    

ans = z(N,r,c)
print(ans)