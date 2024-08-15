import sys
input = sys.stdin.readline

N = int(input())
result = 0
columns = [0] * N  # 퀸이 놓일 수 있는 열을 추적
diagonal1 = [0] * (2 * N - 1)  # / 방향 대각선
diagonal2 = [0] * (2 * N - 1)  # \ 방향 대각선

def n_queens(row):
    global result
    if row == N:
        result += 1
        return
    for col in range(N):
        if columns[col] or diagonal1[row + col] or diagonal2[row - col + N - 1]:
            continue
        columns[col] = diagonal1[row + col] = diagonal2[row - col + N - 1] = 1
        n_queens(row + 1)
        columns[col] = diagonal1[row + col] = diagonal2[row - col + N - 1] = 0

n_queens(0)
print(result)