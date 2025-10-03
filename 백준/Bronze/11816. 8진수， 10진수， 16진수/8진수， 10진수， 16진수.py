import sys, math
input = sys.stdin.readline

n=input().strip()
if n[0]!='0':
    # 10진수
    print(n)
elif n[1]=='x':
    # 16진수
    print(int(n,16))
else:
    # 8진수
    print(int(n,8))