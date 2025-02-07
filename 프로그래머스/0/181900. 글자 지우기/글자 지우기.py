def solution(my_string, indices):
    find = set(indices)
    answer=''
    for i in range(len(my_string)):
        if i not in find:
            answer += my_string[i]
    return answer