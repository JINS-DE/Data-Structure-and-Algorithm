'''
상근이는 4장~10장 개수 사이의 카드를 놓고 놀고있다.
각 카드에는 1~99 정수가 적혀있다
상근이는 카드 중 2~4장을 선택한다.
그 카드로 가로로 나란히 정수를 만든다.
상근이가 만들 수 있는 정수는 모두 몇 가지 인가?

ex) 1,2,3,13,21이 적혀 있는 카드 5장
여기서 3장을 선택해 정수를 만든다.
2,1,13 -> 2113 만든다.
21,1,13 -> 2113 

이렇게 한 정수를 만드는 조합이 여러 가지 일 수 있다.

n장의 카드에 적힌 숫자가 주어졌을 때, 그 중에서 k개를 선택해서 만들 수 있는 정수의 개수를 구하는 프로그램

입력
4 -> n : 총 카드 개수
2 -> k : 선택할 카드 개수
1 -> 1-99의 정수
2 -> 1-99의 정수
12 -> 1-99의 정수
1 -> 1-99의 정수

순열
# aPc = a!/(a-c)!
조합
# aCc = aPc / c! = a!/c!(a-c)!

첫번째 작전 세우기 -> 
n=6; k=3; arr=['1','2','3','4','5','6']
1. 일단 3(k)개를 뽑는다. (조합)
2. 3(k)개를 뽑은 것을 배열한다. (순열) 
    - 1,2,3을 뽑으면 1 2 3 / 1 3 2 / 2 1 3 ... 

    => 라이브러리 사용할 것이면 1번과2번을 나눠서할 필요가 없다. 
    그냥 순열하면 된다. 6P3하면 됨.

3. 뽑은 것들을 정수화로 만들고 set에 add한다. 
4. 모든 경우의 수를 체크 하고 마지막으로 set의 len 값을 리턴한다. 
    - 재귀에서 set를 리턴해야 할 듯?
    - 그리고 마지막 set 리턴된 것을 print(len(함수(arg)))하면 되지 않을까..

'''
# #1 순열과 조합으로 풀기
# from itertools import permutations, combinations
# n=int(input())
# k=int(input())
# arr=[input().strip() for _ in range(n)] # 입력 카드 리스트
# answer_li=set() # 정수 조합 리스트
# for i in permutations(arr,k):
#     answer_li.add("".join(i))
# print(answer_li)

#2 재귀함수로 풀기( 재귀함수로 순열 사용하기 )
import sys
input=sys.stdin.readline
n=int(input())
k=int(input())
a=[input().strip() for _ in range(n)]

check = [0]*n
arr = ['']*k
result=set()
def permutations(level):
     if level==k:
          result.add(''.join(arr))
          return
     for i in range(n):
          if check[i]: continue
          check[i]=1
          arr[level] = a[i]
          permutations(level+1)
          check[i]=0

permutations(0)
print(len(result))

