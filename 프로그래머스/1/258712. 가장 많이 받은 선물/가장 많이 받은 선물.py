from itertools import combinations
from collections import defaultdict
def solution(friends, gifts):
    friends_idx_dict = {}
    for i,v in enumerate(friends):
        friends_idx_dict[v]=i
    
    giver_board = [[0]*len(friends) for _ in range(len(friends))]
    present_degree = defaultdict(int)
    
    for gift in gifts:
        a,b = gift.split()
        giver_board[friends_idx_dict[a]][friends_idx_dict[b]]+=1
        present_degree[friends_idx_dict[a]]+=1
        present_degree[friends_idx_dict[b]]-=1

    answer = defaultdict(int)
    for a, b in combinations(friends,2):
        a = friends_idx_dict[a]
        b = friends_idx_dict[b]
        if giver_board[a][b] > giver_board[b][a]:
            answer[a]+=1
        elif giver_board[a][b] < giver_board[b][a]:
            answer[b]+=1
        else:    
            if present_degree[a] > present_degree[b]:
                answer[a]+=1
            elif present_degree[a] < present_degree[b]:
                answer[b]+=1
    maximum = 0
    for val in answer.values():
        maximum=max(val,maximum)
    return maximum