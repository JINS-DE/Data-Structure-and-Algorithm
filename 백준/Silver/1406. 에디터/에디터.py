import sys
input = sys.stdin.readline
left_stack = list(input().strip())  # 개행 문자 제거
right_stack = []

n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == "P":
        left_stack.append(command[1])
    elif command[0] == "L" and left_stack:
        right_stack.append(left_stack.pop())
    elif command[0] == "B" and left_stack:
        left_stack.pop()
    elif command[0] == "D" and right_stack:
        left_stack.append(right_stack.pop())

print(''.join(left_stack + right_stack[::-1]))
