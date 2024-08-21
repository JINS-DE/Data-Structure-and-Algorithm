'''
해결방안
* 실내 <-> 실내 : 양 노드에서 시작하고 끝나는 방향으로 두가지이다. 
* 실내<->외<->실내 or 실내<->외<->외<->실내 or 내 <->외<->내<->외-<>내
    - '외'를 기준으로 인접한 '내'의 개수를 센다.
    - 내의 개수=N 이면 '내'+'외'의 총 경우의 수는 N*(N-1)개이다.
'''

import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline
n=int(input())
total=0 # 경로의 개수 저장
inside=input().strip()
inside='0'+inside # 각 노드가 실내인지 실외인지 저장, '0'은 인덱싱 때문에 임시로 놓음
visited=[[False] for _ in range(n+1)] # 방문 배열
# 인접 리스트 만들기
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

    if inside[start]=='1' and inside[end]=='1':
        total+=2

def dfs(start):
    visited[start] = True # 방문 처리
    inside_count=0 # 현재 노드와 인접합 실내 노드 개수를 저장
    for v in graph[start]:
        # 인접한 노드가 실내(1)이라면
        if inside[v] == '1':
            inside_count +=1
        
        # 인접한 노드가 실외(0)라면 dfs를 돌려서 그 실외에 인접한 실내 개수 찾기
        elif not visited[v] and inside[i]=="0":
            inside_count+=dfs(v)
    return inside_count

for i in range(1,n+1):
    if inside[i] == '0' and not visited[i]: # 시작이 실외일 때만
        result=dfs(i) # dfs를 통해 인접한 실내 노드 개수 계산
        total += (result) * result-1
print(total)