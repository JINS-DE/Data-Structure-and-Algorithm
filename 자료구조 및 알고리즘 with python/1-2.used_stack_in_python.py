'''
파이썬 리스트를 활용하여 스택으로 사용

- 삽입 : append() 사용
- 삭제 : pop() 사용
- 요소의 수 : len()사용
- 공백 검사 : len(list) == 0
- 포화 검사 : list는 용량이 무한대라 포화상태 의미 x
- 상단 들여다보기 : list[len()-1]
'''

# 리스트 활용 문자열 역순 출력
s = list()
# msg = input('문자열 입력: ')
msg = "123456"
for i in msg:
    s.append(i)
print("문자열 출력:", end = '')
while len(s) > 0 :
    print(s.pop(),end='')
print()

'''
파이썬에서 제공해주는 queue 모듈의 LifoQueue 사용
삽입 : put(), 삭제 : get()
공백확인 : empty(), 포화 확인 : full()
상단보기 : x
'''
import queue
s = queue.LifoQueue(maxsize=20) # maxsize가 0일 때 용량은 무한대
# msg = input('문자열 입력: ')
msg = "1234567"
for i in msg:
    s.put(i)
print("문자열 출력:",end='')
while not s.empty():
    print(s.get(),end='')
print()
