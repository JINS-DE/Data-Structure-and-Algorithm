c1=["i", "drink", "water"]
c2=["to","want"]
goal = ["i", "want", "to", "drink", "water"] 

# #처음시도(마지막 테스트에서 실패)
answer='Yes'
index_c1,index_c2=0,0

# for i in goal:
#     if i in c1 :
#         if index_c1 > c1.index(i):
#             answer = 'No'
#             break
#         index_c1 = c1.index(i)

#     elif i in c2:
#         if index_c2 > c2.index(i):
#             answer = 'No'
#             break
#         index_c2 = c2.index(i)
#     else:
#         answer='No'
#         break
# print(answer)



# 다시 풀었음
def solution(c1, c2, goal):    
    answer='Yes'
    index_c1,index_c2=0,0

    for i in goal:
        if len(c1)>index_c1 and c1[index_c1]==i:
            index_c1 += 1
        elif len(c2)>index_c2 and c2[index_c2]==i:
            index_c2 +=1
        else:
            answer='No'
            break

    return answer
print(solution(c1,c2,goal))