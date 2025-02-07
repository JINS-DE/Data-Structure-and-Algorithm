def solution(my_string, queries):
    
    li=list(my_string)
    print(li)
    for i,j in queries:
        li[i:j+1]=li[i:j+1][::-1]
    
    
    print(''.join(li))

    return ''.join(li)