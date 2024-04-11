'''
배열 구조의 큐를 위한 데이터
- array[] : 큐 요소들을 저장할 배열
- capacity : 큐에 저장할 수 있는 요소의 최대 개수
- rear : 맨 마지막(후단) 요소의 위치(인덱스)
- front : 첫 번째(전단) 요소 바로 이전의 위치(인덱스)

# 선형 큐(linear queue)
- front에 공간이 나오면 그 남은 공간으로 밀어줘야 한다.
- 동작을 이해하기는 쉽지만 요소들의 이동이 필요하여 효율적이지 않다.

# 원형 큐(circular queue)
- 인덱스 front와 rear를 원형으로 회전시키는 개념이다.
- 선형 큐의 문제를 해결 가능하다.
'''

# 원형 큐의 클래스 구현 (시계 방향 기준)
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

# Test Program
import random
q=ArrayQueue(8)
q.display("초기 상태")
while not q.isFull():
    q.enqueue(random.randint(0,100))
q.display("포화 상태")

print("삭제 순서: ", end='')
while not q.isEmpty():
    print(q.dequeue(), end=' ')
print()

'''
# 원형 큐를 링 버퍼로 사용하기
- 예를 들어 최대 7개의 요소를 저장할 수 있는 원형 큐가 있다하자.
- 7개 이상의 자료들이 연속적으로 입력된다면
- 가장 최근에 들어온 7개만 저장되도록 한다. 오래된 데이터는 버린다.
이를 링 버퍼(ring buffer)라고 한다.
'''

# enqueue2를 활용해서 포화상태에도 삽입이 가능하게 하여 계속 포화 상태를 유지
print("--------------------------------")
q=ArrayQueue(8)

q.display("초기 상태")
for i in range(6):
    q.enqueue2(i)
q.display("삽입 0-5")

q.enqueue2(6); q.enqueue2(7)
q.display("삽입 6,7")

q.enqueue2(8); q.enqueue2(9)
q.display("삽입 8,9")

q.dequeue(); q.dequeue()
q.display("전단 2개 삭제")
