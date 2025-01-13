def dfs(start, goal, flag):
    # start: 현재 위치
    # goal: 도착지 위치
    # flag: 도착 가능한지 여부 (True/False)

    if abs(start[0] - goal[0]) + abs(start[1] - goal[1]) <= 1000:
        return True

    for i in range(len(store)):
        if not visited[i]:
            if abs(start[0] - store[i][0]) + abs(start[1] - store[i][1]) <= 1000:
                visited[i] = 1  
                if dfs(store[i], goal, flag): 
                    return True
    return False


import sys
input = sys.stdin.readline
t = int(input()) 

for _ in range(t):
    n = int(input())
    house = tuple(map(int, input().split())) 
    store = [tuple(map(int, input().split())) for _ in range(n)]  
    goal = tuple(map(int, input().split())) 

    visited = [0 for _ in range(n)]

    flag = dfs(house, goal, False)
    if flag:
        print("happy")
    else:
        print("sad")
