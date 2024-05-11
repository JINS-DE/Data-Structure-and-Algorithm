def solution(friends, gifts):
    answer = 0
    return answer



'''
무지가 프로도보다 선물을 많이 받으면 무지가 프로도에게 선물을 주고
둘이 같으면 
선물 지수가 낮은 사람이 높은 사람에게 선물을 주고
그것조차 같으면 선물은 주고받지 않는다.

선물을 가장 많이 받을 친구의 선물의 수를 알고 싶다. 

'''
friends=["muzi", "ryan", "frodo", "neo"]
gifts=["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
'''
1. 누가 누구한테 선물을 받았나 비교, 갯수 세야함
2. 선물지수를 세야함
'''
# #1 
# [[0,3,1,1],[0,0,1,0],[2,0,0,0],[0,0,0,0]]

# #2 서로 겹치지 않게 비교
# [0,1],[1,0]
# [0,2],[2,0]
# [0,3],[3,0]
# [1,2],[2,1]
# [1,3],[3,1]
# [2,3],[3,2]


# #3 #2를 비교하고 둘이 같을 때 선물지수를 비교 

li=[[0]*len(friends)]*len(friends) #얕은 복사 발생..

li = [[0]*len(friends) for _ in range(len(friends))] # 주고 받는 개수 2차원 리스트화 
answer_li=[0]*len(friends)

for i in gifts: # 2차원 list 생성
    giver,receiver=i.split(' ')
    g=friends.index(giver) # 준 친구
    r=friends.index(receiver) # 받은 친구
    li[r][g]=li[r][g]+1


present_index=[] # 선물지수 
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

print(max(answer_li))
