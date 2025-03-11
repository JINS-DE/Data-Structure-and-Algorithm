from collections import defaultdict
def solution(enroll, referral, seller, amount):
    def reverse_dfs(node, profit):
        if node=="center":
            return
        parent = tree_dic[node]
        devide_money = profit//10
        # print("node:",node)
        # print("profit:",profit)
        # print("devide_money:",devide_money)
        revenue_dic[node]+=profit-devide_money
        if devide_money>0:
            reverse_dfs(parent,devide_money)
        
    
    answer = []
    tree_dic = dict() # 자식 : 부모
    revenue_dic = defaultdict(int)
    for i,v in enumerate(referral):
        if v=="-":
            tree_dic[enroll[i]]="center"
        else:
            tree_dic[enroll[i]]=referral[i]
    
    for i,v in enumerate(seller):
        reverse_dfs(v,amount[i]*100)
    
    answer=[]
    for name in enroll:
        answer.append(revenue_dic[name])
        
    return answer