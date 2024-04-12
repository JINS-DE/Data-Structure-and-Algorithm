'''
원형 큐와 덱은 같은 기능이 많다. 그러기에 상속(inheritance)의 객체지향 프로그래밍 기법을 이용한다.
isEmpty(), isFull(), size 연산은 이름과 동작이 모두 같고 , deleteFront, getFront, addRear은 같은 연산인데 이름만 바뀐 것이다.
'''

from ArrayQueue import ArrayQueue
class CircularDeque(ArrayQueue):
    def __init__(self, capacity=10): # 생성자는 상속되지 않아 다시 구현
        super().__init__(capacity) # 부모(super())의 생성자를 직접 호출하여 부모 클래스의 데이터 초기화
    
    # 이미 구현된 부모 클래스의 해당 연산을 호출하기만 하면 된다.
    def addRear( self, item ) : self.enqueue(item)
    def deleteFront(self) : return self.dequeue()
    def getFront( self ) : return self.peek()
    
    def addFront(self, item):
        if not self.isFull():
            self.array[self.front]=item
            self.front=(self.front-1+self.capacity)%self.capacity # 반시계 방향 회전
        else: pass

    def deleteRear( self ):
        if not self.isEmpty():
            item=self.array[self.rear]
            self.rear=(self.rear-1+self.capacity)%self.capacity
            return item
        else : pass
    
    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else : pass

# 원형 덱의 활용 , 테스트 프로그램
dq = CircularDeque()

for i in range(9):
    if i%2==0: dq.addRear(i)
    else : dq.addFront(i)
dq.display("홀수는 전단 짝수는 후단 삽입")

for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display("전단 삭제 2번, 후단 삭제 3번")

for i in range(9,14) : dq.addFront(i)
dq.display("전단에 9~13 삽입")