import sys, math
input = sys.stdin.readline

n=int(input())
st = input().strip()
answer=0

for s in st:
    
    answer+=int(s)
print(answer)

