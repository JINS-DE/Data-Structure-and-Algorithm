import sys
sys.setrecursionlimit(10**6)
def solution(n, m, x, y, r, c, k):
    # 사전순 이동 순서 (d -> l -> r -> u)
    directions = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}
    order = ['d', 'l', 'r', 'u']  # 사전순 정렬
    answer = []
    
    # 맨해튼 거리 계산
    min_dist = abs(x - r) + abs(y - c)
    
    # 도달할 수 없는 경우 (k와 최단 거리의 홀짝성이 다르면 불가능)
    if min_dist > k or (k - min_dist) % 2 == 1:
        return "impossible"

    def dfs(cx, cy, path, moves):
        # 경로를 찾으면 즉시 종료
        if answer:
            return
        
        # 정확히 k번 이동했을 때 목표 위치 도달하면 정답
        if moves == k:
            if cx == r and cy == c:
                answer.append(path)
            return
        
        # 사전순으로 탐색 (d → l → r → u)
        for d in order:
            dx, dy = directions[d]
            nx, ny = cx + dx, cy + dy
            
            # 범위를 벗어나면 스킵
            if not (1 <= nx <= n and 1 <= ny <= m):
                continue
            
            # 남은 이동 가능 거리
            remaining_moves = k - (moves + 1)
            manhattan_dist = abs(nx - r) + abs(ny - c)

            # 남은 이동 거리로 도달 가능할 때만 탐색
            if remaining_moves >= manhattan_dist:
                dfs(nx, ny, path + d, moves + 1)

    # DFS 탐색 시작
    dfs(x, y, "", 0)
    
    return answer[0] if answer else "impossible"
