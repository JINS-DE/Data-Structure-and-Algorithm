# 비트마스킹 연습
import sys
input=sys.stdin.readline
M=int(input())
S=0
for _ in range(M):
    li = input().split()
    if len(li)==2:
        command,num=li
        num=1<<int(num)
    else:
        command=li[0]
    
    if command=="add":
        S|= num
    elif command=="remove":
        S&= ~ num
    elif command=="check":
        print(1 if S&(num) else 0)
    elif command=="toggle":
        S^= num
    elif command=="all":
        S= (1<<21)-1
    else:
        S=0