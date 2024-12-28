def minimum_decontamination(N, data):
    # 오염 물질 데이터를 위치 기준으로 정렬
    data.sort(key=lambda x: x[0])  # x[0]: 위치(index)

    # 초기값 계산
    LSUM, RSUM = 0, 0
    MNIDX = data[0][0]  # 최소 위치
    MXIDX = data[-1][0]  # 최대 위치

    for i in range(N):
        LSUM += (data[i][0] - MNIDX) + data[i][1]  # 위치 차이 + 오염도
        RSUM += (MXIDX - data[i][0]) + data[i][1]

    # 최소값 초기화
    answer = float('inf')

    # 한 개의 오염 물질 제외하며 최소값 갱신
    for i in range(N):
        if i != 0:  # 첫 번째 제외 가능
            answer = min(answer, LSUM - (data[i][0] - MNIDX) - data[i][1])
        if i != N - 1:  # 마지막 제외 가능
            answer = min(answer, RSUM - (MXIDX - data[i][0]) - data[i][1])

    # 첫 번째 오염 물질 기준으로 계산
    answer = min(answer, LSUM - (N - 1) * (data[1][0] - MNIDX) - data[0][1])
    answer = min(answer, LSUM - (MXIDX - MNIDX) - data[-1][1])

    # 마지막 오염 물질 기준으로 계산
    answer = min(answer, RSUM - (N - 1) * (MXIDX - data[-2][0]) - data[-1][1])
    answer = min(answer, RSUM - (MXIDX - MNIDX) - data[0][1])

    return answer

# 입력 받기
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    lines = input().splitlines()
    N = int(lines[0])  # 오염 물질 개수
    data = [tuple(map(int, line.split())) for line in lines[1:]]  # 위치와 오염도 데이터

    # 결과 출력
    print(minimum_decontamination(N, data))
