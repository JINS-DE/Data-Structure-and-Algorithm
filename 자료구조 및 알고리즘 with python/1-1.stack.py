'''
# 자료구조
- 선형(linear) : 큐, 스택, 덱, 리스트
- 비선형(non-linear) : 트리, 그래프

# 스택이란?
- 후입선출(Last-IN First-Out)인 LIFO 형태
- 상단(Stack Top)만 열어둔 상태
=> 요소의 삽입과 삭제가 상단에서만 가능하다.

# 추상자료형(ADT : Abstract Data Type) : 추상화를 통해 정의한 자료형
- 추상화란? 새로운 자료형을 정의하기 위해 복잡한 내용 대신 필수적이고 중요한 특징만 골라 단순화 시킴.
즉 어떤 자료를 다루고, 어떤 연산이 필요한지 정의해 보는 것

# 스택의 연산
- push(e), pop(), isEmpty(), isFull(), peek(), size()

# 오버플로(overflow) : 삽입불가 (포화상태)
# 언더플로(underflow) : 삭제불가 (공백상태)

# 배열구조 : 인접한 메모리 공간에 저장
# 연결된 구조 : 흩어져 있는 요소들을 연결
'''

capacity = 10 # 스택 용량 : 10으로 지정
array = [None]*capacity # 요소 배열 : [None,None...,None] (길이가 capacity)
top = -1 # 상단 인덱스 (공백상태 -1 초기화)

def isEmpty():
    return top==-1

def isFull():
    return top==capacity

def push(e):
    # global top
    if not isFull():
        top+=1
        array[top]=e
    else:
        print("stack overflow")
        exit()

def pop():
    #global top
    if not isEmpty():
        top -= 1
        return array[top+1]
    else:
        print("stack underflow")
        exit()

def peek():
    if not isEmpty():
        return array[top]
    else: pass

def size() : return top+1
# ----------문제발생----------------
'''
1. 전역변수를 선언해서 오류를 피해야함
2. 전역변수를 사용한다 한들 여러 개의 스택이 동시에 필요한 문제에는 사용하기가 힘듬
=> 즉! 함수 기반으로 하는 절차적 프로그래밍보다는 클래스를 기반으로 하는 객체 지향 프로그래밍 기법을 사용해하는 것이 훨씬 좋다.
자료구조의 추상 자료형이 클래스의 개념과 정확히 일치한다 ! 

# 객체 지향 프로그래밍
- 클래스(class) : 데이터와 함수를 묶는 하나의 틀
- 멤버변수 : 클래스에 포함된 데이터
- 메서드(method) : 클래스에 포함된 함수(멤버함수)
- 객체(object) : 클래스의 사례(인스턴스,instance)
스택에서는 스택을 위한 데이터가 멤버변수, 스택의 연산이 멤버함수
클래스가 자료형, 객체는 그 자료형의 변수
'''
# 스택을 class로 구현
# self는 모든 메서드(멤버함수)의 첫 번째 매개변수로 객체 자신을 나타냄
class ArrayStack:
    def __init__(self, capacity): # 스택의 생성자(constructor)
        self.capacity = capacity 
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top==-1

    def isFull(self):
        return self.top==capacity

    def push(self, item):
        if not self.isFull():
            self.top+=1
            self.array[self.top]= item
        else:
            pass

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else:pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass

    def size(self) : return self.top+1

# ex1)
# s = ArrayStack(5)
# msg = input("문자열 입력: ")
# for i in msg:
#     s.push(i)
# print("문자열 출력: ", end ='')    
# while not s.isEmpty():
#     print(s.pop(), end='')

'''
# 괄호 검사 문제
조건 1 : 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
조건 2 : 같은 종류인 경우 왼쪽 괄호가 오른쪽보다 먼저 나와야 한다.
조건 3 : 다른 종류의 괄호 쌍이 서로 교차하면 안 된다.

- 준비 과정 - 
1. 빈 스택 준비
2. 입력된 문자를 하나씩 읽어 왼쪽 괄호를 만나면 스택에 삽입
3. 오른쪽 괄호를 만나면 가장 최근에 삽입된 괄호를 스택에서 꺼냄, 이 때 스택이 비었다면 오른쪽 괄호가 먼저 나온 상황이므로 조건2에 위배
4. 꺼낸 괄호가 오른쪽 괄호와 짝이 맞지 않으면 조건 3에 위배
5. 입력 문자열을 끝까지 처리했는데 스택에 괄호가 남아 있으면 괄호의 개수가 같지 않으므로 조건 1에 위배
6. 모든 문자를 처리하고 스택이 공백 상태이면 성공
'''

def checkBrackets(statement):
    stack = ArrayStack(15)
    for i in statement:
        if i in '({[':
            stack.push(i)
            print(stack.array)
            
        elif i in ')}]':
            if stack.isEmpty():
               return False
            else:
                left = stack.pop()
                if ( i==')' and left != '(' ) or ( i=='}' and left != '{' ) or ( i==']' and left != '[' ):
                    return False
    return stack.isEmpty()

print(checkBrackets('[iT+1{34(1(i)2)}]()...'))