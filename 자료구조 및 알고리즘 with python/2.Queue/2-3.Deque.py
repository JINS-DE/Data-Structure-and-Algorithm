'''
덱 Deque
- 덱(deque)이란 ? 
    double-ended queue의 줄임말로서 전단과 후단에서 모두 삽입과 삭제가 가능한 큐를 말한다.

- 덱의 주요 연산
    * addFront(e) : 새로운 요소 e를 전단에 추가 
    * addRear(e) : 새로운 요소 e를 후단에 추가 (큐의 enqueue와 동일)
    * deleteFront() : 덱의 전단 요소를 꺼내서 반환 (큐의 dequeue와 동일)
    * deleteRear() : 덱의 후단 요소를 꺼내서 반환 
    * getFront() : 덱의 전단 요소를 삭제하지 않고 반환 (peek 연산과 동일)
    * getRear() : 덱의 후단 요소를 삭제하지 않고 반환
    * isEmpty() : 덱이 비어있으면 True 아니면 False 반환
    * isFull() : 덱이 가득 차 있으면 True 아니면 False 반환
    * size() : 덱에 들어 있는 전체 요소의 수를 반환

- 원형 큐와 같이 원형 덱(circular deque)로 구현하는 것이 좋다. 
- 주의해야 할 연산은 deleteRear과 addFront로서 반시계 방향 회전을 시켜야 한다.
    전단 회전(반시계) : (front-1+capacity)%capacity
    후단 회전(반시계) : (rear-1+capacity)%capacity
'''