class Node:
    def __init__ (self, elem, link=None):
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = link # 링크 생성 및 초기화

    def append(self, node):
        if node is not None:
            node.link = self.link 
            self.link = node
    