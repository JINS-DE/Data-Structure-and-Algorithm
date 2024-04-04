def solution(food):
    answer = ''
    cnt=1
    for i in food:
        if i >1:
            for j in range(i//2):
                answer+=str(cnt)
            cnt+=1 
    answer= answer+'0'+answer[::-1]
    return answer

print(solution([1, 3, 4, 6]))