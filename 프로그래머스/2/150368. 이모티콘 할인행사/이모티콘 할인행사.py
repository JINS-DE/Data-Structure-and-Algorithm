def solution(users, emoticons):
    n,m=len(users),len(emoticons)
    discount=[0.9,0.8,0.7,0.6]
    answer = [0,0]
    def dfs(depth,tmp):
        if depth==m:
            plus=0
            total_sum=0
            for user_rate, plus_price in users:
                tmp_sum=0
                for emo_rate, emo_price in tmp:
                    if user_rate<=emo_rate:
                        tmp_sum+=emo_price                      
                flag = tmp_sum // plus_price
                if flag:
                    plus+=1
                else:
                    total_sum += tmp_sum
            if answer[0]<plus:
                answer[0] = plus
                answer[1] = total_sum
            elif answer[0]==plus and answer[1] < total_sum:
                answer[1]=total_sum
                
            return
        for i in range(4):
            dfs(depth+1,tmp+[[100-discount[i]*100, emoticons[depth]*discount[i]]])

    
    dfs(0,[])
    return answer