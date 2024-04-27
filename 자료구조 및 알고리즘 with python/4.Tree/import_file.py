class ArrayQueue:
    def __init__(self, capacity=10): # 원형큐의 생성자 정의
        self.capacity = capacity # 용량
        self.array = [None]*capacity # 요소들을 저장할 배열
        self.front = 0 # 전단 인덱스
        self.rear = 0 # 후단 인덱스
    
    def isEmpty(self): #공백 상태 확인
        return self.front==self.rear
    
    def isFull(self): # 포화 상태 확인
        return self.front==(self.rear+1)%self.capacity
    
    def enqueue(self, item): # 삽입 연산
        if not self.isFull():
            self.rear=(self.rear+1)%self.capacity
            self.array[self.rear]=item
        else: pass # 오버플로 오류 : 처리 안 함
    
    def dequeue(self): # 삭제 연산
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity
            return self.array[self.front]
        else: pass # 언더플로 오류 : 처리 안 함

    def peek(self): # 상단 들여다보기 연산
        if not self.isEmpty():
            return (self.front+1)%self.capacity
        else : pass 
    
    def size(self): # 전체 요소의 수
        return (self.rear-self.front+self.capacity)%self.capacity
    
    def display(self,msg) : 
        print(msg, end='= [')
        for i in range(self.front+1,self.front+1+self.size()):
            print(self.array[i%self.capacity],end=' ')
        print(']')
    
    def enqueue2(self,item):
        self.rear = (self.rear+1)%self.capacity
        self.array[self.rear]=item # 일단 강제 삽입
        if self.isEmpty(): # 삽입 후에도 empty가 뜬다면 포화상태임
            self.front=(self.front+1)%self.capacity # front를 회전시켜 가장 오래된 요소 삭제

class BTNode:
    def __init__ (self, elem, left=None, right=None):
        self.data = elem
        self.left = left # 왼쪽 자식을 위한 링크
        self.right = right # 오른쪽 자식을 위한 링크
    def isLeaf(self):
        return self.left is None and self.right is None

# 1. 전위순회(preorder)
def preorder(n): 
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left) 
        preorder(n.right) 

# 2. 중위순회(inorder)
def inorder(n):
    if n is not None:
        inorder(n.left) 
        print(n.data, end=' ')
        inorder(n.right)

# 3. 후위순회(postorder)
def postorder(n):
    if n is not None:
        postorder(n.left) 
        postorder(n.right) 
        print(n.data, end=' ')