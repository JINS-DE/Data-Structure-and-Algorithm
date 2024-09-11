def solution(friends, gifts):
    li = [[0]*len(friends) for _ in range(len(friends))] 
    answer_li=[0]*len(friends)

    for i in gifts: # 2차원 list 생성
        giver,receiver=i.split(' ')
        g=friends.index(giver) # 준 친구
        r=friends.index(receiver) # 받은 친구
        li[r][g]=li[r][g]+1


    present_index=[] # 선물지수!
    for i in range(len(friends)):
        present_index.append(sum(map(lambda x : x[i], li)) -sum(li[i]))


    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            if li[i][j] > li[j][i]:
                answer_li[j] += 1
            elif li[i][j] < li[j][i]:
                answer_li[i] += 1
            else:
                if present_index[i]>present_index[j]:
                    answer_li[i] += 1
                elif present_index[i]<present_index[j]:
                    answer_li[j] += 1
    return max(answer_li)