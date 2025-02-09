def solution(friends, gifts):
    dic = dict()
    for i,friend in enumerate(friends):
        dic[friend] = i
    
    gifts_give_li = [[0]*len(friends) for _ in range(len(friends))]
    
    gifts_index=[0]*len(friends)
    
    for gift in gifts:
        A, B = gift.split()
        gifts_give_li[dic[A]][dic[B]]+=1
        gifts_index[dic[A]]+=1
        gifts_index[dic[B]]-=1
    
    expectedGifts=[0]*len(friends)
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            if gifts_give_li[i][j] > gifts_give_li[j][i]:
                expectedGifts[i]+=1
            elif gifts_give_li[i][j] < gifts_give_li[j][i]:
                expectedGifts[j]+=1
            else:
                if gifts_index[i]>gifts_index[j]:
                    expectedGifts[i]+=1
                elif gifts_index[i]<gifts_index[j]:
                    expectedGifts[j]+=1
                  
    return max(expectedGifts)