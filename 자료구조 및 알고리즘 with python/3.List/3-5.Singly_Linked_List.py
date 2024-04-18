class Node:
    def __init__ (self, elem, link=None):
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = link # 링크 생성 및 초기화

    def append(self, node):
        if node is not None:
            node.link = self.link 
            self.link = node
    
    def popNext(self): # self의 다음 노드를 삭제하는 연산
        next = self.link # 현재 노드(self)의 다음 노드
        if next is not None:
            self.link = next.link
        return next # 다음 노드 반환
 
class LinkedList: # 단순 연결 리스트 클래스
    def __init__(self) : # 생성자
        self.head = None # head 선언 및 None으로 초기화

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
            ptr = ptr.link # 최종 노드 반환
        return ptr
    
    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 구함
        if node == None : return None # 해당 노드가 없는 경우
        else : return node.data # 있는 경우 데이터 필드 반환
    
    def insert(self, pos, e) :
        node = Node(e,None) # 삽입할 새로운 노드를 만듦 
        before = self.getNode(pos-1) # 삽입할 위치 이전 노드 탐색
        if before == None: # before가 None이면 맨 앞에 추가, 리스트의 머리노드 변경
            node.link = self.head
            self.head = node
        else: before.append(node) # 아닌 경우 : before 뒤에 추가

    def delete(self,pos):
        before = self.getNode(pos-1)
        if before == None:
            before = self.head 
            if self.head is not None:
                self.head = self.head.link
            return before
        else: return before.popNext()
    def display(self,msg='LinkedList:'):
        print(msg,end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='->')
            ptr=ptr.link
        print('None')
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None: # ptr이 None이 아닌 동안
            ptr =ptr.link # 링크를 따라 ptr 이동
            count+=1 # 이동할 때마다 count 증가
        return count # count 반환


s=LinkedList()
s.insert(0,10)
s.display()
s.insert(0,20)
s.display()
s.insert(2,40)
s.display()
s.insert(1,30)
s.display()
s.delete(2)
s.display()
print(s.size())

