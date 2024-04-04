n=16
m=4
section=[2,3,6,11,13]


answer = 1 # 칠하는 횟수
paint = section[0] # 덧칠 시작점
for i in range(1, len(section)):
    if section[i] - paint >= m:
        answer += 1
        paint = section[i]

print(answer)




