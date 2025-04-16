def solution(s):
    answer = []

    for x in s:
        last_zero_idx = -1
        stack, cnt110 = [], 0

        for n in x:
            stack.append(n)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                # '110' 제거
                del stack[-3:]
                cnt110 += 1
            elif stack[-1] == '0':
                last_zero_idx = len(stack) - 1  # 마지막 0 위치 기억

        # '110'을 삽입할 위치 계산
        insert_110 = list('110' * cnt110)
        if last_zero_idx == -1:
            # 0이 하나도 없으면, 맨 앞에 삽입
            stack = insert_110 + stack
        else:
            # 가장 마지막 0 뒤에 삽입
            stack = stack[:last_zero_idx+1] + insert_110 + stack[last_zero_idx+1:]

        answer.append(''.join(stack))

    return answer
