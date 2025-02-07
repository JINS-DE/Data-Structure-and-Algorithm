def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        tmp = int(i[s:s+l])
        if tmp > k:
            answer.append(tmp)
    return answer