import sys
input = sys.stdin.readline

# 첫 번째 줄: 전체 타구의 개수
N = int(input())

# N개의 타구의 좌표
hits = []
foul_flags = []  # 파울인지 아닌지 저장
distances = []   # 파울이 아닌 타구들의 거리 제곱값을 저장
for i in range(N):
    x, y = map(int, input().split())
    # 파울인지 확인
    if y < x or y < -x:
        # 파울인 경우
        foul_flags.append(True)
    else:
        # 파울이 아닌 경우
        foul_flags.append(False)
        distances.append(x**2 + y**2)

# 파울이 아닌 타구들의 거리 제곱값을 정렬
distances.sort()

# Q개의 담장 거리 후보
Q = int(input())
R_list = [int(input()) for _ in range(Q)]

# 파울 개수 미리 계산 (한 번만 수행)
foul_count = sum(foul_flags)

# 이분 탐색 직접 구현
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return low

# 각 거리 후보에 대한 파울, 내야, 홈런의 개수를 저장할 리스트
result = []

# 각 담장 후보 거리마다 처리
for R in R_list:
    R_squared = R ** 2

    # 이분 탐색을 사용하여 R_squared보다 작은 타구들 찾기
    infield_count = binary_search(distances, R_squared)
    homerun_count = len(distances) - infield_count

    # 결과 저장
    result.append(f"{foul_count} {infield_count} {homerun_count}")

# 출력
sys.stdout.write("\n".join(result) + "\n")
