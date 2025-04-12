def solution(picks, minerals):
    answer = 0
    li = []
    
    # ⛏️ 곡괭이로 캘 수 있는 최대 광물 수
    max_mine = sum(picks) * 5
    minerals = minerals[:max_mine]

    # 📦 5개 단위로 묶고, 해당 묶음의 난이도(피로도) 측정
    for i in range(0, len(minerals), 5):
        tmp = 0
        for j in range(i, i + 5):
            if j >= len(minerals):
                break
            if minerals[j] == "diamond":
                tmp += 25
            elif minerals[j] == "iron":
                tmp += 5
            else:
                tmp += 1
        li.append((tmp, i))  # (피로도, 시작 인덱스)
    
    li.sort()  # 피로도 낮은 것부터 → pop()하면 높은 것부터 나오게

    # ⚙️ 곡괭이 배정: 좋은 곡괭이부터 힘든 구간에 배정
    for i in range(3):  # 0:다이아, 1:철, 2:돌
        for _ in range(picks[i]):
            if li:
                _, idx = li.pop()
                for k in range(idx, idx + 5):
                    if k >= len(minerals):
                        break
                    m = minerals[k]
                    if i == 0:
                        answer += 1  # 다이아 곡괭이: 모두 1
                    elif i == 1:
                        answer += 5 if m == "diamond" else 1
                    elif i == 2:
                        answer += 25 if m == "diamond" else 5 if m == "iron" else 1
            else:
                break
                
    return answer
