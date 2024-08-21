import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

n = int(input())  # 숫자 개수
numbers = list(map(int, input().split()))  # 숫자 리스트
operator = list(map(int, input().split()))  # 연산자 리스트

max_val = -sys.maxsize  # 최댓값 초기화
min_val = sys.maxsize   # 최솟값 초기화

def dfs(depth, current_result):
    global max_val, min_val
    # 모든 숫자를 다 사용한 경우
    if depth == n:
        max_val = max(max_val, current_result)  # 최댓값 갱신
        min_val = min(min_val, current_result)  # 최솟값 갱신
    else:
        # 덧셈
        if operator[0] > 0:
            operator[0] -= 1
            dfs(depth + 1, current_result + numbers[depth])
            operator[0] += 1

        # 뺄셈
        if operator[1] > 0:
            operator[1] -= 1
            dfs(depth + 1, current_result - numbers[depth])
            operator[1] += 1

        # 곱셈
        if operator[2] > 0:
            operator[2] -= 1
            dfs(depth + 1, current_result * numbers[depth])
            operator[2] += 1

        # 나눗셈
        if operator[3] > 0:
            operator[3] -= 1
            if current_result < 0:
                dfs(depth + 1, -(-current_result // numbers[depth]))
            else:
                dfs(depth + 1, current_result // numbers[depth])
            operator[3] += 1

# 깊이 1부터 시작 (첫 번째 숫자는 이미 계산에 포함된 것으로 간주)
dfs(1, numbers[0])

print(max_val)
print(min_val)

