def solution(msg):
    dic=dict()
    for i in range(1,27):
        dic[chr(65+i-1)]=i

    answer = []
    
    idx=0
    ch=''
    for m in msg:
        ch+=m
        if ch in dic:
            idx = dic[ch]
        else:
            answer.append(idx)
            dic[ch]=len(dic)+1
            ch=m
            idx=dic[ch]
    
    answer.append(idx)
    
    return answer