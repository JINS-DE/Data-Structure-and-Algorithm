from collections import defaultdict
def solution(orders, courses):
    def dfs(n,s,st):
        if n==course:
            tmp = ''.join(sorted(st))
            dic[tmp]+=1
            return
        for i in range(s,len(order)):
            dfs(n+1,i+1,st+order[i])
            
    answer = []
    for course in courses:
        dic=defaultdict(int)
        for order in orders:
            if len(order)>=course:
                dfs(0,0,'')
        if dic:
            max_val = max(dic.values())
            if max_val>1:
                for key,val in dic.items():
                    if val==max_val :
                        answer.append(key)
    answer.sort()
        
    return answer