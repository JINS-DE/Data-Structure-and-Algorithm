'''
N퀸의 해결책 Think
1. 우리는 row에 Queen을 한 개 씩만 놓는다. 
2. 위치 적합성을 판단한다. (같은 열이나 대각선에 있는지)
3. 종료 조건( 모든 row에 퀸을 놓았을 때) if row == N 
'''

# gpt 형님의 정답 코드
import sys
input = sys.stdin.readline

N = int(input())
count = 0  # 가능한 경우의 수를 세기 위한 변수

# 각 열, 대각선에 퀸이 있는지를 추적하는 배열
columns = [0] * N
# '/' 대각선의 위치를 추적하는 배열, row+col 값이 같은 위치
diagonal1 = [0] * (2 * N - 1)
# '\' 대각선의 위치를 추적하는 배열, row-col 값이 같은 위치
diagonal2 = [0] * (2 * N - 1)

def n_queens(row):
    global count
    if row == N:
        count += 1  # 가능한 경우의 수를 증가
        return
    for col in range(N):
        if columns[col] or diagonal1[row + col] or diagonal2[row - col + N - 1]:
            continue  # 이 위치에 퀸을 놓을 수 없으면 다음 열로 이동
        # 퀸을 놓는 경우
        columns[col] = diagonal1[row + col] = diagonal2[row - col + N - 1] = 1
        n_queens(row + 1)  # 다음 행으로 이동
        # 퀸을 제거하고 백트래킹
        columns[col] = diagonal1[row + col] = diagonal2[row - col + N - 1] = 0
    # 질문?!
        # diagonal2[row - col + N - 1] 의 의미는??
        # row-col 의 범위는 음수(-(N-1))부터 양수(N-1)까지이다.
        # 인덱싱 처리를 하기 위해 N-1을 더해줘 양수화로 만들어 diagonal2를 탐색 한다.
n_queens(0)
print(count)


# 시간 초과 코드
import sys
input=sys.stdin.readline
N=int(input())
board=[-1]*N # 퀸의 위치를 저장하는 배열 (행: 인덱스, 열: 값)
sol=[] # 퀸의 위치를 담는 배열
def is_safe(row,col):
    for i in range(row):
        # 같은 열에 퀸이 있는지 확인
        if board[i]==col:
            return False
        # 같은 대각선 위치에 있는지 확인
        elif abs(board[i]-col)==abs(i-row):
            return False
    return True

def n_queens(row):
    if row==N:
        sol.append(board[:])
        return 
    for col in range(N):
        if is_safe(row,col):
            board[row]=col
            n_queens(row+1)
            board[row]=-1
n_queens(0)
print(len(sol))

# N 퀸의 기본 공식
def is_safe(board, row, col, N):
    for i in range(row):
        # 같은 열에 퀸이 있는지 확인
        if board[i]==col:
            return False
        elif abs(board[i]-col)==abs(i-row):
            return False
    return True

def solve_n_queens(board, row, N, solutions):
    if row == N:  # 모든 행에 퀸을 다 놓았다면
        solutions.append(board[:])  # 현재 배치를 저장
        return
    
    for col in range(N):  # 현재 행에서 가능한 열들을 시도
        if is_safe(board, row, col, N):
            board[row] = col  # 퀸을 배치
            solve_n_queens(board, row + 1, N, solutions)  # 다음 행으로 이동
            board[row] = -1  # 백트래킹: 현재 행에서 퀸을 제거

def n_queens(N):
    board = [-1] * N  # 퀸의 위치를 저장하는 배열 (행: 인덱스, 열: 값)
    solutions = []
    solve_n_queens(board, 0, N, solutions)
    return solutions

solutions = n_queens(4)
for sol in solutions:
    print(sol)
