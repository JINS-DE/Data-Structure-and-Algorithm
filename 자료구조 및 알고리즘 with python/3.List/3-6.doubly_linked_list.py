# 이중 연결 구조로 리스트 구현
class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem # 노드의 데이터 필드(요소)
        self.next = next # 다음 노드를 위한 링크
        self.prev = prev # 이전 노드를 위한 링크(추가됨)