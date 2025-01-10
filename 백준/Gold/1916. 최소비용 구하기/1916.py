import sys, heapq
input=sys.stdin.readline
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for i in range(m):
    s,e,v = map(int,input().split())
    adj[s].append((e,v))

start, end = map(int,input().split())
distance = [1e9 for _ in range(n+1)]
heap = []
distance[start] = 0
heapq.heappush(heap,(0,start))

while heap:
    cur_dis, cur_node = heapq.heappop(heap)
    if cur_dis > distance[cur_node] : 
        continue
    for next_node, next_dis in adj[cur_node]:
        tmp = cur_dis + next_dis
        if distance[next_node] > tmp :
            distance[next_node] = tmp
            heapq.heappush(heap,(tmp,next_node))

print(distance[end])

