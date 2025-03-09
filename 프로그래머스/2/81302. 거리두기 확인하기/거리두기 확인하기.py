def solution(places):
    def dfs(depth, r, c):
        if depth == 2:  # 최대 거리 2까지만 탐색
            return True

        visited[r][c] = 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                if place[nr][nc] == 'P':  # 거리 2 이내에 P가 있으면 거리두기 실패
                    return False
                if place[nr][nc] == 'O':  # 빈 공간일 경우만 계속 탐색
                    if not dfs(depth + 1, nr, nc):
                        return False

        return True

    answer = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for place in places:
        flag = True  
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':  
                    visited = [[0] * 5 for _ in range(5)]
                    if not dfs(0, i, j):  
                        flag = False
                        break
            if not flag:
                break
        answer.append(1 if flag else 0)

    return answer
