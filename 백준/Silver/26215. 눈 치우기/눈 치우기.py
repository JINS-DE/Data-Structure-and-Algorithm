def min_snow_removal_time(n, snow_heights):
    snow_heights.sort(reverse=True)  # 눈의 높이를 내림차순 정렬
    time = 0

    while snow_heights and snow_heights[0] > 0:
        if n >= 2 and snow_heights[1] > 0:
            # 두 사람을 활용해 눈을 치움
            snow_heights[0] -= 1
            snow_heights[1] -= 1
        else:
            # 남은 집이 하나이거나, 두 번째 집 앞에 눈이 없을 경우 혼자서 치움
            snow_heights[0] -= 1
        
        # 다시 정렬
        snow_heights.sort(reverse=True)
        time += 1

    return time

# 입력 받기
n = int(input())
snow_heights = list(map(int, input().split()))

# 최소 시간 계산
time = min_snow_removal_time(n, snow_heights)

# 시간이 1440분을 넘으면 -1 출력
if time > 1440:
    print(-1)
else:
    print(time)
