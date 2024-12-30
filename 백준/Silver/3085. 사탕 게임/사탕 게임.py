import sys
input=sys.stdin.readline
n=int(input())
li=[list(input().rstrip()) for _ in range(n)]
answer=0

def check(li):
    n=len(li)
    answer=1
    
    for i in range(n):
        cnt=1
        for j in range(1,n):
            if li[i][j] == li[i][j-1]:
                cnt+=1
            else:
                cnt=1
            if cnt > answer : 
                answer = cnt

        cnt=1
        for j in range(1,n):
            if li[j][i] == li[j-1][i]:
                cnt+=1
            else:
                cnt=1
            if cnt > answer : 
                answer = cnt
    return answer
            

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n :
            li[i][j], li[i][j+1] = li[i][j+1], li[i][j]

            temp = check(li)

            if temp> answer:
                answer = temp
            li[i][j], li[i][j+1] = li[i][j+1], li[i][j]
        # 행 바꾸기
        if i+1 < n :
            li[i][j], li[i+1][j] = li[i+1][j], li[i][j]

            temp = check(li)

            if temp > answer :
                answer = temp
            
            li[i][j], li[i+1][j] = li[i+1][j], li[i][j]

print(answer)

