def check(command):
    min_x,min_y,max_x,max_y = 0,0,0,0
    curr_x,curr_y = 0,0
    direct = 0
    for c in command:
        if c == "F":
            curr_x += direction[direct][0]
            curr_y += direction[direct][1]
        elif c == "R":
            direct= (direct+1)%4
        elif c == "L":
            direct= (direct-1)%4
        else:
            curr_x -= direction[direct][0]
            curr_y -= direction[direct][1]
        
        min_x = min(min_x,curr_x)
        min_y = min(min_y,curr_y)
        max_x = max(max_x,curr_x)
        max_y = max(max_y,curr_y)
    return (max_x-min_x)*(max_y-min_y)

import sys
input = sys.stdin.readline
T = int(input())
direction = [(0,1),(1,0),(0,-1),(-1,0)]

for _ in range(T):
    command = input().strip()
    print(check(command))