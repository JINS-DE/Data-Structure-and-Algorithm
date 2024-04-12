'''
파이썬의 queue 모델은 스택과 함께 큐를 제공 해준다.
큐 클래스의 이름은 Queue이다.

삽입/삭제 : pull(), get()
공백/포화 : empty(), full()
전단 들여다보기 : 제공x
'''
import queue
import random
q = queue.Queue(8)

print("삽입 순서 : ",end ='')
while not q.full():
    v=random.randint(0,100)
    q.put(v)
    print(v, end=' ')
print()

print("삭제 순서 : ",end ='')
while not q.empty():
    print(q.get(), end=' ')
print()

# collections 모듈의 deque 클래스 사용하기

'''
전단 삽입/삭제 : appendleft(),popleft()
후단 삽입/삭제 : append(),pop()
공백 상태 겁사 : dq
포화 상태 검사 : 의미 없음 (용량 무한)
들여다보기 : 제공하지 않음
'''
print('-------------------------------')
import collections
dq = collections.deque()

print("덱은 공백상태 아님"if dq else "덱은 공백 상태")
for i in range(9):
    if i%2 ==0 : dq.append(i) # 짝수는 후단
    else : dq.appendleft(i) # 홀수는 전단
print("홀수는 전단 짝수는 후단 삽입",dq)

for i in range(2): dq.popleft()
for i in range(3): dq.pop()
print("전단 삭제 2번, 후단 삭제 3번",dq)

for i in range(9,14) : dq.appendleft(i) #9~13 전단 삽입
print("전단데 9~13 삽입")

print("덱은 공백상태 아님" if dq else "덱은 공백 상태")