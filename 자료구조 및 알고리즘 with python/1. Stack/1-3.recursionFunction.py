'''
순환(recursion) : 함수가 자기 자신을 다시 호출하여 문제를 해결하는 프로그래밍 기법
- 문제 자체가 순환적일 때 사용(팩토리얼, 하노이)
- 순환적으로 정의되는 자료구조(이진 트리)일 때 사용

- 주의 사항 - 
순환은 함수 호출에 의한 부담이 있고, 시스템 스택을 많이 사용하기에 대부분 반복보다 느리다.
but, 트리와 같은 특정 문제에 대해 반복보다 훨씬 명확하고 간결한 코딩이 가능하다.
'''

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
'''
factorial(4)
-> 4*factorial(3)
-> 3*factorial(2)
-> 2*factorial(1)
--------------------
-> 2*1
-> 3*(2*1)
-> 4*(3*(2*1)) => 24
''' 
print(factorial(4))


def hanoi(n,fr,tmp,to):
    if n==1:
        print(f"{n}:{fr}->{to}") 
    else:
        hanoi(n-1,fr,to,tmp)
        print(f"{n}:{fr}->{to}") 
        hanoi(n-1,tmp,fr,to)

hanoi(4,'A','B','C')


'''
hanoi(4,'A','B','C')
->1 hanoi(3,'A','C','B')
   5 print(3:A->B)
   6 hanoi(2,'C','A','B')
        7 hanoi(1,'C','B','A') print(1:'C'->'A') 
        8 print(2:'C'->'B') 
        9 hanoi(1,'A','C','B') print(1:'A'->'B') 
->2 hanoi(2,'A','B','C') => print(2:A->C) 
   4 hanoi(1,'B','A','C') => print(1:B->C) 
->3 hanoi(1,'A','C','B') => print(1:A->B)
'''