def solution(n, lost, reserve):
    # 여벌이 있지만 도난당한 학생을 먼저 제외 (차집합 사용)
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    # 체육복을 빌릴 수 있는 경우 찾기
    for miss in sorted(lost_set):
        if miss - 1 in reserve_set:  # 앞 번호 학생이 여벌 있음
            reserve_set.remove(miss - 1)
            lost_set.remove(miss)
        elif miss + 1 in reserve_set:  # 뒷 번호 학생이 여벌 있음
            reserve_set.remove(miss + 1)
            lost_set.remove(miss)
    
    return n - len(lost_set)  # 도난당한 학생 중 체육복을 못 빌린 학생 제외

