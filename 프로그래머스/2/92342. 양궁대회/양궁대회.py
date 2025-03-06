def solution(n, info):
    from itertools import combinations_with_replacement

    max_diff = 0
    best_shot = [-1]

    # 라이언이 쏠 수 있는 모든 경우 탐색
    for comb in combinations_with_replacement(range(11), n):
        shot = [0] * 11
        for i in comb:
            shot[i] += 1

        # 점수 계산
        apeach_score, lion_score = 0, 0
        for i in range(11):
            if info[i] == 0 and shot[i] == 0:
                continue
            if info[i] >= shot[i]:
                apeach_score += 10 - i
            else:
                lion_score += 10 - i

        diff = lion_score - apeach_score
        if diff > max_diff:
            max_diff = diff
            best_shot = shot[:]
        elif diff == max_diff and best_shot != [-1]:  
            # 낮은 점수를 더 많이 맞힌 경우 선택
            for j in range(10, -1, -1):
                if shot[j] > best_shot[j]:
                    best_shot = shot[:]
                    break
                elif shot[j] < best_shot[j]:
                    break

    return best_shot
