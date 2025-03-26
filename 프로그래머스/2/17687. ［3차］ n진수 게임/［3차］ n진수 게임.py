def change_jinbeob(n, div):
    if n==0: return '0'
    change_dic = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    li = []
    while n > 0:
        n, mod = divmod(n, div)
        if mod >= 10:
            mod = change_dic[mod]
        li.append(str(mod))
    li.reverse() 
    return ''.join(li)  

def solution(n, t, m, p):
    
    answer = ''
    cnt=0
    num=0
    if p==m: p=0
    while True:
        x=change_jinbeob(num,n)
        print(x)
        for i in x:
            cnt+=1
            if cnt%m==p:
                answer+=i
            if len(answer)==t:
                break
        
        num+=1
        if len(answer)==t:
            break
    # print(answer)
            
    return answer