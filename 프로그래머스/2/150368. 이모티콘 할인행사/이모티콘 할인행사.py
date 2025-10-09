"""
할인율은 10,20,30,40 중 하나

"""
def solution(users, emoticons):
    discount_rates = [0.1,0.2,0.3,0.4] # 10%, 20%, 30%, 40%
    result=[0,0]
    def calc(lst):
        cnt, price=0,0
        tmp=0
        for cell_line_rate, plus_price in users:
            buy_total=0
            for emoticon, discount_rate in lst:
                if cell_line_rate <= discount_rate*100:
                    buy_total+=emoticons[emoticon]*(1-discount_rate)
            if plus_price <= buy_total:
                cnt+=1
            else:
                price+=buy_total
            tmp+=1
        return cnt,price
    
    def dfs(depth, lst):
        if depth==len(emoticons):
            register_cnt, cell_price = calc(lst)
            if register_cnt > result[0]:
                result[0] = register_cnt
                result[1] = cell_price
            elif register_cnt == result[0] and cell_price>result[1]:
                result[1]=cell_price
            return
        
        for rate in discount_rates:
            dfs(depth+1,lst+[(depth,rate)])
        
    dfs(0,[])
    
    
    
    return result