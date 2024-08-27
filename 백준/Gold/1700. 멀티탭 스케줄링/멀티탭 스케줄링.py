import sys
input = sys.stdin.readline

N, K = map(int, input().split())
use_seq = list(map(int, input().split()))

is_in = [False]*101
multitap = []
result = 0

for i in range(K):
    item = use_seq[i]   # 멀티탭에 꽂을 차례인 물건
    if is_in[item]:     # 이미 멀티탭에 꽂혀있는 물건이면 무시
        continue
    if len(multitap) < N:   # 멀티탭 구멍이 비어있는 경우
        multitap.append(item)
        is_in[item] = True
        continue

    pop_item_idx = 0    # 멀티탭에 있는 물건 중 빼야 할 물건의 인덱스
    max_idx = -1    # 멀티탭에 있는 물건 중 다음으로 넣을 순서에서 가장 늦은 순서의 인덱스
    for j in range(N):
        next_seq = use_seq[i+1:]    # 남은 순서
        use_item = multitap[j]      # 멀티탭의 j인덱스 물건 확인
        if use_item not in next_seq:    # 남은 순서가 없는 물건이면 뽑아야 할 최우선 순위
            pop_item_idx = j
            break
        idx = next_seq.index(use_item)  # 남은 순서에서 현재 확인중인 물건의 인덱스
        if idx > max_idx:   # 가장 멀리있는 물건 찾기
            max_idx = idx
            pop_item_idx = j    # 뽑아야 할 물건 갱신

    is_in[multitap[pop_item_idx]] = False   # 뽑은 물건에 대해서 False로 변경
    multitap[pop_item_idx] = item   # 꽂을 차례인 물건 꽂기
    is_in[item] = True  # 꽂은 물건에 대해서 True
    result += 1 # 뽑은 횟수 세기

print(result)