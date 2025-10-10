from collections import defaultdict,deque
def solution(edges):
    # 1. 그래프 정보 초기화
    max_node = 0
    adj = defaultdict(list)
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    
    for a,b in edges:
        adj[a].append(b)
        indegree[b]+=1
        outdegree[a]+=1
        max_node = max(max_node,a,b)
        
    # 2. 시작 정점 찾기
    start_node = -1
    for i in range(1, max_node + 1):
        if indegree[i] == 0 and outdegree[i] >= 2:
            start_node = i
            break
    
    answer=[start_node,0,0,0] # [초기 시작 정점, 도넛, 막대, 8자]
    visited = [0] * (max_node + 1)
    
    for node in adj[start_node]:
        if visited[node]:
            continue
        # BFS로 한 덩어리의 노드와 간선 수 세기
        q = deque([node])
        visited[node] = True
        node_count = 1
        edge_count = outdegree[node]
        
        while q:
            curr = q.popleft()
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
                    node_count += 1
                    edge_count += outdegree[neighbor]
        
        if edge_count == node_count -1: # 막대 그래프
            answer[2] += 1
        elif edge_count == node_count + 1: # 8자 그래프
            answer[3] += 1
        else:
            answer[1]+=1
        
    return answer