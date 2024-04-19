# 이중 연결 구조로 리스트 구현
class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem # 노드의 데이터 필드(요소)
        self.next = next # 다음 노드를 위한 링크
        self.prev = prev # 이전 노드를 위한 링크(추가됨)
    
    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node
    
    def popNext(self):
        node= self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node
    
class DblLinkedList:
    def __init__(self):
        self.head=None

    def isEmpty(self): # 공백 상태 검사
        return self.head==None # head가 None이면 공백
    
    def isFull(self): #포화 상태 검사
        return False # 연결된 구조에서는 포화 상태 없음
    
    def getNode(self, pos) : 
        if pos < 0 : return None # 잘못된 위치 -> None 반환
        ptr =  self.head # 시작 위치 -> head
        for i in range(pos): # 머리 노드에서부터 링크를 따라 pos번 이동
            if ptr == None: 
                return None
            ptr = ptr.next # 최종 노드 반환
        return ptr
    
    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 구함
        if node == None : return None # 해당 노드가 없는 경우
        else : return node.data # 있는 경우 데이터 필드 반환

    def display(self, msg='DblLinkedList:'):
        print(msg,end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>')
            ptr = ptr.next
        print('None')
    
    def insert(self,pos,e):
        node = DNode(e)
        before = self.getNode(pos-1)
        if before == None:
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else : before.append(node)
    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head 
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return before
        else: before.popNext()



d=DblLinkedList()
d.insert(0,10)
# d.insert(0,30)
# d.insert(2,20)
# d.display()
# d.insert(1,40)
# d.display()
# d.delete(3)
# d.display()
