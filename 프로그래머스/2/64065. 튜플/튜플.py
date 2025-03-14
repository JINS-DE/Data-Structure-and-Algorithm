def solution(s):
    answer = []
    li=[]
    
    tmp=set()
    symbol = {'{','}',','}
    
    for i in s.split('},'):

        st=''
        for j in i:
            if j not in symbol:
                st+=j
            elif j==",":
                tmp.add(int(st))
                st=''
        tmp.add(int(st))
        li.append(tmp)
        tmp=set()
    li.sort(key=len)
    
    # print(li)
    prev = set() 
    for group in li:
        current = set(group)
        answer.append((current - prev).pop()) 
        prev = current  

    
        
    return answer