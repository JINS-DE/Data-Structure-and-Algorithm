from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(int)
    for i in completion:
        dic[i]+=1
    for i in participant:
        if i in dic:
            dic[i]-=1
            if dic[i]<0:
                return i
        elif i not in dic:
            return i
    