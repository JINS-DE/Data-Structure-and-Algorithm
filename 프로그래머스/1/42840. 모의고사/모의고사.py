def solution(answers):
    arr1=[1,2,3,4,5]
    arr2=[2, 1, 2, 3, 2, 4, 2, 5]
    arr3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_li = [0,0,0]
    for i, ans in enumerate(answers):
        if arr1[i%len(arr1)] == ans:
            answer_li[0]+=1
        if arr2[i%len(arr2)] == ans:
            answer_li[1]+=1
        if arr3[i%len(arr3)] == ans:
            answer_li[2]+=1
    max_=max(answer_li)
    answer=[]
    for i,val in enumerate(answer_li):
        if val == max_:
            answer.append(i+1)
        
    answer.sort()
    return answer