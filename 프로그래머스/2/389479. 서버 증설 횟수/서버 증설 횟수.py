def solution(players, m, k):
    length=len(players)
    now_server=[0]*(length+k) # 증설된 서버의 수 list
    answer=0
    for i,users in enumerate(players):

        if users>=(now_server[i]+1)*m:
            print("users",users)
            add_server= users//m - now_server[i]
            print("add_server",add_server)
            for j in range(i,i+k):
                now_server[j]+=add_server
            answer+=add_server
            print("now_server",now_server)  
            print("----------------------")
    
            
    return answer