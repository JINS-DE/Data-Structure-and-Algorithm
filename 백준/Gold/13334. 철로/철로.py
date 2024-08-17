'''
문제 해결 전략
1. 구간 정리
    - 각 사람의 집과 사무실을 오름차순으로 정렬
    - 각 사람의 구간 => [min(집, 사무실),max(집,사무실)] 형태로 저장

2. 구간의 시작점과 끝점 고려
    - 구간의 끝점을 오름차순 정렬
    - 우선순위 큐를 사용하여 구간 시작점 관리
    - 철로 길이 `d`로 커버할 수 있는 구간만 유지하며 최대 구간 개수 찾기

3. 우선순위 큐 사용
    - 큐에는 시작점들을 넣고, 끝점에서 `d`만큼 뺀 것 보다 작은 시작점들은 큐에서 제거
    - 이 때 큐의 크기 = 커버할 수 있는 구간의 수 
'''
import sys
import heapq
input = sys.stdin.readline
n=int(input())
data=[]
for i in range(n):
    start,end=map(int,input().split())
    # 1. 구간 정리 ----
    if start>end:
        start, end = end, start # 항상 start가 작은 값이 되도록
    data.append((start,end))

# 철로의 길이 d 입력 받기
d=int(input())

# 구간의 시작점과 끝점 고려 ----
# 끝 점을 기준으로 정렬
data.sort(key=lambda x:x[1])

# 3. 우선순위 큐 사용  ----
heap = [] # start(시작) 기준으로 넣는다. 
max_people = 0 

for start, end in data:
    # 끝점 - 시작점 <= 철도 길이 : 사람 이동 거리는 철도 길이보다 작거나 같아야 한다.
    if end-start <= d:
        heapq.heappush(heap,start)

    # 범위 밖인 경우, 우선순위 큐에서 제거
    while heap and heap[0] < end-d: # end-d(끝점- 거리) 보다 작아야 범위 안
        heapq.heappop(heap)
    
    # 최대 구간 수 업데이트
    max_people = max(max_people,len(heap))

print(max_people) 
