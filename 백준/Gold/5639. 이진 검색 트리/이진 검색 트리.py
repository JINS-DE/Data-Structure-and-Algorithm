
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘려주기
input=sys.stdin.readline

def post_order(start,end):
    if start > end:
        return
    root=preorder[start]
    # 루트 다음 노드
    split_index=start+1    
    while split_index<=end:
        # 루트 노드보다 큰 인덱스 번호 찾기
        if preorder[split_index]>=root:
            break
        split_index+=1
    
    # 루트 다음부터 루트보다 큰 수 전까지(왼쪽 노드들)
    post_order(start+1,split_index-1)
    # 루트보다 큰 수부터 끝까지(오른쪽 노드들)
    post_order(split_index,end)
    # print가 맨 밑으로 가면 후위 순회
    print(root)

preorder=[] # 전위순회 값 저장
while True:
    try:
        num = int(input())  # 전위 순회된 값을 입력받습니다.
        preorder.append(num)
    except:
        break  # 더 이상 입력이 없으면 종료합니다.

post_order(0, len(preorder) - 1)  # 후위 순회 시작