from itertools import permutations

def solution(expression):
    answer = []
    operator = {'-', '+', '*'}
    st = ''
    arr = []

    # 수식 파싱
    for s in expression:
        st += s
        if s in operator:
            arr.append(st[:-1])  # 숫자 추가
            arr.append(st[-1])   # 연산자 추가
            st = ''
    arr.append(st)  # 마지막 숫자 추가

    for permu in permutations(operator, 3):  # 연산자 우선순위 순열 생성
        li = arr[:]  # 리스트 깊은 복사 (얕은 복사 방지)
        for op in permu:
            new_li = []
            i = 0
            while i < len(li):
                if li[i] == op:
                    # 연산 수행
                    num1 = int(new_li.pop())  # 이전 숫자
                    num2 = int(li[i + 1])  # 다음 숫자
                    if op == '+':
                        new_li.append(str(num1 + num2))
                    elif op == '-':
                        new_li.append(str(num1 - num2))
                    else:  # '*'
                        new_li.append(str(num1 * num2))
                    i += 1  # 다음 숫자 스킵
                else:
                    new_li.append(li[i])
                i += 1
            li = new_li  # 업데이트된 리스트 반영
        answer.append(abs(int(li[0])))

    return max(answer)
