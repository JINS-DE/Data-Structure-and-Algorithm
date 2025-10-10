from collections import defaultdict

def solution(edges):
    # 1. 그래프 정보 수집
    # defaultdict을 사용하면 max_node를 미리 찾을 필요 없이 동적으로 처리 가능
    out_degree = defaultdict(int)
    in_degree = defaultdict(int)
    nodes = set() # 모든 노드 번호를 저장

    for a, b in edges:
        out_degree[a] += 1
        in_degree[b] += 1
        nodes.add(a)
        nodes.add(b)

    # 2. 각 특징에 맞는 노드 찾기
    answer = [0, 0, 0, 0] # [생성정점, 도넛, 막대, 8자]
    
    for node in nodes:
        # 생성 정점 찾기
        if in_degree[node] == 0 and out_degree[node] >= 2:
            answer[0] = node
        # 8자 그래프의 중심점 찾기
        elif in_degree[node] >= 2 and out_degree[node] == 2:
            answer[3] += 1
        # 막대 그래프의 끝점 찾기
        elif out_degree[node] == 0:
            answer[2] += 1
            
    # 3. 최종 계산 (도넛 그래프 수)
    # 전체 그래프 수 = 생성 정점의 out-degree
    # 도넛 수 = 전체 - (막대 + 8자)
    # 생성 정점에서 나가는 간선 중, 8자/막대 그래프로 가지 않은 간선이 도넛 그래프로 감
    # 8자/막대 그래프에 사용된 간선 수는 (8자 수 + 막대 수)와 같음
    if answer[0] in out_degree:
      total_graphs = out_degree[answer[0]]
      answer[1] = total_graphs - answer[2] - answer[3]
    
    return answer