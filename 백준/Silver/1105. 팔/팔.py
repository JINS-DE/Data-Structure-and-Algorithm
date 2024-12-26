import sys
input = sys.stdin.readline

L, R = input().split()
answer = 0

# 길이가 같을 때만 비교 가능
if len(L) == len(R):
    for i in range(len(L)):
        if L[i] != R[i]:  # 자리 수가 달라지면 비교 중단
            break
        if L[i] == '8':  # 동일한 자리에서 8일 경우만 카운트
            answer += 1

print(answer)
