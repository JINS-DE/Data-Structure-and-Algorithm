N=5
C=3
houses=[1,2,8,4,9]

def find_max_distance(houses,routers):
    houses.sort()
    left=1 # 최소 거리
    right=houses[-1]-houses[0] # 최대 거리
    best_distance=0 # 가장 최적의 거리(최소 거리중에 최대 거리)

    while left <= right:
        mid = (left + right) // 2  # 중간값을 거리로 설정합니다.

        # 현재 거리(mid)로 공유기를 설치할 수 있는지 확인합니다.
        count = 1  # 첫 번째 공유기는 무조건 첫 번째 집에 설치
        last_location = houses[0]  # 마지막으로 설치한 공유기의 위치를 첫 번째 집으로 설정

        for i in range(1, len(houses)):
            if houses[i] - last_location >= mid:  # 현재 집이 마지막 설치 위치로부터 mid 이상 떨어져 있다면
                count += 1  # 공유기 하나 설치
                last_location = houses[i]  # 마지막 설치 위치 갱신

            if count >= routers:  # 설치한 공유기가 목표 개수에 도달했다면
                break  # 더 이상 확인할 필요가 없음

        # 공유기를 충분히 설치할 수 있다면, 거리를 늘려보자
        if count >= routers:
            best_distance = mid  # 현재 mid 거리가 가능한 거리로 설정
            left = mid + 1  # 더 큰 거리를 시도
        else:
            right = mid - 1  # 거리를 줄여서 시도

    return best_distance  # 최적의 거리 반환

print(find_max_distance(houses, C))  # 최대 공유기 간 최소 거리 출력