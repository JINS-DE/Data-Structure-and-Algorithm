import heapq
def solution(N, road, K):
    adj=[[] for _ in range(N+1)]
    distance=[float("inf")]*(N+1)
    distance[1]=0
    for a,b,w in road:
        adj[a].append((b,w))
        adj[b].append((a,w))
    
    q=[]
    heapq.heappush(q,(0,1))
    while q:
        current_weight, current_node = heapq.heappop(q)
        if current_weight > distance[current_node]:
            continue
        for next_node, next_weight in adj[current_node]:
            dist = current_weight + next_weight
            if dist < distance[next_node]:
                distance[next_node]=dist
                heapq.heappush(q,(dist,next_node))
    answer=0
    for dis in distance:
        if dis <=K:
            answer+=1
        
    return answer