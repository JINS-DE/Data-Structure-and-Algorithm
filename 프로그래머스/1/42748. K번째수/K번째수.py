def solution(array, commands):        
    answer = []
    for i,j,k in commands:
        a=array[i-1:j]
        a.sort()
        answer.append(a[k-1])
    return answer