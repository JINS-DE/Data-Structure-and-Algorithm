import sys
import heapq

input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

# 데드라인 기준으로 정렬
li.sort()

# 우선순위 큐 (최소 힙) 사용
heap = []

for deadline, ramen in li:
    heapq.heappush(heap, ramen)  # 현재 문제의 컵라면 수를 큐에 추가
    if len(heap) > deadline:  # 만약 큐의 크기가 현재 데드라인을 초과하면
        heapq.heappop(heap)  # 가장 작은 컵라면 수 제거 (최소 힙이므로 가장 작은 값이 제거됨)

# 우선순위 큐에 남아있는 컵라면 수의 합이 최대가 됨
print(sum(heap))
