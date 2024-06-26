'''
알고리즘의 성능 분석
- 연산량 : 알고리즘이 얼마나 적은 연산을 수행하는가 ?
    - 알고리즘이 수행해야 하는 작업(연산)의 양
    - 시간 효율성
- 메모리 사용량 : 얼마나 적은 메모리 공간을 사용하는가 ?
    - 필요한 작업을 하는데 사용하는 기억 공간의 양
    - 공간 효율성

가장 좋은 알고리즘은 시간 효율성과 공간 효율성이 둘 다 낮은 것이지만 
둘 중 하나를 고르면 보통은 시간 효율성을 선택한다.
'''

#시간 효율성 간단한 측정
def testAlgorithm(input):
    return 0

import time
start = time.time()
testAlgorithm(input)
end = time.time()
print('실행시간 = ',end-start)
'''
위에 내용으로 알고리즘의 성능을 비교하는데에는 치명적인 약점이 있다.
1. 알고리즘을 반드시 '구현'해야 한다.
- 비교적 단순하면 어렵지 않지만 복잡한 경우에는 구현이 큰 부담이 될 수 있다.
2. 반드시 같은 조건의 하드웨어를 사용해야 한다.
- 슈퍼컴퓨터 vs 스마트폰 에서의 구현 차이
3. 프로그래밍 언어나 운영체제와 같은 소프트웨어 환경도 같아야 한다.
4. 실험되지 않은 입력에 대해서는 실행 시간을 주장할 수 없다.

=>So, 복잡도 분석(complexity analysis) 방법을 사용한다.
구현하지 않고 알고리즘의 시간 복잡도(time complexity)와 공간 복잡도(space complexity)를 구해 성능 비교
'''
def calc_sum1(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

def calc_sum2(n):
    sum = n * (n+1) /2
    return sum
'''
알고리즘의 복잡도를 구하기 위해서는 먼저 각 알고리즘에서 얼마나 많은 연산이 실행되는지 계산해야 한다.
T(n)형태로 복잡도 함수로 나타낸다. 

calc_sum1 과 calc_sum2 는 1부터 n까지의 합을 나타내는 알고리즘이다.
calc_sum1의 복잡도 함수는 T1(n) = 2n + 1 (반복만큼)
calc_sum2의 복잡도 함수는 T2(n) = 4 (대입,곱셈,덧셈,나눗셈 연산이 한 번씩만)
=> n이 커질 수록 calc_sum1이 비효율적.


'''
