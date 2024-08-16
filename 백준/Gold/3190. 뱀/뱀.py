from collections import deque

def play_game():
    # 방향: 오른쪽(0), 아래쪽(1), 왼쪽(2), 위쪽(3)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    n = int(input())
    k = int(input())
    board = [[0] * n for _ in range(n)]
    
    # 사과 위치 입력
    for _ in range(k):
        x, y = map(int, input().split())
        board[x-1][y-1] = 1  # 사과가 있는 위치를 1로 표시
    
    l = int(input())
    changes = {}
    for _ in range(l):
        time, direction = input().split()
        changes[int(time)] = direction
    
    # 초기 설정
    direction = 0  # 처음에는 오른쪽
    time = 0
    x, y = 0, 0  # 뱀의 머리 위치
    snake = deque([(x, y)])  # 뱀의 몸을 deque로 관리 (머리부터 꼬리 순)
    board[x][y] = 2  # 뱀이 있는 곳을 2로 표시
    
    while True:
        time += 1
        x += dx[direction]
        y += dy[direction]
        
        # 범위를 벗어났거나 자기 몸에 부딪힌 경우 게임 종료
        if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 2:
            break
        
        # 이동한 위치에 사과가 있는 경우
        if board[x][y] == 1:
            board[x][y] = 2  # 뱀의 몸으로 변경 (길이 증가)
            snake.append((x, y))
        else:
            # 사과가 없는 경우
            board[x][y] = 2
            snake.append((x, y))
            tail_x, tail_y = snake.popleft()  # 꼬리 제거
            board[tail_x][tail_y] = 0  # 꼬리 위치를 비워줌
        
        # 시간에 따른 방향 전환
        if time in changes:
            if changes[time] == 'L':
                direction = (direction - 1) % 4  # 왼쪽 회전
            else:
                direction = (direction + 1) % 4  # 오른쪽 회전
    
    return time

print(play_game())
