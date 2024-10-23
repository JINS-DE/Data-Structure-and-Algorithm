
import sys

st = sys.stdin.readline().rstrip()
bomb_st = sys.stdin.readline().rstrip()
bomb_st_len = len(bomb_st)
stack = []

for i in range(len(st)):
    stack.append(st[i])
    if ''.join(stack[-bomb_st_len:]) == bomb_st:
        for _ in range(bomb_st_len):
            stack.pop()
            
if stack : 
    print(''.join(stack))
else:
    print("FRULA")
